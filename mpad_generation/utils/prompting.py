from .metadata import (
    meta_COCO_info, 
    meta_VOC_info_4, 
    voc_fine_grained_classes, 
    coco_fine_grained_classes,
    convert_object,
    coco2voc,
    )
import random

def get_attributes(att):
    if isinstance(att, list):
        return random.choice(att)
    else:
        key = random.choice(list(att.keys()))
        val = get_attributes(att[key])
        return f"{val} {key}"


def prompting(class_name):
    prompt = "a photo of a " + convert_object.get(class_name, class_name)

    # prompt = random.choice(chatGPT_prompts[class_name])
    return prompt


def prompting2(clss, p_fg_fg, apply_fine_grained = True):
    attr = []
    keys = list(meta_VOC_info[clss].keys())
    for i in range( len(keys) -1 ) :#[:-1]:
        att = keys[i]
        if "classes" in att: continue
        values = meta_VOC_info[clss][att]
        if random.random() > 0.7:
            val = random.choice(values)
            attr.append(f'{val} {att}')
            # augment_prompt = '{} {} {},'.format(augment_prompt, val, att)
    
    prompt = f"a {clss} with {', '.join(attr)}"
    
    if apply_fine_grained and p_fg_fg > random.random():
    # if apply_fine_grained and 0.5 > random.random():
        fg_clss = random.choice(meta_VOC_info[clss]["Fine-grained classes"]).lower()
        prompt = prompt + f" and it belongs to the {fg_clss} type."

    return prompt, attr

def prompting3(clss, p_fg_fg, apply_fine_grained = True, apply_mixup = False, \
               num_fine_grained_cls = 2, meta_VOC_info = None):
    attr = []
    keys = list(meta_VOC_info[clss].keys())
    for i in range( len(keys) ) :#[:-1]:
        att = keys[i]
        
        if "classes" in att: continue

        values = meta_VOC_info[clss][att]
        if random.random() > 0.5:
            val = random.choice(values)
            attr.append(f'{val} {att}')
            # augment_prompt = '{} {} {},'.format(augment_prompt, val, att)
    if apply_mixup:
            similar_class = list(meta_VOC_info[clss]['similar classes'].keys())[0]
            
            attr = meta_VOC_info[clss]['similar classes'][similar_class]["distinguished"] + attr
            similar_attr = meta_VOC_info[clss]['similar classes'][similar_class]["similar"]
            # print(similar_attr) 
            base_prompt = f"a {convert_object.get(similar_class, similar_class)} has {', '.join(similar_attr)}"
    
    # print(len(attr))
    # if len(attr) > 0:
    if apply_fine_grained and p_fg_fg > random.random():
        fg_clss = random.choice(meta_VOC_info[clss]["Fine-grained classes"][:num_fine_grained_cls]).lower()
        fg_clss = random.choice(voc_fine_grained_classes[clss]).lower()
    
        prompt = f"a {fg_clss} of {convert_object.get(clss, clss)} category has {', '.join(attr)}"
        base_prompt = f"a {fg_clss} of {convert_object.get(clss, clss)} category has {', '.join(attr)}"
    else:
        prompt = f"a {convert_object.get(clss, clss)} has {', '.join(attr)}"

    if apply_mixup:
        return prompt, base_prompt
    return prompt, attr


def prompting4(clss, p_fg_fg, apply_fine_grained = True, apply_mixup = False, \
               num_fine_grained_cls = 2, meta_VOC_info = None):
    attr = []
    keys = list(meta_VOC_info_4[clss].keys())
    for i in range( len(keys) ) :#[:-1]:
        att = keys[i]
        
        if "classes" in att: continue

        values = meta_VOC_info_4[clss][att]
        if random.random() > 0.5:
            # val = random.choice(values)
            val = get_attributes(values)
            attr.append(f'{val} {att}')
            # augment_prompt = '{} {} {},'.format(augment_prompt, val, att)
    prompt = f"a {convert_object.get(clss, clss)} has {', '.join(attr)}"

    if False:
            similar_class = list(meta_VOC_info[clss]['similar classes'].keys())[0]
            attr = meta_VOC_info[clss]['similar classes'][similar_class]["distinguished"] + attr
            similar_attr = meta_VOC_info[clss]['similar classes'][similar_class]["similar"]
            base_prompt = f"a {convert_object.get(similar_class, similar_class)} has {', '.join(similar_attr)}"
    elif apply_fine_grained:
        # fg_clss = random.choice(meta_VOC_info[clss]["Fine-grained classes"][:num_fine_grained_cls]).lower()
        
        fg_clss = random.choice(voc_fine_grained_classes[clss][:num_fine_grained_cls]).lower()
        prompt = f"a {fg_clss} of {convert_object.get(clss, clss)} category has {', '.join(attr)}"
        base_prompt = f"a {fg_clss} of {convert_object.get(clss, clss)} category has {', '.join(attr)}"
    

    prompt      =   prompt.replace('_', ' ')
    if apply_mixup:
        base_prompt =   base_prompt.replace('_', ' ')
        return prompt, base_prompt
    return prompt, attr

