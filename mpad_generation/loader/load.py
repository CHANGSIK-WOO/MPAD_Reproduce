import torch
from huggingface_hub import hf_hub_download
from diffusers import UNet2DConditionModel, StableDiffusionPipeline, StableDiffusionInpaintPipeline, StableDiffusionControlNetInpaintPipeline, ControlNetModel, PNDMScheduler, DDIMScheduler, UniPCMultistepScheduler, DPMSolverMultistepScheduler, StableDiffusionXLInpaintPipeline, DPMSolverSinglestepScheduler
from controlnet_aux import HEDdetector, OpenposeDetector
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PowerPaint.utils.utils import TokenizerWrapper, add_tokens
from PowerPaint.pipeline.pipeline_PowerPaint import StableDiffusionInpaintPipeline as Pipeline
from PowerPaint.pipeline.pipeline_PowerPaint_ControlNet import StableDiffusionControlNetInpaintPipeline as controlnetPipeline
from PIL import Image, ImageFilter
from diffusers.pipelines.controlnet.pipeline_controlnet import ControlNetModel
from safetensors.torch import load_model, load_file


def getControlNet(stable_diffusion_name:str, controlnet_name: str, device:str):
    '''
    Load ControlNET condition for Stable Diffusion

    Argument:
        stable_diffusion_name (str) Huggingface Stable Diffusion name
        controlnet_name (str) Huggingface ControlNet condiion name
        device (str) which device to load model ('cpu' or 'cuda')
    '''
    controlnet = ControlNetModel.from_pretrained(controlnet_name, torch_dtype=torch.float16)
    pipe = StableDiffusionControlNetInpaintPipeline.from_pretrained(stable_diffusion_name, controlnet=controlnet, torch_dtype=torch.float16, safety_checker=None)
    # scheduler = DPMSolverSinglestepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_attention_slicing()
    pipe.to(device)

    return pipe

def getDiffusers(model_id:str, device:str):
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    # pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_attention_slicing()
    pipe = pipe.to(device)
    return pipe

def getPowerPaint(stable_inpaint_name:str, stable_diffusion_name:str, 
                unet_name:str,
                text_encoder_name: str,
                device='cpu'):
    pipe = Pipeline.from_pretrained(
        stable_inpaint_name,
        torch_dtype=torch.float16).to(device)
    pipe.tokenizer = TokenizerWrapper(
        from_pretrained=stable_diffusion_name,
        subfolder='tokenizer',
        revision=None)
    add_tokens(
        tokenizer=pipe.tokenizer,
        text_encoder=pipe.text_encoder,
        placeholder_tokens=['P_ctxt', 'P_shape', 'P_obj'],
        initialize_tokens=['a', 'a', 'a'],
        num_vectors_per_token=10)
    #load_model(pipe.unet, unet_name)
    #load_model(pipe.text_encoder, text_encoder_name)
    # 아래처럼 수정
    # UNet 로딩 - strict=False
    print(f"Loading UNet from {unet_name}")
    unet_state_dict = load_file(unet_name)
    pipe.unet.load_state_dict(unet_state_dict, strict=False)
    print("✓ UNet loaded")

    # Text Encoder 로딩 - strict=False
    print(f"Loading Text Encoder from {text_encoder_name}")
    text_encoder_state_dict = load_file(text_encoder_name)
    pipe.text_encoder.load_state_dict(text_encoder_state_dict, strict=False)
    print("✓ Text Encoder loaded")


def getPowerPaint_ControlNet(stable_inpaint_name:str, stable_diffusion_name:str, device='cpu'):
    pipe = Pipeline.from_pretrained(
        stable_inpaint_name,
        torch_dtype=torch.float16).to(device)
    pipe.tokenizer = TokenizerWrapper(
        from_pretrained=stable_diffusion_name,
        subfolder='tokenizer',
        revision=None)
    add_tokens(
        tokenizer=pipe.tokenizer,
        text_encoder=pipe.text_encoder,
        placeholder_tokens=['P_ctxt', 'P_shape', 'P_obj'],
        initialize_tokens=['a', 'a', 'a'],
        num_vectors_per_token=10)
    load_model(pipe.unet, "PowerPaint/models/unet/unet.safetensors")
    load_model(pipe.text_encoder, "PowerPaint/models/text_encoder/text_encoder.safetensors")
    base_control = ControlNetModel.from_pretrained(
                "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16)
    controlnet = controlnetPipeline(pipe.vae,
                pipe.text_encoder,
                pipe.tokenizer,
                pipe.unet,
                base_control,
                pipe.scheduler,
                None,
                None,
                False,
            )
    controlnet.set_progress_bar_config(disable=True)
    return controlnet