def prompting3_coco(clss, p_fg_fg, apply_fine_grained=True, apply_mixup=False, num_fine_grained_cls=2):
    attr = []
    meta_info = meta_COCO_info
    clss_name = str(clss)
    clss =  clss if clss in list(meta_info.keys()) else coco2voc[clss]
    keys = list(meta_info[clss].keys())
    for i in range( len(keys) ) :#[:-1]:
        att = keys[i]
        
        if "classes" in att: continue

        values = meta_info[clss][att]
        if random.random() > 0.5:
            val = random.choice(values)
            attr.append(f'{val} {att}')
            # augment_prompt = '{} {} {},'.format(augment_prompt, val, att)
    if apply_mixup:
            similar_classes = meta_info[clss]['similar classes']
            similar_class = list(similar_classes.keys())[0]
            
            attr = similar_classes[similar_class]["distinguished"] + attr
            similar_attr = similar_classes[similar_class]["similar"]
            # print(similar_attr) 
            base_prompt = f"a {similar_class} has {', '.join(similar_attr)}"
    
    if apply_fine_grained and p_fg_fg > random.random():
        # fg_clss = random.choice(meta_info[clss]["Fine-grained classes"][:num_fine_grained_cls]).lower()
        fg_clss = random.choice(coco_fine_grained_classes[clss_name][:num_fine_grained_cls]).lower()
        
        prompt = f"a {fg_clss} of {clss_name} category has {', '.join(attr)}"
    else:
        prompt = f"a {clss_name} has {', '.join(attr)}"

    if apply_mixup:
        return prompt, base_prompt
    return prompt, attr

def __prompting3(clss):
    def generate_prompt(category, attributes):
        if category == "bus":
            return f"A {attributes['size']} bus with a {attributes['body shape']} body. It has {attributes['axles']} axles, {attributes['doors']} doors ({attributes['doors placement']} doors), and {attributes['wheels']} wheels. The windows are {attributes['windows']}. The bus features {attributes['headlights']} headlights, a {attributes['grille']} grille, and a {attributes['roof']}. The interior layout includes {attributes['interior layout']}. The color of the bus is {attributes['colors']}. It belongs to the {attributes['Fine-grained classes']} type."
        
        elif category == "cow":
            return f"A {attributes['size']} cow with a {attributes['body']} body covered in {attributes['hair']} hair. It has a {attributes['head']} head with a {attributes['nose']} nose and {attributes['eyes']} eyes. The cow's horns are {attributes['horns']}, and its ears are {attributes['ears']}. It has a {attributes['tail']} tail and a {attributes['udder']} udder. The hooves are {attributes['hooves']}, and it has {attributes['distinctive marking']}. The color is {attributes['colors']}, and it belongs to the {attributes['Fine-grained classes']} type."
        
        elif category == "motorbike":
            return f"A {attributes['design']} motorbike with a {attributes['body']} body and a {attributes['frame']} frame. The bike has {attributes['seat']} seating, {attributes['handlebars']} handlebars, and {attributes['wheels']} wheels. The engine is {attributes['engine']}, and the fuel tank is {attributes['fuel tank']}. The motorbike is equipped with {attributes['headlights']} headlights, {attributes['taillights']} taillights, and {attributes['exhaust pipes']} exhaust pipes. The color of the motorbike is {attributes['colors']}, and it belongs to the {attributes['Fine-grained classes']} type."
        
        elif category == "sofa":
            return f"A {attributes['size']} sofa with a {attributes['frame']} frame and {attributes['upholstery']} upholstery. The texture is {attributes['texture']}, and the cushions are {attributes['cushions']}. It features {attributes['arms']} arms, a {attributes['backrest']} backrest, and {attributes['legs']} legs. The sofa also includes {attributes['features']}. The color is {attributes['colors']}, and it belongs to the {attributes['Fine-grained classes']} type."
        
        else:
            return "Category not recognized."
