meta_VOC_info1 = {
    'aeroplane': {
        "colors": ["white", "silver", "blue", "combination"],
        "body": ["streamlined", "cylindrical"], "wings": ["large", "medium"],
        "tail": ["vertical", "horizontal", "with stabilizers"],
        "engines": ["under the wings", "rear"],
        "landing gear": ["retractable", "fixed"],
        "cockpit windows": ["angular"],
        "markings": ["logos", "stripes", "national insignia"],
        "Fine-grained classes": ["Jet airliner", "Private jet", "Cargo plane", "Military fighter jet",
                                 "Propeller plane", "Glider", "Seaplane"]},

    'bicycle': {
        "colors": ["red", "black", "blue", "white", "combination"],
        "frame": ["thin", "sturdy", "thick"],
        "wheels": ["medium", "rubber tires", "metal spokes"],
        "handlebars": ["flat", "curved"], "seat": ["padded", "firm"], "pedals": ["metal", "plastic"],
        "chain": ["visible", "covered"], "features": ["gears", "fenders", "baskets"],
        "Fine-grained classes": ["Mountain bike", "Road bike", "Hybrid bike", "BMX", "Electric bike"]},

    'boat': {
        "colors": ["white", "blue", "black", "combination"],
        "hull": ["long", "narrow", "wide", "flat"],
        "power": ["motorized", "sail-powered"],
        "deck features": ["cabins", "masts", "navigation equipment"], "controls": ["rudder", "propeller"],
        "Fine-grained classes": ["Sailboat", "Motorboat", "Fishing boat", "Yacht", "Canoe", "Speedboat"]},

    'bottle': {
        "colors": ["transparent", "green", "brown", "blue"],
        "body": ["cylindrical", "square"],
        "neck": ["long", "short"],
        "materials": ["glass", "plastic"],
        "caps": ["screw-top", "corked", "flip-top"],
        "features": ["labels", "branding"],
        "Fine-grained classes": ["Water bottle", "Wine bottle", "Soda bottle", "Milk bottle", "Juice bottle"]},

    'car': {
        "colors": ["black", "white", "red", "blue", "combination"],
        "body": ["compact", "sleek", "large", "boxy"],
        "wheels": ["rubber tires", "metal rims"],
        "features": ["windows", "mirrors", "headlights", "tail lights", "air conditioning", "sound system",
                     "navigation"],
        "Fine-grained classes": ["Sedan", "SUV", "Hatchback", "Convertible", "Truck", "Electric car"]},

    'cat': {
        "colors": ["black", "white", "orange", "grey", "combination"],
        "fur": ["short", "medium", "long"],
        "ears": ["pointed", "rounded"],
        "tail": ["long", "flexible"], "size": ["small", "medium"],
        "body": ["sleek", "muscular", "stocky"],
        "eyes": ["almond-shaped", "round", "green", "yellow", "blue"],
        "expression": ["curious", "alert", "calm"],
        "Fine-grained classes": ["Siamese", "Persian", "Maine Coon", "Bengal", "Sphynx"]},

    'chair': {
        "colors": ["black", "white", "brown", "combination"],
        "frame": ["wood", "metal", "plastic"],
        "seat": ["padded", "hard"], "back": ["high", "medium", "low"],
        "armrests": ["present", "absent"],
        "legs": ["short", "long", "straight", "curved"],
        "design": ["modern", "traditional", "minimalist"],
        "features": ["upholstery", "cushions", "decorative details"],
        "Fine-grained classes": ["Armchair", "Recliner", "Office chair", "Dining chair", "Folding chair"]},

    'diningtable': {
        "colors": ["brown", "black", "white", "combination"],
        "top": ["wood", "glass", "metal"],
        "legs": ["short", "medium", "tall"],
        "shape": ["rectangular", "square", "round"], "features": ["extendable leaves", "decorative legs"],
        "design": ["traditional", "modern", "minimalist"],
        "surface": ["polished", "matte"],
        "Fine-grained classes": ["Round table", "Square table", "Extendable table", "Glass top table"]},

    'dog': {
        "colors": ["black", "brown", "white", "mix"],
        "fur": ["short", "medium", "long"],
        "ears": ["floppy", "semi-floppy", "erect"],
        "tail": ["bushy", "curled", "straight"],
        "size": ["small", "medium", "large"],
        "body": ["muscular", "lean", "stout"],
        "face": ["short snout", "long snout"],
        "eyes": ["round", "almond-shaped", "oval"],
        "expression": ["alert", "gentle", "playful"],
        "distinctive marking": ["spots", "patches", "brindle patterns"],
        "Fine-grained classes": ["Labrador Retriever", "Bulldog", "Poodle", "German Shepherd", "Golden Retriever"]},

    'horse': {
        "colors": ["brown", "black", "white", "combination"],
        "coat": ["short", "sleek"],
        "mane and tail": ["long", "wavy"],
        "body": ["large", "muscular"],
        "legs": ["long"],
        "ears": ["medium", "pointed"],
        "face": ["long", "prominent snout"],
        "eyes": ["large", "expressive"],
        "posture": ["strong", "graceful"],
        "Fine-grained classes": ["Thoroughbred", "Arabian", "Quarter Horse", "Mustang", "Clydesdale"]},

    'person': {
        "colors": ["varied skin tones"],
        "height": ["small", "medium", "tall"],
        "body size": ["slender", "muscular", "stocky"],
        "hair": ["short", "medium", "long", "varied textures"],
        "eyes": ["round", "almond-shaped", "hooded", "brown", "blue", "green", "hazel"],
        "facial features": ["nose", "mouth", "jawlines"],
        "clothing": ["diverse"],
        "expression": ["varied"],
        "Fine-grained classes": ["Men", "Women", "Children", "Athletes", "Professionals"]},

    'pottedplant': {
        "colors": ["green leaves", "brown stems", "colorful flowers"],
        "leaves": ["broad", "thin", "spiky", "succulent"],
        "pot": ["plastic", "ceramic", "clay"],
        "height": ["small", "medium"],
        "features": ["decorative stones", "moss"],
        "Fine-grained classes": ["Succulent", "Fern", "Flowering plant", "Cactus", "Palm"]},

    'sheep': {
        "colors": ["white", "black", "brown", "combination"],
        "wool": ["thick", "curly", "fluffy"], "ears": ["medium", "floppy"],
        "tail": ["short"],
        "body": ["stocky", "robust"],
        "hooves": ["adapted for varied terrain"],
        "face": ["long snout", "short snout"],
        "eyes": ["round", "oval", "calm", "gentle"],
        "Fine-grained classes": ["Merino", "Suffolk", "Dorset", "Katahdin", "Hampshire"]},

    "train":
        {"colors": ["black", "brown", "white", "mix"],
         "exterior": ["sleek", "boxy", "smooth", "ribbed"],
         "train cars": ["connected series"],
         "windows": ["large", "rectangular", "rounded"],
         "wheels": ["sturdy", "metallic"],
         "front": ["streamlined", "rounded", "angular"],
         "features": ["pantographs", "electrical components", "diesel exhausts"],
         "interior": ["seating", "luggage compartments", "dining areas", "sleeping areas"],
         "Fine-grained classes": ["Freight Train", "Passenger Train", "High-Speed Train", "Subway Train", "Monorail",
                                  "Diesel Locomotive", "Electric Locomotive", "Bullet Train"]},

    "tvmonitor": {
        "colors": ["black", "brown", "white", "mix"],
        "screen": ["flat", "rectangular"],
        "bezels": ["slim", "thicker"],
        "size": ["small", "medium", "large"],
        "finish": ["glossy", "matte"],
        "back panel": ["vents", "ports"],
        "stand": ["minimalistic", "wide", "adjustable"],
        "mounting options": ["wall mounting"],
        "display technology": ["LED", "LCD", "OLED"],
        "surface": ["glare-resistant", "anti-reflective"],
        "features": ["built-in speakers", "adjustable controls"],
        "Fine-grained classes": ["CRT TV", "LED Monitor", "LCD TV", "Plasma Screen", "OLED Display", "Smart TV",
                                 "Gaming Monitor"], },
    "bird": {
        "colors": ["black", "brown", "white", "mix"],
        "feathers": ["smooth", "fluffy", "sleek"],
        "beak": ["short", "long", "curved", "straight"],
        "wings": ["broad", "narrow", "pointed"],
        "tail": ["long", "short", "forked"],
        "size": ["small", "medium", "large"],
        "legs": ["thin", "strong", "webbed"],
        "feet": ["sharp claws", "webbed toes", "perching toes"],
        "eyes": ["round", "oval", "sharp"],
        "expression": ["keen", "curious", "calm"],
        "distinctive marking": ["stripes", "spots", "colorful patterns"],
        "Fine-grained classes": ["Sparrow", "Eagle", "Parrot", "Owl", "Penguin", "Peacock"]
    },
    "bus": {
        "colors": ["black", "brown", "white", "mix"],
        "body shape": ["boxy", "flat front", "rounded front"],
        "axles": ["two", "three"],
        "windows": ["large", "rectangular"],
        "doors": ["single", "double", "front", "middle", "rear"],
        "wheels": ["large", "covered by fenders"],
        "headlights": ["large"],
        "grille": ["prominent"],
        "roof": ["flat", "curved", "luggage racks", "air conditioning units"],
        "interior layout": ["rows of seats", "handrails", "overhead compartments", "accessible seating"],
        "size": ["small", "large", "articulated"],
        "Fine-grained classes": ["City bus", "School Bus", "Double-Decker", "Coach", "Minibus", "Articulated Bus"]
    },
    "cow": {
        "colors": ["black", "brown", "white", "mix"],
        "body": ["sturdy", "muscular", "lean", "stocky"],
        "hair": ["short"],
        "head": ["broad"],
        "nose": ["large", "moist"],
        "eyes": ["round", "oval"],
        "horns": ["curved", "straight", "absent"],
        "ears": ["medium-sized", "floppy", "semi-erect"],
        "tail": ["long", "tuft of hair at the end"],
        "udder": ["prominent"],
        "hooves": ["cloven"],
        "size": ["medium", "large"],
        "distinctive marking": ["spots", "patches", "stripes"],
        "Fine-grained classes": ["Holstein", "Jersey", "Hereford", "Angus", "Guernsey", "Ayrshire"]
    },
    "motorbike": {
        "colors": ["black", "brown", "white", "mix"],
        "body": ["sleek", "aerodynamic", "metal", "plastic"],
        "frame": ["narrow", "steel", "aluminum", "carbon fiber"],
        "seat": ["one rider", "two riders", "padded"],
        "handlebars": ["straight", "curved", "clip-on"],
        "wheels": ["spoked", "alloy"],
        "engine": ["visible", "beneath the fuel tank"],
        "fuel tank": ["rounded", "angular"],
        "headlights": ["round", "rectangular", "integrated"],
        "taillights": ["rear positioned"],
        "exhaust pipes": ["chromed", "matte-finished"],
        "design": ["sporty", "aggressive", "classic", "vintage"],
        "Fine-grained classes": ["Cruiser", "Sportbike", "Touring", "Standard", "Dual-sport", "Scooter"]
    },
    "sofa": {
        "colors": ["black", "brown", "white", "mix"],
        "frame": ["wood", "metal", "combination"],
        "upholstery": ["fabric", "leather", "synthetic"],
        "texture": ["smooth", "textured"],
        "cushions": ["plush", "attached", "removable", "firm"],
        "arms": ["straight", "curved", "flared"],
        "backrest": ["low", "medium", "high"],
        "legs": ["short", "wood", "metal", "visible", "hidden"],
        "size": ["compact", "large", "sectional"],
        "features": ["recliners", "storage compartments", "convertible functions"],
        "Fine-grained classes": ["Loveseat", "Sectional", "Sleeper", "Chesterfield", "Recliner", "Modular"]
    },

}
meta_VOC_info = None

meta_VOC_info_1 = {
    "aeroplane": {
        "colors": ["white", "silver", "blue", "varied"],
        "body": ["cylindrical", "sleek"],
        "wings": ["horizontal", "wide", "with engines"],
        "engines": ["two", "four", "on wings", "rear fuselage"],
        "tail": ["vertical stabilizer", "horizontal stabilizers"],
        "nose": ["rounded", "sharp"],
        "windows": ["aligned along fuselage", "passenger windows"],
        "landing gear": ["large wheels", "retractable"],
        "distinctive marking": ["airline logo", "manufacturer decals"],
        "Fine-grained classes": ["Boeing 737", "Airbus A320", "Boeing 747", "Airbus A380", "Lockheed C-130", "Concorde"]
    },
    "bicycle": {
        "colors": ["black", "blue", "red", "green", "varied"],
        "frame": ["metal", "lightweight", "compact"],
        "wheels": ["two", "thin tires", "thick tires"],
        "handlebars": ["flat", "curved"],
        "seat": ["padded", "adjustable"],
        "chain": ["chain-driven", "gear system"],
        "accessories": ["basket", "rack"],
        "Fine-grained classes": ["Road Bike", "Mountain Bike", "BMX", "Cruiser", "Folding Bike", "Hybrid Bike"]
    },
    "boat": {
        "colors": ["white", "blue", "varied"],
        "material": ["fiberglass", "wood"],
        "hull": ["buoyant", "stable"],
        "propulsion": ["sails", "motor", "oars"],
        "deck": ["open", "enclosed"],
        "size": ["small", "large"],
        "accessories": ["cabin", "storage"],
        "Fine-grained classes": ["Sailboat", "Speedboat", "Yacht", "Kayak", "Canoe", "Ferry"]
    },
    "bottle": {
        "colors": ["clear", "green", "brown"],
        "material": ["glass", "plastic"],
        "shape": ["cylindrical", "narrow neck"],
        "closure": ["screw cap", "cork"],
        "size": ["small", "medium", "large"],
        "purpose": ["beverage", "oil storage", "chemical storage"],
        "Fine-grained classes": ["Wine Bottle", "Water Bottle", "Soda Bottle", "Olive Oil Bottle", "Perfume Bottle"]
    },
    "car": {
        "colors": ["black", "white", "silver", "red", "varied"],
        "body": ["metallic", "compact", "spacious"],
        "wheels": ["four", "rubber tires"],
        "lights": ["headlights", "taillights"],
        "interior": ["seating", "dashboard"],
        "size": ["small", "medium", "large"],
        "Fine-grained classes": ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Truck"]
    },
    "cat": {
        "colors": ["black", "white", "orange", "gray", "mix"],
        "fur": ["short", "medium", "long"],
        "eyes": ["round", "almond-shaped"],
        "ears": ["upright", "pointed"],
        "tail": ["long", "flexible"],
        "claws": ["retractable"],
        "body": ["slender", "muscular"],
        "Fine-grained classes": ["Persian", "Siamese", "Maine Coon", "Bengal", "British Shorthair", "Ragdoll"]
    },
    "chair": {
        "materials": ["wood", "metal", "plastic"],
        "features": ["armrests", "no armrests"],
        "legs": ["four legs", "swivel base"],
        "seat": ["cushioned", "solid"],
        "backrest": ["short", "tall"],
        "colors": ["varied"],
        "Fine-grained classes": ["Armchair", "Office Chair", "Dining Chair", "Folding Chair", "Rocking Chair"]
    },
    "diningtable": {
        "shape": ["rectangular", "round", "square"],
        "material": ["wood", "glass", "metal"],
        "size": ["small", "medium", "large"],
        "features": ["extendable", "folding", "fixed"],
        "surface": ["smooth", "textured"],
        "colors": ["varied finishes"],
        "Fine-grained classes": ["Rectangular Table", "Round Table", "Folding Table", "Extendable Table",
                                 "Glass-top Table"]
    },
    "dog": {
        "colors": ["black", "brown", "white", "mix"],
        "fur": ["short", "medium", "long"],
        "ears": ["floppy", "semi-floppy", "erect"],
        "tail": ["bushy", "curled", "straight"],
        "size": ["small", "medium", "large"],
        "body": ["muscular", "lean", "stout"],
        "face": ["short snout", "long snout"],
        "eyes": ["round", "almond-shaped", "oval"],
        "expression": ["alert", "gentle", "playful"],
        "distinctive marking": ["spots", "patches", "brindle patterns"],
        "Fine-grained classes": ["Golden Retriever", "Siberian Husky", "Border Collie", "Shiba Inu", "Chihuahua",
                                 "Dachshund", "Bulldog", "Pomeranian", "German Shepherd",
                                 "Cavalier King Charles Spaniel"]
    },
    "horse": {
        "colors": ["brown", "black", "white", "gray", "chestnut"],
        "body": ["sleek", "muscular"],
        "legs": ["strong", "long"],
        "mane": ["long", "straight", "wavy"],
        "tail": ["long", "flowing"],
        "ears": ["upright"],
        "snout": ["long"],
        "eyes": ["expressive"],
        "Fine-grained classes": ["Thoroughbred", "Arabian", "Clydesdale", "Quarter Horse", "Mustang", "Appaloosa"]
    },
    "person": {
        "skin color": ["varied"],
        "hair": ["straight", "curly", "wavy"],
        "body": ["slim", "muscular", "short", "tall"],
        "eyes": ["brown", "blue", "green"],
        "nose": ["sharp", "round"],
        "age": ["child", "teenager", "adult", "senior"],
        "Fine-grained classes": ["Male", "Female", "Child", "Teenager", "Adult", "Senior"]
    },
    "pottedplant": {
        "leaves": ["broad", "narrow"],
        "stems": ["short", "tall"],
        "pots": ["ceramic", "plastic", "clay"],
        "size": ["small", "medium", "large"],
        "colors": ["green", "varied"],
        "Fine-grained classes": ["Fern", "Cactus", "Succulent", "Orchid", "Bonsai", "Ficus"]
    },
    "sheep": {
        "colors": ["white", "brown", "black"],
        "wool": ["thick", "curly"],
        "legs": ["short", "sturdy"],
        "face": ["wool-covered", "bare"],
        "hooves": ["small", "hard"],
        "Fine-grained classes": ["Merino", "Suffolk", "Dorset", "Rambouillet", "Hampshire"]
    },
    "train": {
        "colors": ["metallic", "varied markings"],
        "design": ["sleek", "boxy"],
        "carriages": ["multiple", "linked"],
        "wheels": ["metal"],
        "tracks": ["metal"],
        "windows": ["large"],
        "Fine-grained classes": ["Freight Train", "Passenger Train", "High-Speed Train", "Metro Train", "Steam Train"]
    },
    "tvmonitor": {
        "screen": ["rectangular", "flat"],
        "frame": ["slim", "black", "silver"],
        "size": ["small", "medium", "large"],
        "features": ["buttons", "remote control"],
        "mounting": ["stand", "wall-mounted"],
        "Fine-grained classes": ["LCD", "LED", "OLED", "Plasma", "CRT"]
    },
    "bird": {
        "colors": ["black", "brown", "white", "blue", "red", "yellow"],
        "feathers": ["short", "long", "colorful"],
        "wings": ["large", "small", "flight", "flightless"],
        "beak": ["long", "short", "curved"],
        "tail": ["short", "long"],
        "legs": ["thin", "perching"],
        "claws": ["sharp", "small"],
        "Fine-grained classes": ["Sparrow", "Eagle", "Parrot", "Pigeon", "Crow", "Hummingbird"],
        "similar classes": {
            "aeroplane": {
                "distinguished": ["feathers", "a beak", "lightweight body"],
                "similar": ["wings", "streamlined body", "ability to glide through the air"]
            },
            "cat": {
                "distinguished": ["feathers", "wings", "a beak"],
                "similar": ["eyes", "ears", "a tail"]
            },
            "dog": {
                "distinguished": ["feathers", "a beak", "wings"],
                "similar": ["limbs", "eyes", "the ability to move on land"]
            }
        }
    },
    "bus": {
        "colors": ["white", "blue", "red", "yellow"],
        "shape": ["rectangular", "large"],
        "wheels": ["four", "six"],
        "windows": ["large", "passenger windows"],
        "doors": ["automatic"],
        "roof": ["flat", "curved"],
        "storage": ["underneath", "overhead"],
        "Fine-grained classes": ["City Bus", "Double-Decker Bus", "Coach Bus", "School Bus", "Shuttle Bus"],

        "similar classes": {
            "train": {
                "distinguished": ["multiple passenger compartments", "large wheels", "city routes"],
                "similar": ["large size", "long structure", "ability to transport many passengers"]
            },
            "car": {
                "distinguished": ["high seating capacity", "longer frame", "dedicated lanes"],
                "similar": ["wheels", "engine-powered", "road-bound transportation"]
            },
            "aeroplane": {
                "distinguished": ["ground-bound movement", "four to six wheels",
                                  "doors for passengers to board directly"],
                "similar": ["transport passengers", "large size", "engine-powered"]
            }
        },
    },
    "cow": {
        "colors": ["black", "white", "brown", "mix"],
        "hair": ["short", "smooth"],
        "body": ["large", "muscular"],
        "legs": ["sturdy", "strong"],
        "hooves": ["hard", "rounded"],
        "face": ["broad", "pronounced nose"],
        "ears": ["short"],
        "tail": ["long", "tuft of hair"],
        "horns": ["present", "absent"],
        "Fine-grained classes": ["Holstein", "Jersey", "Guernsey", "Angus", "Hereford"],
        "similar classes": {
            "horse": {
                "distinguished": ["a bulky body", "horns", "udder"],
                "similar": ["four legs", "hooves", "tail"]
            },
            "sheep": {
                "distinguished": ["a large body", "horns", "udder"],
                "similar": ["four legs", "hooves", "ability to graze"]
            },
            "dog": {
                "distinguished": ["a large body", "hooves", "udder"],
                "similar": ["four legs", "tail", "ability to walk on land"]
            }
        },

    },
    "motorbike": {
        "colors": ["black", "red", "blue", "silver"],
        "frame": ["metallic", "plastic"],
        "wheels": ["two", "thick tires"],
        "engine": ["exposed"],
        "seat": ["centered"],
        "features": ["handlebars", "headlight", "windshield", "saddlebags"],
        "Fine-grained classes": ["Cruiser", "Sportbike", "Scooter", "Touring Bike", "Dirt Bike"],
        "similar classes": {
            "bicycle": {
                "distinguished": ["an engine", "metal frame with more weight", "larger wheels"],
                "similar": ["two wheels", "handlebars", "ability to be balanced by a rider"]
            },
            "car": {
                "distinguished": ["two wheels", "lack of enclosed cabin", "lighter body"],
                "similar": ["engine for propulsion", "metal frame", "ability to transport people"]
            },
            "person": {
                "distinguished": ["mechanical engine", "wheels", "metal frame"],
                "similar": ["ability to move", "carry objects", "propelled in forward direction"]
            }
        },

    },
    "sofa": {
        "colors": ["black", "brown", "beige", "gray", "patterned"],
        "material": ["fabric", "leather"],
        "cushions": ["cushioned seats", "backrests"],
        "features": ["armrests", "sectional"],
        "legs": ["short", "wood", "metal"],
        "Fine-grained classes": ["Sectional Sofa", "Loveseat", "Recliner Sofa", "Sleeper Sofa", "Chaise Lounge"],
        "similar classes": {
            "chair": {
                "distinguished": ["larger seating space", "soft cushions", "support for lying down"],
                "similar": ["seating surface", "back support", "legs"]
            },
            "diningtable": {
                "distinguished": ["soft seating surface", "armrests", "back support"],
                "similar": ["legs", "flat surface", "furniture for household use"]
            },
            "pottedplant": {
                "distinguished": ["seating surface", "back support", "made of fabric or leather"],
                "similar": ["both can be placed indoors", "used to enhance room aesthetics", "stationary in position"]
            }
        },
    }
}

meta_VOC_info_2 = {
    "aeroplane": {
        "colors": ["white", "silver", "blue", "varied"],
        "body": ["cylindrical", "sleek"],
        "wings": ["horizontal", "wide", "with engines"],
        "engines": ["two", "four", "on wings", "rear fuselage"],
        "tail": ["vertical stabilizer", "horizontal stabilizers"],
        "nose": ["rounded", "sharp"],
        "windows": ["aligned along fuselage", "passenger windows"],
        "landing gear": ["large wheels", "retractable"],
        "distinctive marking": ["airline logo", "manufacturer decals"],
        "Fine-grained classes": ["Boeing 737", "Airbus A320", "Boeing 747", "Airbus A380", "Lockheed C-130",
                                 "Concorde"],
        "similar classes": {
            "bird": {
                "distinguished": ["metal body", "engines", "cockpit"],
                "similar": ["wings", "streamlined body", "ability to glide through the air"]
            },
            "boat": {
                "distinguished": ["wings", "engines", "landing gear"],
                "similar": ["elongated body", "smooth surface", "structural form"]
            },
            "bus": {
                "distinguished": ["wings", "propulsion system", "aerodynamic shape"],
                "similar": ["elongated structure", "windows", "large body size"]
            }
        }
    },
    "bicycle": {
        "colors": ["black", "blue", "red", "green", "varied"],
        "frame": ["metal", "lightweight", "compact"],
        "wheels": ["two", "thin tires", "thick tires"],
        "handlebars": ["flat", "curved"],
        "seat": ["padded", "adjustable"],
        "chain": ["chain-driven", "gear system"],
        "accessories": ["basket", "rack"],
        "Fine-grained classes": ["Road Bike", "Mountain Bike", "BMX", "Cruiser", "Folding Bike", "Hybrid Bike"]
    },
    "boat": {
        "colors": ["white", "blue", "varied"],
        "material": ["fiberglass", "wood"],
        "hull": ["buoyant", "stable"],
        "propulsion": ["sails", "motor", "oars"],
        "deck": ["open", "enclosed"],
        "size": ["small", "large"],
        "accessories": ["cabin", "storage"],
        "Fine-grained classes": ["Sailboat", "Speedboat", "Yacht", "Kayak", "Canoe", "Ferry"]
    },
    "bottle": {
        "colors": ["clear", "green", "brown"],
        "material": ["glass", "plastic"],
        "shape": ["cylindrical", "narrow neck"],
        "closure": ["screw cap", "cork"],
        "size": ["small", "medium", "large"],
        "purpose": ["beverage", "oil storage", "chemical storage"],
        "Fine-grained classes": ["Wine Bottle", "Water Bottle", "Soda Bottle", "Olive Oil Bottle", "Perfume Bottle"],
        "similar classes": {
            "pottedplant": {
                "distinguished": ["narrow neck", "cap", "transparent material"],
                "similar": ["cylindrical shape", "vertical orientation"]
            },
            "tvmonitor": {
                "distinguished": ["cylindrical shape", "neck", "liquid content"],
                "similar": ["standing position", "rectangular body part"]
            },
            "chair": {
                "distinguished": ["narrow top", "transparent surface"],
                "similar": ["upright orientation", "base support"]
            }
        }
    },
    "car": {
        "colors": ["black", "white", "silver", "red", "varied"],
        "body": ["metallic", "compact", "spacious"],
        "wheels": ["four", "rubber tires"],
        "lights": ["headlights", "taillights"],
        "interior": ["seating", "dashboard"],
        "size": ["small", "medium", "large"],
        "Fine-grained classes": ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Truck"]
    },
    "cat": {
        "colors": ["black", "white", "orange", "gray", "mix"],
        "fur": ["short", "medium", "long"],
        "eyes": ["round", "almond-shaped"],
        "ears": ["upright", "pointed"],
        "tail": ["long", "flexible"],
        "claws": ["retractable"],
        "body": ["slender", "muscular"],
        "Fine-grained classes": ["Persian", "Siamese", "Maine Coon", "Bengal", "British Shorthair", "Ragdoll"]
    },
    "chair": {
        "materials": ["wood", "metal", "plastic"],
        "features": ["armrests", "no armrests"],
        "legs": ["four legs", "swivel base"],
        "seat": ["cushioned", "solid"],
        "backrest": ["short", "tall"],
        "colors": ["varied"],
        "Fine-grained classes": ["Armchair", "Office Chair", "Dining Chair", "Folding Chair", "Rocking Chair"]
    },
    "diningtable": {
        "shape": ["rectangular", "round", "square"],
        "material": ["wood", "glass", "metal"],
        "size": ["small", "medium", "large"],
        "features": ["extendable", "folding", "fixed"],
        "surface": ["smooth", "textured"],
        "colors": ["varied finishes"],
        "Fine-grained classes": ["Rectangular Table", "Round Table", "Folding Table", "Extendable Table",
                                 "Glass-top Table"]
    },
    "dog": {
        "colors": ["black", "brown", "white", "mix"],
        "fur": ["short", "medium", "long"],
        "ears": ["floppy", "semi-floppy", "erect"],
        "tail": ["bushy", "curled", "straight"],
        "size": ["small", "medium", "large"],
        "body": ["muscular", "lean", "stout"],
        "face": ["short snout", "long snout"],
        "eyes": ["round", "almond-shaped", "oval"],
        "expression": ["alert", "gentle", "playful"],
        "distinctive marking": ["spots", "patches", "brindle patterns"],
        "Fine-grained classes": ["Golden Retriever", "Siberian Husky", "Border Collie", "Shiba Inu", "Chihuahua",
                                 "Dachshund", "Bulldog", "Pomeranian", "German Shepherd",
                                 "Cavalier King Charles Spaniel"]
    },
    "horse": {
        "colors": ["brown", "black", "white", "gray", "chestnut"],
        "body": ["sleek", "muscular"],
        "legs": ["strong", "long"],
        "mane": ["long", "straight", "wavy"],
        "tail": ["long", "flowing"],
        "ears": ["upright"],
        "snout": ["long"],
        "eyes": ["expressive"],
        "Fine-grained classes": ["Thoroughbred", "Arabian", "Clydesdale", "Quarter Horse", "Mustang", "Appaloosa"],
        "similar classes": {
            "dog": {
                "distinguished": ["larger size", "mane", "tail type"],
                "similar": ["quadruped structure", "legs", "head shape"]
            },
            "cow": {
                "distinguished": ["mane", "slimmer body", "tail type"],
                "similar": ["quadruped structure", "muscular legs", "fur"]
            },
            "sheep": {
                "distinguished": ["mane", "muscular structure", "tail type"],
                "similar": ["quadruped shape", "legs", "head structure"]
            }
        }
    },
    "person": {
        "skin color": ["varied"],
        "hair": ["straight", "curly", "wavy"],
        "body": ["slim", "muscular", "short", "tall"],
        "eyes": ["brown", "blue", "green"],
        "nose": ["sharp", "round"],
        "age": ["child", "teenager", "adult", "senior"],
        "Fine-grained classes": ["Male", "Female", "Child", "Teenager", "Adult", "Senior"]
    },
    "pottedplant": {
        "leaves": ["broad", "narrow"],
        "stems": ["short", "tall"],
        "pots": ["ceramic", "plastic", "clay"],
        "size": ["small", "medium", "large"],
        "colors": ["green", "varied"],
        "Fine-grained classes": ["Fern", "Cactus", "Succulent", "Orchid", "Bonsai", "Ficus"]
    },
    "sheep": {
        "colors": ["white", "brown", "black"],
        "wool": ["thick", "curly"],
        "legs": ["short", "sturdy"],
        "face": ["wool-covered", "bare"],
        "hooves": ["small", "hard"],
        "Fine-grained classes": ["Merino", "Suffolk", "Dorset", "Rambouillet", "Hampshire"]
    },
    "train": {
        "colors": ["metallic", "varied markings"],
        "design": ["sleek", "boxy"],
        "carriages": ["multiple", "linked"],
        "wheels": ["metal"],
        "tracks": ["metal"],
        "windows": ["large"],
        "Fine-grained classes": ["Freight Train", "Passenger Train", "High-Speed Train", "Metro Train", "Steam Train"]
    },
    "tvmonitor": {
        "screen": ["rectangular", "flat"],
        "frame": ["slim", "black", "silver"],
        "size": ["small", "medium", "large"],
        "features": ["buttons", "remote control"],
        "mounting": ["stand", "wall-mounted"],
        "Fine-grained classes": ["LCD", "LED", "OLED", "Plasma", "CRT"]
    },
    "bird": {
        "colors": ["black", "brown", "white", "blue", "red", "yellow"],
        "feathers": ["short", "long", "colorful"],
        "wings": ["large", "small", "flight", "flightless"],
        "beak": ["long", "short", "curved"],
        "tail": ["short", "long"],
        "legs": ["thin", "perching"],
        "claws": ["sharp", "small"],
        "Fine-grained classes": ["Sparrow", "Eagle", "Parrot", "Pigeon", "Crow", "Hummingbird"],
        "similar classes": {
            "aeroplane": {
                "distinguished": ["feathers", "a beak", "lightweight body"],
                "similar": ["wings", "streamlined body", "ability to glide through the air"]
            },
            "cat": {
                "distinguished": ["feathers", "wings", "a beak"],
                "similar": ["eyes", "ears", "a tail"]
            },
            "dog": {
                "distinguished": ["feathers", "a beak", "wings"],
                "similar": ["limbs", "eyes", "the ability to move on land"]
            }
        }
    },
    "bus": {
        "colors": ["white", "blue", "red", "yellow"],
        "shape": ["rectangular", "large"],
        "wheels": ["four", "six"],
        "windows": ["large", "passenger windows"],
        "doors": ["automatic"],
        "roof": ["flat", "curved"],
        "storage": ["underneath", "overhead"],
        "Fine-grained classes": ["City Bus", "Double-Decker Bus", "Coach Bus", "School Bus", "Shuttle Bus"],

        "similar classes": {
            "train": {
                "distinguished": ["multiple passenger compartments", "large wheels", "city routes"],
                "similar": ["large size", "long structure", "ability to transport many passengers"]
            },
            "car": {
                "distinguished": ["high seating capacity", "longer frame", "dedicated lanes"],
                "similar": ["wheels", "engine-powered", "road-bound transportation"]
            },
            "aeroplane": {
                "distinguished": ["ground-bound movement", "four to six wheels",
                                  "doors for passengers to board directly"],
                "similar": ["transport passengers", "large size", "engine-powered"]
            }
        },
    },
    "cow": {
        "colors": ["black", "white", "brown", "mix"],
        "hair": ["short", "smooth"],
        "body": ["large", "muscular"],
        "legs": ["sturdy", "strong"],
        "hooves": ["hard", "rounded"],
        "face": ["broad", "pronounced nose"],
        "ears": ["short"],
        "tail": ["long", "tuft of hair"],
        "horns": ["present", "absent"],
        "Fine-grained classes": ["Holstein", "Jersey", "Guernsey", "Angus", "Hereford"],
        "similar classes": {
            "sheep": {
                "distinguished": ["larger body size", "horns", "udder"],
                "similar": ["quadruped structure", "fur texture", "head-body shape"]
            },
            "horse": {
                "distinguished": ["horns", "bulkier body", "udder"],
                "similar": ["quadruped structure", "tail", "muscular legs"]
            },
            "dog": {
                "distinguished": ["larger body", "horns", "tail type"],
                "similar": ["quadruped shape", "head structure", "fur"]
            }
        },

    },
    "motorbike": {
        "colors": ["black", "red", "blue", "silver"],
        "frame": ["metallic", "plastic"],
        "wheels": ["two", "thick tires"],
        "engine": ["exposed"],
        "seat": ["centered"],
        "features": ["handlebars", "headlight", "windshield", "saddlebags"],
        "Fine-grained classes": ["Cruiser", "Sportbike", "Scooter", "Touring Bike", "Dirt Bike"],
        "similar classes": {
            "bicycle": {
                "distinguished": ["an engine", "metal frame with more weight", "larger wheels"],
                "similar": ["two wheels", "handlebars", "ability to be balanced by a rider"]
            },
            "car": {
                "distinguished": ["two wheels", "lack of enclosed cabin", "lighter body"],
                "similar": ["engine for propulsion", "metal frame", "ability to transport people"]
            },
            "person": {
                "distinguished": ["mechanical engine", "wheels", "metal frame"],
                "similar": ["ability to move", "carry objects", "propelled in forward direction"]
            }
        },

    },
    "sofa": {
        "colors": ["black", "brown", "beige", "gray", "patterned"],
        "material": ["fabric", "leather"],
        "cushions": ["cushioned seats", "backrests"],
        "features": ["armrests", "sectional"],
        "legs": ["short", "wood", "metal"],
        "Fine-grained classes": ["Sectional Sofa", "Loveseat", "Recliner Sofa", "Sleeper Sofa", "Chaise Lounge"],
        "similar classes": {
            "chair": {
                "distinguished": ["larger seating area", "multiple cushions"],
                "similar": ["seating structure", "legs", "backrest"]
            },
            "diningtable": {
                "distinguished": ["cushions", "fabric cover", "soft structure"],
                "similar": ["rectangular form", "horizontal surface", "supporting legs"]
            },
            "pottedplant": {
                "distinguished": ["cushioned seating", "fabric texture"],
                "similar": ["rounded, soft appearance"]
            }
        }
    }
}

meta_VOC_info_3 = {
    "aeroplane": {
        "colors": ["white", "silver", "blue", "varied"],
        "body": ["cylindrical", "sleek"],
        "wings": ["horizontal", "wide", "with engines"],
        "engines": ["two", "four", "on wings", "rear fuselage"],
        "tail": ["vertical stabilizer", "horizontal stabilizers"],
        "nose": ["rounded", "sharp"],
        "windows": ["aligned along fuselage", "passenger windows"],
        "landing gear": ["large wheels", "retractable"],
        "distinctive marking": ["airline logo", "manufacturer decals"],
        "Fine-grained classes": ["Boeing 737", "Airbus A320", "Boeing 747", "Airbus A380", "Lockheed C-130", "Concorde"]
    },
    "bicycle": {
        "colors": ["black", "blue", "red", "green", "varied"],
        "frame": ["metal", "lightweight", "compact"],
        "wheels": ["two", "thin tires", "thick tires"],
        "handlebars": ["flat", "curved"],
        "seat": ["padded", "adjustable"],
        "chain": ["chain-driven", "gear system"],
        "accessories": ["basket", "rack"],
        "Fine-grained classes": ["Road Bike", "Mountain Bike", "BMX", "Cruiser", "Folding Bike", "Hybrid Bike"]
    },
    "boat": {
        "colors": ["white", "blue", "varied"],
        "material": ["fiberglass", "wood"],
        "hull": ["buoyant", "stable"],
        "propulsion": ["sails", "motor", "oars"],
        "deck": ["open", "enclosed"],
        "size": ["small", "large"],
        "accessories": ["cabin", "storage"],
        "Fine-grained classes": ["Sailboat", "Speedboat", "Yacht", "Kayak", "Canoe", "Ferry"],
        "similar classes": {
            "bus": {
                "distinguished": ["land-based movement", "wheels", "doors"],
                "similar": ["elongated body", "window arrangement", "structured form"]
            },
            "car": {
                "distinguished": ["wheels", "ground movement", "engine"],
                "similar": ["elongated body", "smooth surface", "enclosed cabin"]
            },
            "train": {
                "distinguished": ["rails", "multiple compartments", "wheels"],
                "similar": ["elongated structure", "window pattern", "transport design"]
            }
        }
    },
    "bottle": {
        "colors": ["clear", "green", "brown"],
        "material": ["glass", "plastic"],
        "shape": ["cylindrical", "narrow neck"],
        "closure": ["screw cap", "cork"],
        "size": ["small", "medium", "large"],
        "purpose": ["beverage", "oil storage", "chemical storage"],
        "Fine-grained classes": ["Wine Bottle", "Water Bottle", "Soda Bottle", "Olive Oil Bottle", "Perfume Bottle"]
    },
    "car": {
        "colors": ["black", "white", "silver", "red", "varied"],
        "body": ["metallic", "compact", "spacious"],
        "wheels": ["four", "rubber tires"],
        "lights": ["headlights", "taillights"],
        "interior": ["seating", "dashboard"],
        "size": ["small", "medium", "large"],
        "Fine-grained classes": ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Truck"]
    },
    "cat": {
        "colors": ["black", "white", "orange", "gray", "mix"],
        "fur": ["short", "medium", "long"],
        "eyes": ["round", "almond-shaped"],
        "ears": ["upright", "pointed"],
        "tail": ["long", "flexible"],
        "claws": ["retractable"],
        "body": ["slender", "muscular"],
        "Fine-grained classes": ["Persian", "Siamese", "Maine Coon", "Bengal", "British Shorthair", "Ragdoll"],
        "similar classes": {
            "dog": {
                "distinguished": ["smaller size", "claws", "purring"],
                "similar": ["quadruped body", "fur", "tail"]
            },
            "cow": {
                "distinguished": ["larger body", "hooves", "udder"],
                "similar": ["four-legged structure", "fur texture", "head shape"]
            },
            "horse": {
                "distinguished": ["larger size", "mane", "tail type"],
                "similar": ["quadruped body", "muscular legs", "fur coat"]
            }
        }
    },
    "chair": {
        "materials": ["wood", "metal", "plastic"],
        "features": ["armrests", "no armrests"],
        "legs": ["four legs", "swivel base"],
        "seat": ["cushioned", "solid"],
        "backrest": ["short", "tall"],
        "colors": ["varied"],
        "Fine-grained classes": ["Armchair", "Office Chair", "Dining Chair", "Folding Chair", "Rocking Chair"]
    },
    "diningtable": {
        "shape": ["rectangular", "round", "square"],
        "material": ["wood", "glass", "metal"],
        "size": ["small", "medium", "large"],
        "features": ["extendable", "folding", "fixed"],
        "surface": ["smooth", "textured"],
        "colors": ["varied finishes"],
        "Fine-grained classes": ["Rectangular Table", "Round Table", "Folding Table", "Extendable Table",
                                 "Glass-top Table"]
    },
    "dog": {
        "colors": ["black", "brown", "white", "mix"],
        "fur": ["short", "medium", "long"],
        "ears": ["floppy", "semi-floppy", "erect"],
        "tail": ["bushy", "curled", "straight"],
        "size": ["small", "medium", "large"],
        "body": ["muscular", "lean", "stout"],
        "face": ["short snout", "long snout"],
        "eyes": ["round", "almond-shaped", "oval"],
        "expression": ["alert", "gentle", "playful"],
        "distinctive marking": ["spots", "patches", "brindle patterns"],
        "Fine-grained classes": ["Golden Retriever", "Siberian Husky", "Border Collie", "Shiba Inu", "Chihuahua",
                                 "Dachshund", "Bulldog", "Pomeranian", "German Shepherd",
                                 "Cavalier King Charles Spaniel"]
    },
    "horse": {
        "colors": ["brown", "black", "white", "gray", "chestnut"],
        "body": ["sleek", "muscular"],
        "legs": ["strong", "long"],
        "mane": ["long", "straight", "wavy"],
        "tail": ["long", "flowing"],
        "ears": ["upright"],
        "snout": ["long"],
        "eyes": ["expressive"],
        "Fine-grained classes": ["Thoroughbred", "Arabian", "Clydesdale", "Quarter Horse", "Mustang", "Appaloosa"]
    },
    "person": {
        "skin color": ["varied"],
        "hair": ["straight", "curly", "wavy"],
        "body": ["slim", "muscular", "short", "tall"],
        "eyes": ["brown", "blue", "green"],
        "nose": ["sharp", "round"],
        "age": ["child", "teenager", "adult", "senior"],
        "Fine-grained classes": ["Male", "Female", "Child", "Teenager", "Adult", "Senior"]
    },
    "pottedplant": {
        "leaves": ["broad", "narrow"],
        "stems": ["short", "tall"],
        "pots": ["ceramic", "plastic", "clay"],
        "size": ["small", "medium", "large"],
        "colors": ["green", "varied"],
        "Fine-grained classes": ["Fern", "Cactus", "Succulent", "Orchid", "Bonsai", "Ficus"]
    },
    "sheep": {
        "colors": ["white", "brown", "black"],
        "wool": ["thick", "curly"],
        "legs": ["short", "sturdy"],
        "face": ["wool-covered", "bare"],
        "hooves": ["small", "hard"],
        "Fine-grained classes": ["Merino", "Suffolk", "Dorset", "Rambouillet", "Hampshire"],
        "similar classes": {
            "cow": {
                "distinguished": ["larger size", "horns", "udder"],
                "similar": ["quadruped shape", "fur texture", "head-body structure"]
            },
            "dog": {
                "distinguished": ["different head shape", "tail type"],
                "similar": ["quadruped structure", "fur", "legs"]
            },
            "horse": {
                "distinguished": ["larger body", "mane", "muscular build"],
                "similar": ["four-legged structure", "tail", "fur coat"]
            }
        }
    },
    "train": {
        "colors": ["metallic", "varied markings"],
        "design": ["sleek", "boxy"],
        "carriages": ["multiple", "linked"],
        "wheels": ["metal"],
        "tracks": ["metal"],
        "windows": ["large"],
        "Fine-grained classes": ["Freight Train", "Passenger Train", "High-Speed Train", "Metro Train", "Steam Train"]
    },
    "tvmonitor": {
        "screen": ["rectangular", "flat"],
        "frame": ["slim", "black", "silver"],
        "size": ["small", "medium", "large"],
        "features": ["buttons", "remote control"],
        "mounting": ["stand", "wall-mounted"],
        "Fine-grained classes": ["LCD", "LED", "OLED", "Plasma", "CRT"]
    },
    "bird": {
        "colors": ["black", "brown", "white", "blue", "red", "yellow"],
        "feathers": ["short", "long", "colorful"],
        "wings": ["large", "small", "flight", "flightless"],
        "beak": ["long", "short", "curved"],
        "tail": ["short", "long"],
        "legs": ["thin", "perching"],
        "claws": ["sharp", "small"],
        "Fine-grained classes": ["Sparrow", "Eagle", "Parrot", "Pigeon", "Crow", "Hummingbird"],
        "similar classes": {
            "aeroplane": {
                "distinguished": ["feathers", "a beak", "lightweight body"],
                "similar": ["wings", "streamlined body", "ability to glide through the air"]
            },
            "cat": {
                "distinguished": ["feathers", "wings", "a beak"],
                "similar": ["eyes", "ears", "a tail"]
            },
            "dog": {
                "distinguished": ["feathers", "a beak", "wings"],
                "similar": ["limbs", "eyes", "the ability to move on land"]
            }
        }
    },
    "bus": {
        "colors": ["white", "blue", "red", "yellow"],
        "shape": ["rectangular", "large"],
        "wheels": ["four", "six"],
        "windows": ["large", "passenger windows"],
        "doors": ["automatic"],
        "roof": ["flat", "curved"],
        "storage": ["underneath", "overhead"],
        "Fine-grained classes": ["City Bus", "Double-Decker Bus", "Coach Bus", "School Bus", "Shuttle Bus"],

        "similar classes": {
            "train": {
                "distinguished": ["multiple passenger compartments", "large wheels", "city routes"],
                "similar": ["large size", "long structure", "ability to transport many passengers"]
            },
            "car": {
                "distinguished": ["high seating capacity", "longer frame", "dedicated lanes"],
                "similar": ["wheels", "engine-powered", "road-bound transportation"]
            },
            "aeroplane": {
                "distinguished": ["ground-bound movement", "four to six wheels",
                                  "doors for passengers to board directly"],
                "similar": ["transport passengers", "large size", "engine-powered"]
            }
        },
    },
    "cow": {
        "colors": ["black", "white", "brown", "mix"],
        "hair": ["short", "smooth"],
        "body": ["large", "muscular"],
        "legs": ["sturdy", "strong"],
        "hooves": ["hard", "rounded"],
        "face": ["broad", "pronounced nose"],
        "ears": ["short"],
        "tail": ["long", "tuft of hair"],
        "horns": ["present", "absent"],
        "Fine-grained classes": ["Holstein", "Jersey", "Guernsey", "Angus", "Hereford"],
        "similar classes": {
            "horse": {
                "distinguished": ["a bulky body", "horns", "udder"],
                "similar": ["four legs", "hooves", "tail"]
            },
            "sheep": {
                "distinguished": ["a large body", "horns", "udder"],
                "similar": ["four legs", "hooves", "ability to graze"]
            },
            "dog": {
                "distinguished": ["a large body", "hooves", "udder"],
                "similar": ["four legs", "tail", "ability to walk on land"]
            }
        },

    },
    "motorbike": {
        "colors": ["black", "red", "blue", "silver"],
        "frame": ["metallic", "plastic"],
        "wheels": ["two", "thick tires"],
        "engine": ["exposed"],
        "seat": ["centered"],
        "features": ["handlebars", "headlight", "windshield", "saddlebags"],
        "Fine-grained classes": ["Cruiser", "Sportbike", "Scooter", "Touring Bike", "Dirt Bike"],
        "similar classes": {
            "bicycle": {
                "distinguished": ["engine", "thicker frame", "speed"],
                "similar": ["two wheels", "handlebars", "frame structure"]
            },
            "car": {
                "distinguished": ["four wheels", "enclosed cabin", "larger size"],
                "similar": ["mechanical components", "engine", "seating"]
            },
            "person": {
                "distinguished": ["mechanical body", "wheels"],
                "similar": ["riding position", "overall silhouette"]
            }
        },

    },
    "sofa": {
        "colors": ["black", "brown", "beige", "gray", "patterned"],
        "material": ["fabric", "leather"],
        "cushions": ["cushioned seats", "backrests"],
        "features": ["armrests", "sectional"],
        "legs": ["short", "wood", "metal"],
        "Fine-grained classes": ["Sectional Sofa", "Loveseat", "Recliner Sofa", "Sleeper Sofa", "Chaise Lounge"],
        "similar classes": {
            "chair": {
                "distinguished": ["larger seating space", "soft cushions", "support for lying down"],
                "similar": ["seating surface", "back support", "legs"]
            },
            "diningtable": {
                "distinguished": ["soft seating surface", "armrests", "back support"],
                "similar": ["legs", "flat surface", "furniture for household use"]
            },
            "pottedplant": {
                "distinguished": ["seating surface", "back support", "made of fabric or leather"],
                "similar": ["both can be placed indoors", "used to enhance room aesthetics", "stationary in position"]
            }
        },
    }
}

meta_VOC_info_4 = {
    "bird": {
        "colors": ["blue", "red", "yellow", "green", "white", "black", "spotted", "striped"],
        "feathers": ["soft", "fluffy", "sleek", "glossy", "iridescent"],
        "body": {
            "weight": ["lightweight"],
            "shape": ["streamlined"],
            "features": ["hollow bones"]
        },
        "beak": ["short and pointed", "long and curved", "varied based on diet and habitat"],
        "wings": {
            "type": ["long", "strong"],
            "features": ["structured feathers for lift and maneuverability"]
        },
        "legs": {
            "type": ["thin", "sturdy"],
            "ends": ["claws", "webbed feet"]
        },
        "face": {
            "beak": ["short and pointed", "long and curved"],
            "eyes": {
                "shape": ["round"],
                "colors": ["black", "brown", "yellow", "vibrant shades"]
            }
        },
        "expression": ["alert", "curious"],
        "behavior": ["flying", "singing", "hunting", "nesting"]
    },

    "bus": {
        "colors": ["yellow", "white", "blue", "green", "red", "reflective patterns"],
        "body": {
            "size": ["large"],
            "shape": ["rectangular", "boxy"],
            "surface": ["smooth", "painted metallic"]
        },
        "windows": ["linear", "tinted glass", "clear glass"],
        "wheels": {
            "shape": ["circular"],
            "features": ["large", "thick rubber tires"]
        },
        "parts": ["doors", "mirrors", "headlights", "grille"],
        "doors": {
            "type": ["wide", "automatic"],
            "purpose": ["passenger entry", "passenger exit"]
        },
        "front": {
            "features": ["large windshield", "rectangular headlights", "circular headlights", "varied grille design"]
        },
        "interior": {
            "features": ["rows of seats", "handrails", "storage areas"],
            "qualities": ["comfortable", "safe"]
        },
        "movement": ["stopping", "boarding passengers", "deboarding passengers", "fixed routes"],
        "sound": ["low rumble", "quieter in electric models", "louder in diesel models"],
        "purpose": ["mass transportation", "functional", "practical"]
    },

    "cow": {
        "colors": ["black", "white", "brown", "tan", "spotted", "patched"],
        "body": {
            "size": ["large", "stocky"],
            "fur": ["short", "smooth"],
            "shape": ["bulky torso", "broad back", "straight or slightly arched spine"]
        },
        "head": {
            "features": ["large size", "flat snout", "long ears", "expressive eyes"]
        },
        "legs": {
            "type": ["strong", "short"],
            "ends": ["cloven hooves"]
        },
        "tail": {
            "type": ["long", "slender"],
            "ends": ["tuft of hair"]
        },
        "udder": ["large", "rounded", "used for milk production"],
        "horns": ["curved", "straight", "absent in some breeds"],
        "expression": ["calm", "docile"],
        "behavior": ["grazing", "chewing cud", "moving in herds"],
        "sound": ["moo"],
        "environment": ["pastures", "barns"]
    },

    "motorbike": {
        "colors": ["black", "white", "red", "blue", "silver", "custom-painted designs"],
        "body": {
            "size": ["compact"],
            "shape": ["aerodynamic"],
            "frame": ["lightweight metals", "aluminum", "steel"],
            "surface": ["smooth", "glossy"]
        },
        "wheels": {
            "shape": ["circular"],
            "rims": ["alloy", "steel"],
            "tires": ["durable", "rubber", "designed for traction"]
        },
        "parts": ["handlebars", "mirrors", "headlights"],
        "engine": {
            "position": ["central"],
            "features": ["visible exhaust system"]
        },
        "seat": {
            "type": ["narrow", "cushioned"],
            "capacity": ["one rider", "two riders"]
        },
        "suspension": ["stability", "control during movement"],
        "movement": ["accelerating", "braking", "leaning into turns"],
        "sound": ["quiet hums in electric models", "loud roars in high-performance engines"],
        "association": ["freedom", "adventure", "utility"],
        "environment": ["urban", "rural"]
    },

    "sofa": {
        "colors": ["beige", "gray", "black", "red", "blue", "patterned designs"],
        "body": {
            "shape": ["rectangular", "rounded"],
            "surface": ["soft", "cushioned"],
            "materials": ["leather", "fabric", "microfiber"]
        },
        "legs": {
            "type": ["wooden", "metallic", "hidden"]
        },
        "parts": ["armrests", "backrests", "cushions"],
        "armrests": ["wide and padded", "slim and minimalistic"],
        "backrests": ["high", "low", "reclinable"],
        "cushions": ["foam fillings", "down fillings", "soft", "durable"],
        "purpose": ["sitting", "lounging", "sleeping"],
        "expression": ["minimalist", "modern", "luxurious", "ornate"],
        "environment": ["living rooms", "offices", "waiting areas"]
    },

    "aeroplane": {
        "colors": ["white", "blue", "red", "camouflaged", "gray"],
        "surface": ["smooth", "metallic"],
        "body": ["elongated", "streamlined"],
        "wings": {
            "size": ["wide"],
            "shapes": ["straight", "swept", "delta"]
        },
        "engines": {
            "location": ["under wings", "on tail"],
            "type": ["jet engines", "propellers"]
        },
        "wheels": {
            "type": ["retractable"],
            "location": ["fuselage"]
        },
        "cockpit": ["front location", "transparent windows"],
        "tail": ["vertical stabilizer", "horizontal stabilizer"],
        "actions": ["takeoff", "cruising", "landing"],
        "sounds": ["engine noise"]
    },

    "bicycle": {
        "colors": ["black", "white", "red", "blue", "vibrant combinations"],
        "surface": ["smooth", "glossy", "matte"],
        "frame": {
            "materials": ["steel", "aluminum", "carbon fiber"],
            "geometry": ["triangular", "diamond-shaped"]
        },
        "wheels": {
            "rims": ["thin", "circular", "aluminum", "carbon fiber"],
            "tires": ["rubber", "smooth", "treaded"]
        },
        "handlebars": ["flat", "curved", "drop-style"],
        "saddle": ["padded", "adjustable height"],
        "drivetrain": ["pedals", "chain", "gears"],
        "actions": ["cruising", "climbing hills", "traversing trails"],
        "movements": ["pedaling", "turning", "braking"],
        "sounds": ["clicking gears", "brake squeaks"]
    },

    "boat": {
        "colors": ["white", "blue", "red", "striped", "painted designs"],
        "hull": {
            "materials": ["wood", "fiberglass", "metal"],
            "shapes": ["flat-bottomed", "V-shaped", "rounded"],
            "finish": ["glossy", "matte"]
        },
        "structure": {
            "deck": ["sturdy", "plank", "composite"],
            "bow": ["pointed", "rounded"],
            "components": ["masts", "motors", "rudders"]
        },
        "accessories": ["anchors", "life buoys", "ropes"],
        "interior": {
            "features": ["cabins", "open seating areas"],
            "parts": ["storage", "comfort zones"]
        },
        "action": ["floating", "sailing", "speeding"]
    },

    "bottle": {
        "colors": ["clear", "green", "blue", "opaque"],
        "materials": ["plastic", "glass", "metal"],
        "shape": ["cylindrical", "rectangular"],
        "surface": ["smooth", "textured", "glossy", "matte"],
        "structure": {
            "neck": ["narrower than body"],
            "opening": ["threaded", "corked"],
            "caps_or_lids": ["screw-on", "flip-top", "cork stoppers"],
            "handles_or_grips": ["handles", "indented grips"]
        },
        "interior": {
            "design": ["hollow"],
            "use": ["liquids", "powders", "substances"],
            "features": ["nozzle", "straw", "dropper"]
        },
        "action": ["pouring", "storing", "transporting"]
    },
    "car": {
        "colors": ["black", "white", "red", "blue", "metallic shades"],
        "materials": ["metal", "plastic", "glass"],
        "design": ["sleek", "aerodynamic"],
        "features": ["hood", "roof", "trunk"],
        "structure": {
            "wheels": ["four", "sporty", "rugged", "all-terrain"],
            "doors": ["two", "four", "traditional", "sliding", "lifting"],
            "sections": ["front", "rear"],
            "parts": ["headlights", "taillights", "grills"]
        },
        "interior": {
            "features": ["seats", "steering wheel", "dashboard"],
            "extras": ["upholstery", "air conditioning", "infotainment systems", "sunroofs", "cup holders",
                       "foldable seats"]
        },
        "functional_parts": ["mirrors", "wipers", "exhaust pipes"],
        "action": ["accelerating", "braking", "parking"]
    },

    "cat": {
        "colors": ["black", "white", "gray", "orange", "brown", "striped", "spotted", "calico"],
        "fur": ["soft", "smooth", "short", "long"],
        "body": ["flexible", "lightweight", "sleek", "agile"],
        "legs": {
            "type": ["slender", "strong"],
            "ends": ["padded paws", "retractable claws"]
        },
        "face": {
            "shape": ["triangular"],
            "eyes": {
                "shape": ["almond-shaped"],
                "colors": ["green", "blue", "yellow", "amber"]
            },
            "ears": ["upright", "pointed"],
            "nose": ["small", "pink", "black"],
            "whiskers": ["long", "sensitive"]
        },
        "behavior": ["purring", "meowing", "hunting", "grooming"]
    },

    "chair": {
        "materials": ["wood", "metal", "plastic", "upholstered fabric"],
        "colors": ["black", "white", "brown", "gray", "vibrant hues"],
        "structure": {
            "shapes": ["rectangular", "square", "rounded"],
            "components": ["seat", "backrest"],
            "seat_types": ["cushioned", "contoured", "flat"]
        },
        "legs": {
            "count": ["four"],
            "styles": ["single pedestal", "cantilever"],
            "features": ["protective caps", "wheels"]
        },
        "armrests": ["curved", "straight"],
        "behavior": ["swiveling", "folding", "reclining"],
        "settings": ["dining", "office", "relaxation spaces"]
    },

    "diningtable": {
        "materials": ["wood", "metal", "glass", "composite materials"],
        "colors": ["natural wood tones", "white", "black", "stained finishes"],
        "tabletop": {
            "surface": ["flat"],
            "shapes": ["rectangular", "circular", "square", "oval"],
            "features": ["decorative patterns", "smooth finishes", "protective coatings"]
        },
        "support": {
            "type": ["legs", "pedestals"],
            "styles": ["straight", "carved", "tapered"]
        },
        "mechanisms": ["extendable", "foldable"],
        "height": ["consistent for dining"],
        "settings": ["formal", "informal"],
        "designs": ["modern", "rustic", "classic"]
    },

    "dog": {
        "colors": ["brown", "black", "white", "golden", "gray", "spotted", "brindle"],
        "fur": ["smooth", "short", "long", "fluffy"],
        "body_structure": ["balanced", "athletic", "small", "large"],
        "ears": ["floppy", "upright", "semi-erect"],
        "tail": ["bushy", "curled", "straight"],
        "face": {
            "muzzle": ["pronounced"],
            "nose": ["wet", "black", "brown"]
        },
        "eyes": {
            "expression": ["expressive"],
            "colors": ["brown", "blue", "hazel"]
        },
        "mouth": ["panting", "smiling", "barking"],
        "legs": {
            "type": ["sturdy"],
            "ends": ["padded paws", "claws"]
        },
        "emotions": ["playful", "excited", "calm", "alert"],
        "actions": ["running", "barking", "wagging tail", "interacting socially"]
    },

    "horse": {
        "colors": ["chestnut", "bay", "black", "gray", "white", "palomino", "dappled", "roan", "spotted"],
        "coat": ["smooth", "shiny"],
        "body_structure": ["strong", "muscular", "speed", "endurance"],
        "neck": ["long"],
        "chest": ["broad"],
        "mane_and_tail": ["long", "flowing"],
        "face": {
            "muzzle": ["long", "straight"],
            "nostrils": ["large"],
            "jaw": ["prominent"]
        },
        "eyes": {
            "size": ["large"],
            "placement": ["set wide apart"],
            "colors": ["brown", "black"],
            "expression": ["calm", "alert"]
        },
        "legs": {
            "type": ["slender", "powerful"],
            "ends": ["hard hooves", "durable"]
        },
        "emotions": ["calmness", "alertness", "excitement"],
        "actions": ["running", "trotting", "galloping", "grazing"]
    },

    "person": {
        "skin_tones": ["pale", "fair", "tan", "dark"],
        "body_shapes": ["slender", "athletic", "stocky"],
        "hair": {
            "colors": ["black", "brown", "blonde", "red", "gray", "white"],
            "textures": ["straight", "wavy", "curly", "coiled"]
        },
        "eyes": {
            "shapes": ["round", "almond-shaped"],
            "colors": ["brown", "blue", "green", "gray", "hazel"]
        },
        "face": {
            "nose": ["varied sizes and shapes"],
            "lips": ["thin", "full", "medium"],
            "eyebrows": ["frame the eyes", "contribute to expressions"]
        },
        "arms_and_legs": {
            "proportions": ["proportional length"],
            "ends": {
                "hands": ["fingers"],
                "feet": ["toes"]
            }
        },
        "emotions": ["happiness", "sadness", "surprise", "confidence", "curiosity", "anxiety"],
        "actions": ["walking", "running", "sitting", "talking"]
    },

    "pottedplant": {
        "colors": ["green", "red", "yellow", "pink", "white"],
        "leaves": {
            "shape": ["oval", "round", "narrow", "pointed"],
            "edges": ["smooth", "wavy", "serrated"],
            "texture": ["glossy", "velvety", "leathery"]
        },
        "stems": ["sturdy", "upright", "trailing", "visible nodes", "internodes"],
        "pot": {
            "materials": ["clay", "ceramic", "plastic", "metal"],
            "shapes": ["cylindrical", "rectangular", "round"]
        },
        "roots": ["contained within soil"],
        "soil": ["rich", "moist", "sandy", "rocky"],
        "decorations": ["moss", "pebbles", "mulch"],
        "expression": ["serene", "decorative"],
        "behavior": ["blooming", "growing", "wilting"]
    },

    "sheep": {
        "colors": ["white", "cream", "black", "mixed patterns"],
        "fleece": ["soft", "dense", "insulating"],
        "body": ["sturdy", "rounded", "compact"],
        "hooves": {
            "type": ["small", "split"],
            "function": ["grip on uneven ground"]
        },
        "face": {
            "snout": ["long", "slightly tapered"],
            "eyes": {
                "shape": ["almond-shaped"],
                "colors": ["brown", "black", "amber"]
            },
            "ears": ["medium-sized", "point outward or downward"]
        },
        "behavior": ["grazing", "flocking", "playful bounding"]
    },
    "train": {
        "colors": ["black", "white", "red", "blue", "green", "yellow"],
        "body": {
            "structure": ["long", "cylindrical", "aerodynamic", "boxy"],
            "features": ["windows", "doors", "painted patterns", "logos"]
        },
        "wheels": ["large", "metallic", "attached to undercarriage"],
        "interior": {
            "features": ["rows of seats", "storage areas", "standing sections"],
            "facilities": ["lighting", "air conditioning", "luggage racks"]
        },
        "locomotive": {
            "components": ["engine", "control panel"]
        },
        "sounds": ["whistles", "horns", "clattering wheels"],
        "expression": ["sleek", "modern", "vintage", "industrial"],
        "behavior": ["starting", "stopping", "motion at varying speeds"],
        "purpose": ["transportation of passengers", "transportation of cargo"]
    },
    "tvmonitor": {
        "colors": ["black", "gray", "silver"],
        "screen": {
            "shape": ["rectangular"],
            "features": ["thin bezels", "flat surface", "curved surface"],
            "resolution": ["high-definition", "ultra-high-definition"]
        },
        "stand": {
            "materials": ["metal", "plastic"],
            "features": ["sturdy", "adjustable angles"]
        },
        "ports": ["HDMI", "USB", "VGA"],
        "additional_features": ["built-in speakers", "ventilation grilles", "control buttons"],
        "control": ["remote control"],
        "placement": ["wall-mounted", "on stand"],
        "expression": ["modern", "minimalistic", "professional", "high-tech"],
        "behavior": ["display static images", "display dynamic video", "switch channels", "adjust brightness",
                     "connect to external devices"]
    },
}



meta_COCO_info_T1 = {
    "bird": {
        "colors": ["black", "brown", "white", "mix"],
        "feathers": ["smooth", "fluffy", "sleek"],
        "beak": ["short", "long", "curved", "straight"],
        "wings": ["broad", "narrow", "pointed"],
        "tail": ["long", "short", "forked"],
        "size": ["small", "medium", "large"],
        "legs": ["thin", "strong", "webbed"],
        "feet": ["sharp claws", "webbed toes", "perching toes"],
        "eyes": ["round", "oval", "sharp"],
        "expression": ["keen", "curious", "calm"],
        "distinctive marking": ["stripes", "spots", "colorful patterns"],
        "Fine-grained classes": ["Sparrow", "Eagle", "Parrot", "Owl", "Penguin", "Peacock"],
        "similar classes": {
            "kite": {
                "distinguished": ["feathers", "beak", "ability to fly independently"],
                "similar": ["ability to glide through air", "aerodynamic structure", "used in aerial environments"]
            },
            "frisbee": {
                "distinguished": ["living organism", "feathers", "beak"],
                "similar": ["flies through the air", "circular or wing-like structure", "used in flight"]
            },
            "umbrella": {
                "distinguished": ["feathers", "flying ability", "beak"],
                "similar": ["can be spread open like wings", "lightweight structure", "curved form"]
            }
        }
    },

    "bus": {
        "colors": ["black", "brown", "white", "mix"],
        "body shape": ["boxy", "flat front", "rounded front"],
        "axles": ["two", "three"],
        "windows": ["large", "rectangular"],
        "doors": ["single", "double", "front", "middle", "rear"],
        "wheels": ["large", "covered by fenders"],
        "headlights": ["large"],
        "grille": ["prominent"],
        "roof": ["flat", "curved", "luggage racks", "air conditioning units"],
        "interior layout": ["rows of seats", "handrails", "overhead compartments", "accessible seating"],
        "size": ["small", "large", "articulated"],
        "Fine-grained classes": ["City Bus", "School Bus", "Double-Decker", "Coach", "Minibus", "Articulated Bus"],

        "similar classes": {
            "truck": {
                "distinguished": ["passenger transport", "seating arrangement", "longer body"],
                "similar": ["large vehicle", "wheels", "road transport"]
            },
            "bench": {
                "distinguished": ["movement", "engine", "passenger capacity"],
                "similar": ["provides seating", "used in public spaces", "can accommodate many people"]
            },
            "stop sign": {
                "distinguished": ["movement", "large structure", "wheeled vehicle"],
                "similar": ["seen in public transportation settings", "road-associated",
                            "stationary object in transportation system"]
            }
        }
    },

    "cow": {
        "colors": ["black", "brown", "white", "mix"],
        "body": ["sturdy", "muscular", "lean", "stocky"],
        "hair": ["short"],
        "head": ["broad"],
        "nose": ["large", "moist"],
        "eyes": ["round", "oval"],
        "horns": ["curved", "straight", "absent"],
        "ears": ["medium-sized", "floppy", "semi-erect"],
        "tail": ["long", "tuft of hair at the end"],
        "udder": ["prominent"],
        "hooves": ["cloven"],
        "size": ["medium", "large"],
        "distinctive marking": ["spots", "patches", "stripes"],
        "Fine-grained classes": ["Holstein", "Jersey", "Hereford", "Angus", "Guernsey", "Ayrshire"],
        "similar classes": {
            "zebra": {
                "distinguished": ["solid coat color", "domesticated", "bulkier body"],
                "similar": ["four-legged", "grazing animal", "herbivorous"]
            },
            "giraffe": {
                "distinguished": ["long neck", "taller structure", "spotted coat"],
                "similar": ["large body size", "four legs", "herbivore"]
            },
            "bear": {
                "distinguished": ["different body structure", "carnivorous", "shorter fur"],
                "similar": ["large mammal", "fur-covered body", "used in land environments"]
            }
        }

    },

    "motorbike": {
        "colors": ["black", "brown", "white", "mix"],
        "body": ["sleek", "aerodynamic", "metal", "plastic"],
        "frame": ["narrow", "steel", "aluminum", "carbon fiber"],
        "seat": ["one rider", "two riders", "padded"],
        "handlebars": ["straight", "curved", "clip-on"],
        "wheels": ["spoked", "alloy"],
        "engine": ["visible", "beneath the fuel tank"],
        "fuel tank": ["rounded", "angular"],
        "headlights": ["round", "rectangular", "integrated"],
        "taillights": ["rear positioned"],
        "exhaust pipes": ["chromed", "matte-finished"],
        "design": ["sporty", "aggressive", "classic", "vintage"],
        "Fine-grained classes": ["Cruiser", "Sportbike", "Touring", "Standard", "Dual-sport", "Scooter"],
        "similar classes": {
            "skateboard": {
                "distinguished": ["engine", "seating", "handlebars"],
                "similar": ["requires balance", "two-wheeled design", "used for personal transport"]
            },
            "truck": {
                "distinguished": ["smaller size", "open design", "two wheels"],
                "similar": ["engine-powered", "used for transport", "road vehicle"]
            },
            "sports ball": {
                "distinguished": ["engine", "wheels", "seating"],
                "similar": ["round features", "movement involved", "used in active settings"]
            }
        }
    },
    "sofa": {
        "colors": ["black", "brown", "white", "mix"],
        "frame": ["wood", "metal", "combination"],
        "upholstery": ["fabric", "leather", "synthetic"],
        "texture": ["smooth", "textured"],
        "cushions": ["plush", "attached", "removable", "firm"],
        "arms": ["straight", "curved", "flared"],
        "backrest": ["low", "medium", "high"],
        "legs": ["short", "wood", "metal", "visible", "hidden"],
        "size": ["compact", "large", "sectional"],
        "features": ["recliners", "storage compartments", "convertible functions"],
        "Fine-grained classes": ["Loveseat", "Sectional", "Sleeper", "Chesterfield", "Recliner", "Modular"],
        "similar classes": {
            "bench": {
                "distinguished": ["padded cushions", "softer material", "used indoors"],
                "similar": ["long structure", "provides seating", "can accommodate multiple people"]
            },
            "bed": {
                "distinguished": ["upright seating", "backrest", "used for sitting not sleeping"],
                "similar": ["soft surface", "supports reclining", "used for comfort"]
            },
            "umbrella": {
                "distinguished": ["used for seating", "padded", "stationary"],
                "similar": ["wide structure", "used for protection or comfort", "can cover multiple people"]
            }
        }
    },

    'aeroplane': {
        "colors": ["white", "silver", "blue", "combination"],
        "body": ["streamlined", "cylindrical"], "wings": ["large", "medium"],
        "tail": ["vertical", "horizontal", "with stabilizers"],
        "engines": ["under the wings", "rear"],
        "landing gear": ["retractable", "fixed"],
        "cockpit windows": ["angular"],
        "markings": ["logos", "stripes", "national insignia"],
        "Fine-grained classes": ["Jet airliner", "Private jet", "Cargo plane", "Military fighter jet",
                                 "Propeller plane", "Glider", "Seaplane"],
        "similar classes": {
            "kite": {
                "distinguished": ["engine-powered", "metal structure", "passenger transport"],
                "similar": ["ability to fly", "aerodynamic design", "used for travel through air"]
            },
            "frisbee": {
                "distinguished": ["engine", "size", "mechanical complexity"],
                "similar": ["circular or flat design", "ability to glide", "used in the air"]
            },
            "surfboard": {
                "distinguished": ["wings", "engine", "flight capability"],
                "similar": ["streamlined design", "used in open environments",
                            "movement across surfaces (air for airplane, water for surfboard)"]
            }
        }
    },

    'bicycle': {
        "colors": ["red", "black", "blue", "white", "combination"],
        "frame": ["thin", "sturdy", "thick"],
        "wheels": ["medium", "rubber tires", "metal spokes"],
        "handlebars": ["flat", "curved"], "seat": ["padded", "firm"], "pedals": ["metal", "plastic"],
        "chain": ["visible", "covered"], "features": ["gears", "fenders", "baskets"],
        "Fine-grained classes": ["Mountain bike", "Road bike", "Hybrid bike", "BMX", "Electric bike"],
        "similar classes": {
            "skateboard": {
                "distinguished": ["handlebars", "pedals", "two wheels"],
                "similar": ["wheeled transport", "used for personal mobility", "requires balance"]
            },
            "surfboard": {
                "distinguished": ["wheels", "pedals", "land-based use"],
                "similar": ["long, narrow structure", "requires balance", "used for leisure"]
            },
            "kite": {
                "distinguished": ["wheels", "pedals", "ground transport"],
                "similar": ["lightweight structure", "aerodynamic shape", "often seen in recreational environments"]
            }
        }
    },

    'boat': {
        "colors": ["white", "blue", "black", "combination"],
        "hull": ["long", "narrow", "wide", "flat"],
        "power": ["motorized", "sail-powered"],
        "deck features": ["cabins", "masts", "navigation equipment"], "controls": ["rudder", "propeller"],
        "Fine-grained classes": ["Sailboat", "Motorboat", "Fishing boat", "Yacht", "Canoe", "Speedboat"],
        "similar classes": {
            "surfboard": {
                "distinguished": ["engine (in some boats)", "enclosed structure",
                                  "used on water for passengers or cargo"],
                "similar": ["floats on water", "long and flat shape", "used in water sports or travel"]
            },
            "bench": {
                "distinguished": ["ability to float", "propulsion system", "water-based"],
                "similar": ["long structure", "supports multiple people", "used in public settings"]
            },
            "kite": {
                "distinguished": ["floats on water", "solid structure", "carrying capacity"],
                "similar": ["lightweight", "glides through a medium", "used for recreational activities"]
            }
        }
    },

    'bottle': {
        "colors": ["transparent", "green", "brown", "blue"],
        "body": ["cylindrical", "square"],
        "neck": ["long", "short"],
        "materials": ["glass", "plastic"],
        "caps": ["screw-top", "corked", "flip-top"],
        "features": ["labels", "branding"],
        "Fine-grained classes": ["Water bottle", "Wine bottle", "Soda bottle", "Milk bottle", "Juice bottle"],
        "similar classes": {
            "wine glass": {
                "distinguished": ["narrow neck", "often has a cap", "used for storage of liquids"],
                "similar": ["cylindrical shape", "used to hold liquids", "transparent or translucent material"]
            },
            "cup": {
                "distinguished": ["taller structure", "narrow neck", "sealable"],
                "similar": ["used for drinking", "holds liquids", "portable"]
            },
            "vase": {
                "distinguished": ["often has a cap", "used for beverages", "smaller opening"],
                "similar": ["cylindrical shape", "holds contents", "glass or similar material"]
            }
        }
    },

    'car': {
        "colors": ["black", "white", "red", "blue", "combination"],
        "body": ["compact", "sleek", "large", "boxy"],
        "wheels": ["rubber tires", "metal rims"],
        "features": ["windows", "mirrors", "headlights", "tail lights", "air conditioning", "sound system",
                     "navigation"],
        "Fine-grained classes": ["Sedan", "SUV", "Hatchback", "Convertible", "Truck", "Electric car"],
        "similar classes": {
            "truck": {
                "distinguished": ["smaller size", "lower cargo capacity", "different load-bearing capacity"],
                "similar": ["wheels", "engine-powered", "road-based transport"]
            },
            "parking meter": {
                "distinguished": ["large moving body", "passenger capacity", "wheeled transport"],
                "similar": ["seen in urban environments", "associated with roads", "involved in vehicle parking"]
            },
            "bench": {
                "distinguished": ["engine", "movement capability", "wheeled structure"],
                "similar": ["provides seating", "used in public spaces", "stationary feature in urban environments"]
            }
        }
    },

    'cat': {
        "colors": ["black", "white", "orange", "grey", "combination"],
        "fur": ["short", "medium", "long"],
        "ears": ["pointed", "rounded"],
        "tail": ["long", "flexible"], "size": ["small", "medium"],
        "body": ["sleek", "muscular", "stocky"],
        "eyes": ["almond-shaped", "round", "green", "yellow", "blue"],
        "expression": ["curious", "alert", "calm"],
        "Fine-grained classes": ["Siamese", "Persian", "Maine Coon", "Bengal", "Sphynx"],
        "similar classes": {
            "bear": {
                "distinguished": ["smaller size", "more agile", "domestic nature"],
                "similar": ["four-legged", "mammal", "furry body"]
            },
            "backpack": {
                "distinguished": ["living organism", "limbs", "mobility on its own"],
                "similar": ["compact shape", "used in daily activities", "carried or moved easily"]
            },
            "handbag": {
                "distinguished": ["limbs", "living organism", "mobility"],
                "similar": ["small and portable", "compact structure", "often found in domestic environments"]
            }
        }
    },

    'chair': {
        "colors": ["black", "white", "brown", "combination"],
        "frame": ["wood", "metal", "plastic"],
        "seat": ["padded", "hard"], "back": ["high", "medium", "low"],
        "armrests": ["present", "absent"],
        "legs": ["short", "long", "straight", "curved"],
        "design": ["modern", "traditional", "minimalist"],
        "features": ["upholstery", "cushions", "decorative details"],
        "Fine-grained classes": ["Armchair", "Recliner", "Office chair", "Dining chair", "Folding chair"],
        "similar classes": {
            "bench": {
                "distinguished": ["smaller size", "designed for individual use", "has a backrest"],
                "similar": ["used for sitting", "provides seating support", "common in public places"]
            },
            "bed": {
                "distinguished": ["upright seating", "smaller size", "not designed for sleeping"],
                "similar": ["provides support", "used for resting", "has a surface to rest on"]
            },
            "suitcase": {
                "distinguished": ["no mobility features", "no storage capacity", "doesn’t move"],
                "similar": ["rectangular form", "often has a rigid frame", "used in everyday life"]
            }
        }
    },

    'diningtable': {
        "colors": ["brown", "black", "white", "combination"],
        "top": ["wood", "glass", "metal"],
        "legs": ["short", "medium", "tall"],
        "shape": ["rectangular", "square", "round"], "features": ["extendable leaves", "decorative legs"],
        "design": ["traditional", "modern", "minimalist"],
        "surface": ["polished", "matte"],
        "Fine-grained classes": ["Round table", "Square table", "Extendable table", "Glass top table"],
        "similar classes": {
            "bench": {
                "distinguished": ["used for dining", "usually larger", "has a flat top for placing items"],
                "similar": ["used in public spaces", "provides support", "accommodates multiple people"]
            },
            "bed": {
                "distinguished": ["upright structure", "used for eating", "does not support lying down"],
                "similar": ["large surface", "provides support", "used in a room for activities"]
            },
            "suitcase": {
                "distinguished": ["fixed structure", "not portable", "used for dining"],
                "similar": ["rectangular form", "supports daily activities", "used in everyday environments"]
            }
        }
    },

    'dog': {
        "colors": ["black", "brown", "white", "mix"],
        "fur": ["short", "medium", "long"],
        "ears": ["floppy", "semi-floppy", "erect"],
        "tail": ["bushy", "curled", "straight"],
        "size": ["small", "medium", "large"],
        "body": ["muscular", "lean", "stout"],
        "face": ["short snout", "long snout"],
        "eyes": ["round", "almond-shaped", "oval"],
        "expression": ["alert", "gentle", "playful"],
        "distinctive marking": ["spots", "patches", "brindle patterns"],
        "Fine-grained classes": ["Labrador Retriever", "Bulldog", "Poodle", "German Shepherd", "Golden Retriever"],
        "similar classes": {
            "bear": {
                "distinguished": ["smaller size", "domestic behavior", "more agile"],
                "similar": ["four-legged mammal", "furry", "sharp senses"]
            },
            "teddy bear": {
                "distinguished": ["living organism", "mobility", "real fur"],
                "similar": ["fluffy appearance", "used for comfort", "compact body structure"]
            },
            "backpack": {
                "distinguished": ["living organism", "mobility", "limbs"],
                "similar": ["compact shape", "can be carried or held", "useful for daily life"]
            }
        }
    },

    'horse': {
        "colors": ["brown", "black", "white", "combination"],
        "coat": ["short", "sleek"],
        "mane and tail": ["long", "wavy"],
        "body": ["large", "muscular"],
        "legs": ["long"],
        "ears": ["medium", "pointed"],
        "face": ["long", "prominent snout"],
        "eyes": ["large", "expressive"],
        "posture": ["strong", "graceful"],
        "Fine-grained classes": ["Thoroughbred", "Arabian", "Quarter Horse", "Mustang", "Clydesdale"],
        "similar classes": {
            "zebra": {
                "distinguished": ["different coat patterns", "wild nature", "striped appearance"],
                "similar": ["four legs", "herbivorous diet", "similar body size and shape"]
            },
            "giraffe": {
                "distinguished": ["long neck", "taller body", "spotted coat"],
                "similar": ["large size", "four legs", "used for land travel"]
            },
            "bear": {
                "distinguished": ["larger bulk", "different habitat", "carnivorous"],
                "similar": ["four-legged structure", "mammalian", "fur-covered body"]
            }
        }
    },

    'person': {
        "colors": ["varied skin tones"],
        "height": ["small", "medium", "tall"],
        "body size": ["slender", "muscular", "stocky"],
        "hair": ["short", "medium", "long", "varied textures"],
        "eyes": ["round", "almond-shaped", "hooded", "brown", "blue", "green", "hazel"],
        "facial features": ["nose", "mouth", "jawlines"],
        "clothing": ["diverse"],
        "expression": ["varied"],
        "Fine-grained classes": ["Men", "Women", "Children", "Athletes", "Professionals"],
        "similar classes": {
            "suitcase": {
                "distinguished": ["limbs", "head", "mobility on its own"],
                "similar": ["upright structure", "portable", "used for travel"]
            },
            "backpack": {
                "distinguished": ["limbs", "head", "speech ability"],
                "similar": ["portable", "carry-on item", "supports daily tasks"]
            },
            "tie": {
                "distinguished": ["entire body structure", "limbs", "ability to move"],
                "similar": ["used with clothing", "fashionable", "found in professional settings"]
            }
        }
    },

    'pottedplant': {
        "colors": ["green leaves", "brown stems", "colorful flowers"],
        "leaves": ["broad", "thin", "spiky", "succulent"],
        "pot": ["plastic", "ceramic", "clay"],
        "height": ["small", "medium"],
        "features": ["decorative stones", "moss"],
        "Fine-grained classes": ["Succulent", "Fern", "Flowering plant", "Cactus", "Palm"],
        "similar classes": {
            "vase": {
                "distinguished": ["contains soil", "supports living plants", "heavier with soil and water"],
                "similar": ["holds contents", "cylindrical shape", "used for decoration"]
            },
            "bowl": {
                "distinguished": ["contains soil and plants", "used for holding life", "heavier"],
                "similar": ["round shape", "holds items", "used for decorative purposes"]
            },
            "sink": {
                "distinguished": ["contains plants", "doesn't drain water", "used for decoration"],
                "similar": ["holds contents", "can contain water", "has a basin shape"]
            }
        }
    },

    'sheep': {"colors": ["white", "black", "brown", "combination"],
              "wool": ["thick", "curly", "fluffy"], "ears": ["medium", "floppy"],
              "tail": ["short"],
              "body": ["stocky", "robust"],
              "hooves": ["adapted for varied terrain"],
              "face": ["long snout", "short snout"],
              "eyes": ["round", "oval", "calm", "gentle"],
              "Fine-grained classes": ["Merino", "Suffolk", "Dorset", "Katahdin", "Hampshire"],
              "similar classes": {
                  "zebra": {
                      "distinguished": ["wooly coat", "smaller size", "domestic"],
                      "similar": ["four legs", "herbivorous", "grazing behavior"]
                  },
                  "giraffe": {
                      "distinguished": ["long neck", "taller body", "spotted coat"],
                      "similar": ["quadruped", "herbivore", "grazing behavior"]
                  },
                  "bench": {
                      "distinguished": ["non-living object", "stationary", "no limbs"],
                      "similar": ["supports weight", "used in public spaces", "relatively stationary"]
                  }
              }
              },

    "train": {"colors": ["black", "brown", "white", "mix"],
              "exterior": ["sleek", "boxy", "smooth", "ribbed"],
              "train cars": ["connected series"],
              "windows": ["large", "rectangular", "rounded"],
              "wheels": ["sturdy", "metallic"],
              "front": ["streamlined", "rounded", "angular"],
              "features": ["pantographs", "electrical components", "diesel exhausts"],
              "interior": ["seating", "luggage compartments", "dining areas", "sleeping areas"],
              "Fine-grained classes": ["Freight Train", "Passenger Train", "High-Speed Train", "Subway Train",
                                       "Monorail", "Diesel Locomotive", "Electric Locomotive", "Bullet Train"],
              "similar classes": {
                  "truck": {
                      "distinguished": ["tracks", "longer body", "lack of wheels for roads"],
                      "similar": ["large structure", "used for cargo and passenger transport", "mechanized engine"]
                  },
                  "bench": {
                      "distinguished": ["engine", "wheels", "motion capability"],
                      "similar": ["long structure", "accommodates passengers", "used in public places"]
                  },
                  "surfboard": {
                      "distinguished": ["engine", "metal body", "ground-based"],
                      "similar": ["elongated design", "travels long distances", "streamlined form"]
                  }
              }
              },

    "tvmonitor": {
        "colors": ["black", "brown", "white", "mix"],
        "screen": ["flat", "rectangular"],
        "bezels": ["slim", "thicker"],
        "size": ["small", "medium", "large"],
        "finish": ["glossy", "matte"],
        "back panel": ["vents", "ports"],
        "stand": ["minimalistic", "wide", "adjustable"],
        "mounting options": ["wall mounting"],
        "display technology": ["LED", "LCD", "OLED"],
        "surface": ["glare-resistant", "anti-reflective"],
        "features": ["built-in speakers", "adjustable controls"],
        "Fine-grained classes": ["CRT TV", "LED Monitor", "LCD TV", "Plasma Screen", "OLED Display", "Smart TV",
                                 "Gaming Monitor"],
        "similar classes": {
            "laptop": {
                "distinguished": ["larger screen", "fixed position", "used mainly for watching"],
                "similar": ["screen display", "used for media viewing", "rectangular shape"]
            },
            "clock": {
                "distinguished": ["displays time", "smaller size", "used for tracking time"],
                "similar": ["flat surface", "used in homes", "rectangular or square shape"]
            },
            "microwave": {
                "distinguished": ["used for cooking", "enclosed structure", "heats food"],
                "similar": ["rectangular shape", "found in homes", "electronic device"]
            }
        }
    },
}

meta_COCO_info_T2 = {
    "truck": {
        "colors": ["black", "white", "red", "blue", "gray", "mix"],
        "body shape": ["boxy", "flat front", "aerodynamic"],
        "cab": ["single", "extended", "crew"],
        "bed": ["short", "long", "flatbed", "enclosed"],
        "axles": ["two", "three", "multiple"],
        "windows": ["large", "tinted", "rectangular"],
        "doors": ["two", "four"],
        "wheels": ["large", "heavy-duty", "dual rear wheels"],
        "headlights": ["large", "LED", "halogen"],
        "grille": ["prominent", "chrome", "painted"],
        "roof": ["flat", "sleeper cab", "wind deflector"],
        "features": ["towing hitch", "running boards", "toolbox", "ladder rack"],
        "size": ["pickup", "medium-duty", "heavy-duty", "semi-truck"],
        "Fine-grained classes": ["Pickup Truck", "Dump Truck", "Box Truck", "Semi-Truck", "Tow Truck", "Flatbed Truck"],
        "similar classes": {
            "bus": {
                "distinguished": ["cargo transport", "open bed", "different body structure"],
                "similar": ["large vehicle", "wheels", "road transport"]
            },
            "car": {
                "distinguished": ["larger size", "cargo capacity", "higher ground clearance"],
                "similar": ["wheeled vehicle", "engine-powered", "used for transportation"]
            },
            "train": {
                "distinguished": ["wheels for roads", "smaller size", "independent travel"],
                "similar": ["used for cargo transport", "long body", "heavy-duty construction"]
            }
        }
    },

    "traffic light": {
        "colors": ["red", "yellow", "green", "black housing"],
        "shape": ["vertical", "horizontal"],
        "lights": ["three lights", "red on top", "yellow middle", "green bottom"],
        "housing": ["rectangular", "cylindrical"],
        "mounting": ["pole-mounted", "suspended by wires", "wall-mounted"],
        "features": ["sun shade", "backboard", "countdown timer", "arrow signals"],
        "size": ["standard", "large", "pedestrian-sized"],
        "visibility": ["bright", "LED", "incandescent"],
        "expression": ["authoritative", "guiding", "regulatory"],
        "Fine-grained classes": ["Pedestrian Signal", "Vehicle Signal", "Arrow Signal", "Countdown Signal", "Bicycle Signal"],
        "similar classes": {
            "stop sign": {
                "distinguished": ["multiple colored lights", "taller structure", "changes state"],
                "similar": ["traffic control", "mounted on pole", "road safety device"]
            },
            "parking meter": {
                "distinguished": ["lights", "traffic control function", "mounted higher"],
                "similar": ["pole-mounted", "metal structure", "found on streets"]
            },
            "clock": {
                "distinguished": ["colored lights", "traffic control", "larger size"],
                "similar": ["displays information", "circular elements", "time-related function (traffic timing)"]
            }
        }
    },

    "fire hydrant": {
        "colors": ["red", "yellow", "white", "orange", "silver"],
        "body": ["cylindrical", "metal", "sturdy"],
        "height": ["short", "medium"],
        "outlets": ["two nozzles", "three nozzles", "four nozzles"],
        "cap": ["flat top", "rounded top", "chain attached"],
        "valve": ["top valve", "side outlets"],
        "mounting": ["ground-mounted", "sidewalk"],
        "chain": ["attached chain", "loose chain"],
        "features": ["reflective bands", "numbering", "paint markings"],
        "condition": ["new", "weathered", "rusty"],
        "expression": ["sturdy", "reliable", "emergency-ready"],
        "Fine-grained classes": ["Wet Barrel", "Dry Barrel", "Flush Hydrant", "Pillar Hydrant"],
        "similar classes": {
            "parking meter": {
                "distinguished": ["wider body", "water outlet", "emergency use"],
                "similar": ["pole-like structure", "metal construction", "found on sidewalks"]
            },
            "stop sign": {
                "distinguished": ["cylindrical shape", "ground-mounted", "water function"],
                "similar": ["street furniture", "painted bright colors", "safety-related"]
            },
            "bench": {
                "distinguished": ["metal construction", "vertical structure", "functional purpose"],
                "similar": ["found in public spaces", "ground-mounted", "sturdy construction"]
            }
        }
    },

    "stop sign": {
        "colors": ["red", "white text"],
        "shape": ["octagonal"],
        "text": ["STOP"],
        "mounting": ["pole-mounted", "high-mounted", "low-mounted"],
        "pole": ["metal", "wooden", "single pole", "double pole"],
        "size": ["standard", "large", "small"],
        "reflectivity": ["reflective", "non-reflective"],
        "condition": ["new", "faded", "weathered", "graffiti"],
        "features": ["white border", "bold letters"],
        "expression": ["authoritative", "warning", "regulatory"],
        "Fine-grained classes": ["Standard Stop Sign", "All-Way Stop", "Multi-Way Stop", "School Zone Stop"],
        "similar classes": {
            "traffic light": {
                "distinguished": ["octagonal shape", "single message", "static display"],
                "similar": ["traffic control", "pole-mounted", "road safety device"]
            },
            "parking meter": {
                "distinguished": ["flat sign", "octagonal", "different function"],
                "similar": ["pole-mounted", "metal structure", "found on streets"]
            },
            "frisbee": {
                "distinguished": ["stationary", "pole-mounted", "regulatory function"],
                "similar": ["circular/octagonal shape", "flat surface", "visible from distance"]
            }
        }
    },

    "parking meter": {
        "colors": ["gray", "black", "green", "silver"],
        "body": ["rectangular", "cylindrical"],
        "pole": ["metal", "tall", "short"],
        "display": ["digital", "mechanical"],
        "payment": ["coin slot", "card reader", "digital payment"],
        "buttons": ["multiple buttons", "touchscreen"],
        "mounting": ["sidewalk", "curb-mounted"],
        "size": ["compact", "standard", "tall"],
        "features": ["solar panel", "receipt printer", "timer display"],
        "condition": ["new", "weathered", "damaged"],
        "expression": ["functional", "modern", "utilitarian"],
        "Fine-grained classes": ["Single Space Meter", "Multi-Space Meter", "Smart Meter", "Solar Meter"],
        "similar classes": {
            "fire hydrant": {
                "distinguished": ["payment function", "display screen", "taller structure"],
                "similar": ["pole-like structure", "metal construction", "found on sidewalks"]
            },
            "traffic light": {
                "distinguished": ["payment function", "smaller size", "parking-specific"],
                "similar": ["pole-mounted", "metal structure", "regulatory device"]
            },
            "stop sign": {
                "distinguished": ["vertical structure", "payment function", "digital display"],
                "similar": ["pole-mounted", "street furniture", "regulatory purpose"]
            }
        }
    },

    "bench": {
        "colors": ["brown", "black", "green", "white", "gray"],
        "frame": ["wood", "metal", "plastic", "concrete"],
        "seat": ["slatted", "solid", "contoured"],
        "backrest": ["present", "absent", "low", "high"],
        "armrests": ["present", "absent", "center divider"],
        "legs": ["metal", "wood", "concrete base"],
        "mounting": ["ground-mounted", "freestanding", "wall-mounted"],
        "size": ["two-seater", "three-seater", "long"],
        "features": ["memorial plaque", "decorative ironwork", "cushions"],
        "condition": ["new", "weathered", "painted", "rusty"],
        "expression": ["welcoming", "sturdy", "restful"],
        "Fine-grained classes": ["Park Bench", "Garden Bench", "Memorial Bench", "Transit Bench", "Picnic Bench"],
        "similar classes": {
            "chair": {
                "distinguished": ["longer structure", "accommodates multiple people", "outdoor use"],
                "similar": ["provides seating", "has backrest", "used for resting"]
            },
            "sofa": {
                "distinguished": ["outdoor use", "harder surface", "public setting"],
                "similar": ["long seating", "accommodates multiple people", "backrest present"]
            },
            "diningtable": {
                "distinguished": ["used for sitting", "has backrest", "not a flat top"],
                "similar": ["found in public spaces", "accommodates multiple people", "sturdy structure"]
            }
        }
    },

    "elephant": {
        "colors": ["gray", "dark gray", "brownish gray"],
        "body": ["large", "massive", "wrinkled skin"],
        "trunk": ["long", "flexible", "muscular"],
        "ears": ["very large", "fan-shaped", "flapping"],
        "tusks": ["long", "curved", "ivory", "absent in some"],
        "legs": ["thick", "columnar", "powerful"],
        "feet": ["padded", "large", "circular"],
        "tail": ["long", "thin", "tuft of hair at end"],
        "eyes": ["small", "expressive"],
        "size": ["very large", "massive"],
        "skin texture": ["wrinkled", "thick", "rough"],
        "expression": ["gentle", "intelligent", "powerful"],
        "Fine-grained classes": ["African Elephant", "Asian Elephant", "Forest Elephant", "Savanna Elephant"],
        "similar classes": {
            "bear": {
                "distinguished": ["trunk", "tusks", "much larger size"],
                "similar": ["large mammal", "four legs", "powerful build"]
            },
            "cow": {
                "distinguished": ["trunk", "tusks", "much larger size"],
                "similar": ["large herbivore", "four legs", "domesticated or wild"]
            },
            "giraffe": {
                "distinguished": ["shorter neck", "trunk present", "different body proportions"],
                "similar": ["large African animal", "herbivore", "impressive size"]
            }
        }
    },

    "bear": {
        "colors": ["black", "brown", "white", "grizzled"],
        "body": ["large", "stocky", "muscular", "powerful"],
        "fur": ["thick", "shaggy", "dense"],
        "head": ["large", "rounded"],
        "snout": ["short", "prominent"],
        "ears": ["small", "rounded", "furry"],
        "legs": ["strong", "thick"],
        "paws": ["large", "clawed"],
        "claws": ["long", "curved", "sharp"],
        "tail": ["short", "stubby"],
        "size": ["medium", "large", "very large"],
        "posture": ["all fours", "standing upright"],
        "expression": ["powerful", "wild", "fierce", "curious"],
        "Fine-grained classes": ["Grizzly Bear", "Black Bear", "Polar Bear", "Brown Bear", "Panda Bear"],
        "similar classes": {
            "dog": {
                "distinguished": ["larger size", "different body structure", "wild nature"],
                "similar": ["four-legged", "furry", "mammal"]
            },
            "cow": {
                "distinguished": ["carnivorous", "claws", "wild behavior"],
                "similar": ["large mammal", "four legs", "fur-covered"]
            },
            "elephant": {
                "distinguished": ["smaller size", "no trunk", "different body shape"],
                "similar": ["large mammal", "powerful build", "wild animal"]
            }
        }
    },

    "zebra": {
        "colors": ["black and white stripes"],
        "body": ["muscular", "horse-like"],
        "stripes": ["vertical", "unique pattern", "covering entire body"],
        "mane": ["short", "upright", "striped"],
        "tail": ["long", "tufted end", "striped"],
        "legs": ["long", "slender", "striped"],
        "hooves": ["black", "solid"],
        "head": ["long", "horse-like"],
        "ears": ["medium", "upright", "rounded"],
        "eyes": ["dark", "expressive"],
        "size": ["medium", "large"],
        "expression": ["alert", "wild", "graceful"],
        "Fine-grained classes": ["Plains Zebra", "Mountain Zebra", "Grevy's Zebra"],
        "similar classes": {
            "horse": {
                "distinguished": ["striped pattern", "wild nature", "different coloring"],
                "similar": ["four legs", "hooves", "similar body shape"]
            },
            "cow": {
                "distinguished": ["striped pattern", "wild behavior", "slender build"],
                "similar": ["herbivore", "four legs", "grazing animal"]
            },
            "giraffe": {
                "distinguished": ["shorter neck", "striped pattern", "different proportions"],
                "similar": ["African animal", "herbivore", "distinctive markings"]
            }
        }
    },

    "giraffe": {
        "colors": ["tan", "brown", "white", "spotted pattern"],
        "body": ["tall", "long-legged"],
        "neck": ["very long", "flexible"],
        "spots": ["irregular patches", "brown on tan"],
        "legs": ["very long", "slender"],
        "hooves": ["split", "large"],
        "tail": ["long", "tufted end"],
        "head": ["small", "elongated"],
        "ossicones": ["horn-like protrusions", "fur-covered"],
        "ears": ["large", "pointed"],
        "eyes": ["large", "dark", "prominent lashes"],
        "tongue": ["long", "dark", "prehensile"],
        "size": ["very tall", "largest land animal by height"],
        "expression": ["gentle", "graceful", "curious"],
        "Fine-grained classes": ["Masai Giraffe", "Reticulated Giraffe", "Northern Giraffe", "Southern Giraffe"],
        "similar classes": {
            "horse": {
                "distinguished": ["much taller", "long neck", "spotted pattern"],
                "similar": ["four legs", "hooves", "herbivore"]
            },
            "zebra": {
                "distinguished": ["long neck", "spotted not striped", "much taller"],
                "similar": ["African animal", "herbivore", "long legs"]
            },
            "cow": {
                "distinguished": ["long neck", "much taller", "different body proportions"],
                "similar": ["herbivore", "four legs", "hooves"]
            }
        }
    },

    "backpack": {
        "colors": ["black", "blue", "red", "gray", "green", "mix"],
        "material": ["canvas", "nylon", "leather", "polyester"],
        "size": ["small", "medium", "large", "oversized"],
        "compartments": ["single", "multiple", "laptop sleeve"],
        "straps": ["padded", "adjustable", "two shoulder straps"],
        "zippers": ["one", "multiple", "front pocket"],
        "features": ["water bottle holder", "chest strap", "hip belt", "reflective strips"],
        "shape": ["rectangular", "rounded", "top-loading"],
        "style": ["school", "hiking", "tactical", "fashion"],
        "condition": ["new", "worn", "packed full", "empty"],
        "expression": ["practical", "functional", "portable"],
        "Fine-grained classes": ["School Backpack", "Hiking Backpack", "Laptop Backpack", "Military Backpack", "Daypack"],
        "similar classes": {
            "handbag": {
                "distinguished": ["shoulder straps", "worn on back", "larger capacity"],
                "similar": ["used for carrying items", "portable", "has compartments"]
            },
            "suitcase": {
                "distinguished": ["worn on back", "softer material", "smaller size"],
                "similar": ["used for carrying belongings", "has compartments", "portable"]
            },
            "person": {
                "distinguished": ["inanimate object", "no limbs", "carried by person"],
                "similar": ["seen with people", "portable item", "everyday object"]
            }
        }
    },

    "umbrella": {
        "colors": ["black", "red", "blue", "rainbow", "transparent"],
        "canopy": ["dome-shaped", "circular", "octagonal"],
        "material": ["nylon", "polyester", "transparent plastic"],
        "ribs": ["metal", "fiberglass", "multiple"],
        "shaft": ["straight", "telescoping", "J-shaped"],
        "handle": ["curved", "straight", "ergonomic", "wooden", "plastic"],
        "size": ["compact", "standard", "golf umbrella"],
        "features": ["automatic open", "wind-resistant", "inverted design"],
        "state": ["open", "closed", "folded"],
        "condition": ["new", "weathered", "broken"],
        "expression": ["protective", "portable", "practical"],
        "Fine-grained classes": ["Compact Umbrella", "Golf Umbrella", "Beach Umbrella", "Patio Umbrella", "Automatic Umbrella"],
        "similar classes": {
            "kite": {
                "distinguished": ["held by hand", "rain protection", "collapsible"],
                "similar": ["lightweight", "fabric canopy", "used outdoors"]
            },
            "frisbee": {
                "distinguished": ["has handle", "protective function", "larger size"],
                "similar": ["circular shape", "lightweight", "outdoor use"]
            },
            "bird": {
                "distinguished": ["inanimate object", "man-made", "no movement"],
                "similar": ["opens like wings", "lightweight", "used in outdoor settings"]
            }
        }
    },

    "handbag": {
        "colors": ["black", "brown", "red", "white", "mix"],
        "material": ["leather", "synthetic", "canvas", "suede"],
        "size": ["small", "medium", "large"],
        "handles": ["short", "long", "double handles", "single strap"],
        "closure": ["zipper", "magnetic snap", "clasp", "open top"],
        "compartments": ["single", "multiple", "interior pockets"],
        "shape": ["rectangular", "hobo", "tote", "clutch", "satchel"],
        "features": ["metal hardware", "decorative elements", "brand logo", "adjustable strap"],
        "style": ["casual", "formal", "designer", "vintage"],
        "condition": ["new", "worn", "luxury"],
        "expression": ["fashionable", "elegant", "practical"],
        "Fine-grained classes": ["Tote Bag", "Shoulder Bag", "Clutch", "Crossbody Bag", "Hobo Bag", "Satchel"],
        "similar classes": {
            "backpack": {
                "distinguished": ["hand-carried or shoulder", "smaller capacity", "fashion-oriented"],
                "similar": ["used for carrying items", "has compartments", "portable"]
            },
            "suitcase": {
                "distinguished": ["smaller size", "carried by hand", "daily use"],
                "similar": ["used for carrying belongings", "has handles", "portable"]
            },
            "cat": {
                "distinguished": ["inanimate object", "no mobility", "carried item"],
                "similar": ["small and compact", "found in daily settings", "portable"]
            }
        }
    },

    "tie": {
        "colors": ["black", "blue", "red", "striped", "patterned"],
        "material": ["silk", "polyester", "cotton", "wool"],
        "width": ["slim", "standard", "wide"],
        "length": ["short", "standard", "long"],
        "pattern": ["solid", "striped", "dotted", "paisley", "checkered"],
        "knot": ["four-in-hand", "windsor", "half-windsor"],
        "style": ["traditional", "modern", "bow tie", "skinny tie"],
        "features": ["clip", "tie bar", "textured"],
        "condition": ["neatly tied", "loosened", "hanging"],
        "expression": ["formal", "professional", "elegant"],
        "Fine-grained classes": ["Necktie", "Bow Tie", "Ascot", "Bolo Tie", "Skinny Tie"],
        "similar classes": {
            "person": {
                "distinguished": ["clothing accessory", "worn around neck", "fabric"],
                "similar": ["associated with people", "worn item", "professional setting"]
            },
            "belt": {
                "distinguished": ["worn around neck", "narrower", "decorative"],
                "similar": ["fabric accessory", "worn item", "adjustable length"]
            },
            "ribbon": {
                "distinguished": ["specific knot", "professional use", "worn on person"],
                "similar": ["fabric strip", "decorative", "tied in knot"]
            }
        }
    },

    "suitcase": {
        "colors": ["black", "gray", "blue", "red", "brown"],
        "material": ["hard plastic", "soft fabric", "leather", "polycarbonate"],
        "size": ["carry-on", "medium", "large", "oversized"],
        "wheels": ["two wheels", "four spinner wheels"],
        "handle": ["telescoping", "retractable", "top handle", "side handle"],
        "compartments": ["single", "divided", "zippered pockets"],
        "closure": ["zipper", "latches", "combination lock", "TSA lock"],
        "features": ["expandable", "lightweight", "hard shell", "soft shell"],
        "condition": ["new", "travel-worn", "scratched", "packed"],
        "expression": ["practical", "sturdy", "travel-ready"],
        "Fine-grained classes": ["Carry-on Luggage", "Checked Luggage", "Rolling Suitcase", "Hard Shell Case", "Duffel Bag"],
        "similar classes": {
            "backpack": {
                "distinguished": ["wheeled", "larger capacity", "rigid structure"],
                "similar": ["used for carrying belongings", "portable", "has compartments"]
            },
            "handbag": {
                "distinguished": ["larger size", "wheels present", "travel-specific"],
                "similar": ["used for carrying items", "has handles", "portable"]
            },
            "chair": {
                "distinguished": ["storage function", "portable", "wheeled"],
                "similar": ["rectangular form", "rigid structure", "found in daily settings"]
            }
        }
    },

    "microwave": {
        "colors": ["white", "black", "stainless steel", "gray"],
        "body": ["rectangular", "boxy"],
        "door": ["glass window", "hinged", "drop-down"],
        "control panel": ["buttons", "digital display", "dial knobs"],
        "size": ["compact", "standard", "large"],
        "interior": ["turntable", "metal interior", "light"],
        "features": ["ventilation grilles", "handle", "timer display"],
        "mounting": ["countertop", "built-in", "over-range"],
        "finish": ["glossy", "matte", "fingerprint-resistant"],
        "power": ["600-1200 watts"],
        "expression": ["modern", "functional", "utilitarian"],
        "Fine-grained classes": ["Countertop Microwave", "Over-the-Range Microwave", "Built-in Microwave", "Convection Microwave"],
        "similar classes": {
            "oven": {
                "distinguished": ["smaller size", "countertop placement", "microwave technology"],
                "similar": ["cooking appliance", "rectangular shape", "door with window"]
            },
            "tvmonitor": {
                "distinguished": ["cooking function", "control panel", "different purpose"],
                "similar": ["rectangular shape", "display screen", "electronic device"]
            },
            "refrigerator": {
                "distinguished": ["smaller size", "heating function", "different purpose"],
                "similar": ["kitchen appliance", "door with handle", "rectangular shape"]
            }
        }
    },

    "oven": {
        "colors": ["white", "black", "stainless steel", "gray"],
        "body": ["large", "rectangular", "built-in"],
        "door": ["glass window", "hinged", "drop-down"],
        "racks": ["multiple levels", "adjustable", "wire racks"],
        "control panel": ["knobs", "digital display", "buttons"],
        "burners": ["gas", "electric", "induction"],
        "size": ["compact", "standard", "double oven"],
        "features": ["self-cleaning", "convection fan", "temperature display", "oven light"],
        "placement": ["standalone", "built-in", "under counter"],
        "finish": ["glossy", "matte", "stainless"],
        "expression": ["professional", "functional", "kitchen-essential"],
        "Fine-grained classes": ["Gas Oven", "Electric Oven", "Convection Oven", "Double Oven", "Wall Oven"],
        "similar classes": {
            "microwave": {
                "distinguished": ["larger size", "conventional heating", "multiple racks"],
                "similar": ["cooking appliance", "door with window", "kitchen device"]
            },
            "refrigerator": {
                "distinguished": ["heating function", "higher temperature", "different purpose"],
                "similar": ["large kitchen appliance", "door with handle", "rectangular shape"]
            },
            "dishwasher": {
                "distinguished": ["cooking function", "different interior", "higher temperature"],
                "similar": ["kitchen appliance", "door with control panel", "built-in option"]
            }
        }
    },

    "toaster": {
        "colors": ["silver", "black", "white", "red", "chrome"],
        "body": ["rectangular", "compact", "metal"],
        "slots": ["two slots", "four slots", "long slot"],
        "size": ["small", "compact"],
        "features": ["crumb tray", "browning control", "cancel button", "defrost function"],
        "finish": ["chrome", "brushed metal", "plastic", "glossy"],
        "lever": ["push-down", "spring-loaded"],
        "design": ["modern", "retro", "minimalist"],
        "condition": ["new", "used", "clean"],
        "expression": ["compact", "efficient", "practical"],
        "Fine-grained classes": ["Pop-up Toaster", "Toaster Oven", "Long Slot Toaster", "Four Slice Toaster"],
        "similar classes": {
            "microwave": {
                "distinguished": ["smaller size", "slots for bread", "specific toasting function"],
                "similar": ["kitchen appliance", "heating function", "countertop placement"]
            },
            "blender": {
                "distinguished": ["vertical slots", "heating element", "different function"],
                "similar": ["small kitchen appliance", "countertop device", "electric-powered"]
            },
            "clock": {
                "distinguished": ["heating function", "slots", "kitchen appliance"],
                "similar": ["rectangular shape", "small size", "displays information (browning level)"]
            }
        }
    },

    "sink": {
        "colors": ["white", "stainless steel", "black", "gray"],
        "material": ["porcelain", "stainless steel", "granite composite", "cast iron"],
        "bowl": ["single bowl", "double bowl", "deep", "shallow"],
        "shape": ["rectangular", "oval", "square", "farmhouse"],
        "faucet": ["single handle", "double handle", "pull-down sprayer"],
        "mounting": ["top-mount", "undermount", "vessel"],
        "size": ["small", "standard", "large", "extra-large"],
        "features": ["drainboard", "soap dispenser", "garbage disposal", "drain"],
        "finish": ["polished", "brushed", "matte"],
        "condition": ["clean", "used", "stained"],
        "expression": ["functional", "clean", "practical"],
        "Fine-grained classes": ["Kitchen Sink", "Bathroom Sink", "Utility Sink", "Farmhouse Sink", "Vessel Sink"],
        "similar classes": {
            "toilet": {
                "distinguished": ["washing function", "faucet present", "different placement"],
                "similar": ["porcelain fixture", "plumbing fixture", "water-based"]
            },
            "bowl": {
                "distinguished": ["built-in fixture", "faucet", "drain present"],
                "similar": ["holds water", "basin shape", "used for washing"]
            },
            "pottedplant": {
                "distinguished": ["plumbing fixture", "washing function", "faucet"],
                "similar": ["basin shape", "holds water", "found in homes"]
            }
        }
    },

    "refrigerator": {
        "colors": ["white", "black", "stainless steel", "gray", "custom panels"],
        "body": ["tall", "rectangular", "boxy"],
        "doors": ["single door", "double door", "french door"],
        "handles": ["bar handles", "recessed handles", "no handles"],
        "freezer": ["top-mount", "bottom-mount", "side-by-side"],
        "size": ["compact", "standard", "large", "commercial"],
        "features": ["ice maker", "water dispenser", "digital display", "temperature control"],
        "finish": ["glossy", "matte", "fingerprint-resistant", "stainless"],
        "shelves": ["adjustable", "glass", "wire"],
        "drawers": ["crisper drawers", "deli drawer", "freezer drawer"],
        "expression": ["modern", "spacious", "essential"],
        "Fine-grained classes": ["Top-Freezer", "Bottom-Freezer", "Side-by-Side", "French Door", "Mini Fridge"],
        "similar classes": {
            "oven": {
                "distinguished": ["cooling function", "larger size", "vertical orientation"],
                "similar": ["large kitchen appliance", "door with handle", "rectangular shape"]
            },
            "microwave": {
                "distinguished": ["much larger", "cooling function", "different purpose"],
                "similar": ["kitchen appliance", "rectangular shape", "door with handle"]
            },
            "cabinet": {
                "distinguished": ["cooling function", "electronic", "sealed compartment"],
                "similar": ["storage furniture", "doors", "tall structure"]
            }
        }
    }
}

meta_COCO_info_T3 = {
    "frisbee": {
        "colors": ["white", "red", "blue", "yellow", "orange", "neon"],
        "shape": ["disc", "circular", "flat"],
        "material": ["plastic", "rubber"],
        "size": ["standard", "large", "mini"],
        "rim": ["rounded", "beveled"],
        "surface": ["smooth", "textured", "grip pattern"],
        "weight": ["lightweight", "standard", "heavy-duty"],
        "design": ["solid color", "patterned", "logo printed"],
        "condition": ["new", "worn", "scuffed"],
        "flight pattern": ["stable", "curving"],
        "expression": ["playful", "dynamic", "recreational"],
        "Fine-grained classes": ["Ultimate Frisbee", "Disc Golf", "Freestyle Disc", "Dog Frisbee", "Beach Frisbee", "Glow Disc"],
        "similar classes": {
            "sports ball": {
                "distinguished": ["flat disc shape", "thrown horizontally", "glides through air"],
                "similar": ["used in sports", "thrown object", "recreational use"]
            },
            "kite": {
                "distinguished": ["heavier", "thrown not flown", "no string attached"],
                "similar": ["flies through air", "lightweight", "outdoor activity"]
            },
            "plate": {
                "distinguished": ["sports equipment", "aerodynamic design", "durable plastic"],
                "similar": ["circular flat shape", "disc-like", "lightweight"]
            }
        }
    },

    "skis": {
        "colors": ["black", "white", "red", "blue", "yellow", "graphic designs"],
        "shape": ["long", "narrow", "curved tip"],
        "material": ["fiberglass", "carbon fiber", "wood core"],
        "length": ["short", "medium", "long"],
        "width": ["narrow", "wide"],
        "tip": ["upturned", "rocker", "traditional camber"],
        "tail": ["flat", "twin-tip"],
        "bindings": ["mounted", "adjustable"],
        "edges": ["metal edges", "sharp"],
        "base": ["flat", "waxed", "patterned"],
        "design": ["racing", "all-mountain", "powder", "freestyle"],
        "expression": ["sleek", "performance-oriented", "winter-ready"],
        "Fine-grained classes": ["Downhill Skis", "Cross-Country Skis", "Freestyle Skis", "Touring Skis", "Powder Skis", "Racing Skis"],
        "similar classes": {
            "snowboard": {
                "distinguished": ["two separate skis", "poles used", "parallel stance"],
                "similar": ["winter sports equipment", "glides on snow", "long flat surface"]
            },
            "surfboard": {
                "distinguished": ["used on snow", "narrower", "pair of boards"],
                "similar": ["long board shape", "gliding motion", "recreational equipment"]
            },
            "baseball bat": {
                "distinguished": ["flat surface", "two items", "used for gliding"],
                "similar": ["long shape", "held by user", "sports equipment"]
            }
        }
    },

    "snowboard": {
        "colors": ["black", "white", "colorful graphics", "custom designs"],
        "shape": ["wide", "flat", "curved edges"],
        "material": ["wood core", "fiberglass", "carbon fiber"],
        "length": ["short", "medium", "long"],
        "width": ["narrow waist", "wide"],
        "tip and tail": ["twin-tip", "directional", "tapered"],
        "stance": ["centered", "setback"],
        "bindings": ["strap bindings", "mounted"],
        "edges": ["metal edges", "beveled"],
        "base": ["extruded", "sintered", "waxed"],
        "flex": ["soft", "medium", "stiff"],
        "expression": ["aggressive", "freestyle", "all-mountain"],
        "Fine-grained classes": ["Freestyle Snowboard", "Freeride Snowboard", "All-Mountain Snowboard", "Powder Snowboard", "Split Board"],
        "similar classes": {
            "skis": {
                "distinguished": ["single board", "sideways stance", "no poles"],
                "similar": ["winter sports equipment", "glides on snow", "long flat surface"]
            },
            "surfboard": {
                "distinguished": ["used on snow", "bindings attached", "different shape"],
                "similar": ["board shape", "gliding motion", "balance required"]
            },
            "skateboard": {
                "distinguished": ["used on snow", "bindings", "different terrain"],
                "similar": ["board shape", "balance sport", "youth culture"]
            }
        }
    },

    "sports ball": {
        "colors": ["white", "orange", "yellow", "red", "black and white"],
        "shape": ["spherical", "round"],
        "material": ["leather", "rubber", "synthetic"],
        "size": ["small", "medium", "large"],
        "surface": ["smooth", "textured", "paneled", "dimpled"],
        "pattern": ["solid", "paneled", "striped", "stitched seams"],
        "inflation": ["inflated", "firm", "soft"],
        "weight": ["lightweight", "medium", "heavy"],
        "type": ["soccer", "basketball", "volleyball", "tennis", "baseball"],
        "condition": ["new", "worn", "scuffed"],
        "expression": ["dynamic", "competitive", "athletic"],
        "Fine-grained classes": ["Soccer Ball", "Basketball", "Volleyball", "Tennis Ball", "Baseball", "Football"],
        "similar classes": {
            "frisbee": {
                "distinguished": ["spherical shape", "bounces", "various sports"],
                "similar": ["thrown or kicked", "sports equipment", "recreational use"]
            },
            "orange": {
                "distinguished": ["synthetic material", "sports use", "different texture"],
                "similar": ["round shape", "similar size (some balls)", "spherical"]
            },
            "apple": {
                "distinguished": ["man-made", "sports equipment", "uniform shape"],
                "similar": ["round shape", "similar size", "spherical"]
            }
        }
    },

    "kite": {
        "colors": ["red", "blue", "yellow", "rainbow", "multicolored"],
        "shape": ["diamond", "delta", "box", "dragon"],
        "material": ["nylon", "polyester", "ripstop fabric"],
        "frame": ["wooden sticks", "fiberglass rods", "flexible"],
        "tail": ["long ribbon", "short", "multiple tails"],
        "string": ["attached", "reel", "control lines"],
        "size": ["small", "medium", "large", "giant"],
        "design": ["traditional", "stunt", "decorative patterns"],
        "features": ["single line", "dual line", "quad line"],
        "flight": ["stable", "maneuverable", "acrobatic"],
        "expression": ["colorful", "playful", "soaring"],
        "Fine-grained classes": ["Diamond Kite", "Delta Kite", "Box Kite", "Stunt Kite", "Parafoil", "Dragon Kite"],
        "similar classes": {
            "frisbee": {
                "distinguished": ["flies with string", "larger size", "fabric material"],
                "similar": ["flies through air", "outdoor activity", "wind-dependent"]
            },
            "bird": {
                "distinguished": ["inanimate object", "requires wind", "controlled by string"],
                "similar": ["flies in sky", "lightweight", "aerial movement"]
            },
            "umbrella": {
                "distinguished": ["flies in air", "string attached", "recreational use"],
                "similar": ["fabric canopy", "lightweight", "wind interaction"]
            }
        }
    },

    "baseball bat": {
        "colors": ["brown", "black", "natural wood", "silver", "colorful"],
        "material": ["wood", "aluminum", "composite"],
        "shape": ["cylindrical", "tapered handle", "barrel end"],
        "length": ["short", "standard", "long"],
        "barrel": ["thick", "thin", "wide sweet spot"],
        "handle": ["thin grip", "wrapped grip", "knob end"],
        "finish": ["polished", "matte", "painted"],
        "weight": ["lightweight", "standard", "heavy"],
        "type": ["youth", "adult", "professional"],
        "condition": ["new", "used", "dented"],
        "expression": ["powerful", "athletic", "classic"],
        "Fine-grained classes": ["Wood Bat", "Aluminum Bat", "Composite Bat", "Youth Bat", "Softball Bat", "Training Bat"],
        "similar classes": {
            "tennis racket": {
                "distinguished": ["solid construction", "no strings", "cylindrical shape"],
                "similar": ["sports equipment", "held in hand", "swinging motion"]
            },
            "baseball glove": {
                "distinguished": ["hitting tool", "hard material", "cylindrical"],
                "similar": ["baseball equipment", "sports gear", "handheld"]
            },
            "umbrella": {
                "distinguished": ["solid structure", "sports use", "swinging purpose"],
                "similar": ["long handle", "held by hand", "cylindrical shaft"]
            }
        }
    },

    "baseball glove": {
        "colors": ["brown", "black", "tan", "red"],
        "material": ["leather", "synthetic leather"],
        "shape": ["curved", "pocket", "webbed"],
        "size": ["small", "medium", "large"],
        "webbing": ["closed web", "open web", "H-web", "basket web"],
        "pocket": ["deep", "shallow", "broken-in"],
        "padding": ["thick", "thin", "padded palm"],
        "fingers": ["separate", "connected"],
        "wrist": ["adjustable strap", "velcro", "laced"],
        "hand": ["right-handed", "left-handed"],
        "condition": ["new", "broken-in", "well-worn"],
        "expression": ["protective", "athletic", "traditional"],
        "Fine-grained classes": ["Catcher's Mitt", "First Base Glove", "Infield Glove", "Outfield Glove", "Pitcher's Glove", "Youth Glove"],
        "similar classes": {
            "baseball bat": {
                "distinguished": ["catching tool", "soft material", "hand-shaped"],
                "similar": ["baseball equipment", "sports gear", "handheld"]
            },
            "oven mitt": {
                "distinguished": ["sports use", "specific finger design", "leather material"],
                "similar": ["hand protection", "padded", "worn on hand"]
            },
            "backpack": {
                "distinguished": ["worn on hand", "catching purpose", "smaller size"],
                "similar": ["leather material", "straps", "holds items"]
            }
        }
    },

    "skateboard": {
        "colors": ["black", "natural wood", "colorful graphics", "custom designs"],
        "deck": ["wooden", "flat", "concave", "kick tail", "nose"],
        "length": ["short", "standard", "long"],
        "width": ["narrow", "wide"],
        "trucks": ["metal", "adjustable", "mounted underneath"],
        "wheels": ["four wheels", "polyurethane", "small", "large"],
        "bearings": ["metal bearings", "smooth rolling"],
        "grip tape": ["black", "textured", "custom patterns"],
        "graphics": ["bottom design", "brand logo", "custom art"],
        "style": ["street", "vert", "cruiser", "longboard"],
        "expression": ["rebellious", "athletic", "urban"],
        "Fine-grained classes": ["Street Skateboard", "Longboard", "Cruiser", "Penny Board", "Electric Skateboard", "Vert Skateboard"],
        "similar classes": {
            "snowboard": {
                "distinguished": ["wheels attached", "used on pavement", "smaller size"],
                "similar": ["board shape", "balance sport", "youth culture"]
            },
            "surfboard": {
                "distinguished": ["wheels", "used on land", "different shape"],
                "similar": ["board design", "balance required", "gliding motion"]
            },
            "bicycle": {
                "distinguished": ["no pedals", "pushed with foot", "smaller"],
                "similar": ["wheeled transport", "outdoor activity", "youth-oriented"]
            }
        }
    },

    "surfboard": {
        "colors": ["white", "blue", "yellow", "multicolored", "custom designs"],
        "shape": ["long", "streamlined", "pointed nose", "tail"],
        "material": ["foam core", "fiberglass", "epoxy"],
        "length": ["short", "medium", "long"],
        "thickness": ["thin", "thick"],
        "nose": ["pointed", "rounded"],
        "tail": ["square", "round", "swallow", "pin"],
        "rails": ["sharp", "soft", "rounded"],
        "fins": ["single fin", "tri-fin", "quad fin", "removable"],
        "rocker": ["flat", "curved"],
        "design": ["shortboard", "longboard", "fish", "funboard"],
        "expression": ["sleek", "oceanic", "adventurous"],
        "Fine-grained classes": ["Shortboard", "Longboard", "Fish Board", "Funboard", "Gun", "Stand-Up Paddleboard"],
        "similar classes": {
            "skateboard": {
                "distinguished": ["used on water", "no wheels", "larger size"],
                "similar": ["board design", "balance sport", "gliding motion"]
            },
            "snowboard": {
                "distinguished": ["used on water", "no bindings", "different shape"],
                "similar": ["board shape", "gliding motion", "balance required"]
            },
            "boat": {
                "distinguished": ["smaller", "ridden standing", "no motor"],
                "similar": ["water vehicle", "floats on water", "recreational use"]
            }
        }
    },

    "tennis racket": {
        "colors": ["black", "white", "red", "blue", "yellow"],
        "frame": ["graphite", "aluminum", "carbon fiber"],
        "shape": ["oval head", "elongated"],
        "head size": ["small", "midsize", "oversize"],
        "strings": ["nylon", "polyester", "natural gut", "criss-cross pattern"],
        "handle": ["grip wrapped", "cushioned", "leather grip"],
        "length": ["standard", "extended"],
        "weight": ["lightweight", "medium", "heavy"],
        "throat": ["open throat", "closed throat"],
        "condition": ["new", "restrung", "worn"],
        "expression": ["dynamic", "precise", "athletic"],
        "Fine-grained classes": ["Power Racket", "Control Racket", "Tweener Racket", "Junior Racket", "Professional Racket"],
        "similar classes": {
            "baseball bat": {
                "distinguished": ["has strings", "oval head", "hitting different object"],
                "similar": ["sports equipment", "swinging motion", "held in hand"]
            },
            "badminton racket": {
                "distinguished": ["thicker strings", "larger head", "different sport"],
                "similar": ["racket design", "strings present", "swinging sports"]
            },
            "frying pan": {
                "distinguished": ["sports use", "strings", "lightweight"],
                "similar": ["flat surface with handle", "circular head", "held by handle"]
            }
        }
    },

    "banana": {
        "colors": ["yellow", "green", "brown spots"],
        "shape": ["curved", "elongated", "crescent"],
        "size": ["small", "medium", "large"],
        "peel": ["smooth", "textured", "spotted", "bruised"],
        "stem": ["attached", "green stem"],
        "ripeness": ["green", "yellow", "overripe with spots"],
        "condition": ["fresh", "ripe", "overripe"],
        "bunch": ["single", "clustered"],
        "texture": ["firm", "soft"],
        "expression": ["fresh", "natural", "tropical"],
        "distinctive marking": ["natural curve", "stem end"],
        "Fine-grained classes": ["Cavendish", "Plantain", "Lady Finger", "Red Banana", "Burro Banana"],
        "similar classes": {
            "hot dog": {
                "distinguished": ["fruit", "peel", "grows on plant"],
                "similar": ["elongated shape", "curved form", "yellow/tan color"]
            },
            "carrot": {
                "distinguished": ["curved shape", "yellow color", "peelable skin"],
                "similar": ["elongated vegetable/fruit", "natural food", "similar length"]
            },
            "tennis racket": {
                "distinguished": ["edible", "soft", "organic"],
                "similar": ["curved shape", "yellow color", "handheld object"]
            }
        }
    },

    "apple": {
        "colors": ["red", "green", "yellow", "mix"],
        "shape": ["round", "spherical", "slightly flattened"],
        "size": ["small", "medium", "large"],
        "skin": ["smooth", "waxy", "shiny"],
        "stem": ["short", "brown", "attached"],
        "bottom": ["indented", "crowned"],
        "condition": ["fresh", "bruised", "polished"],
        "variety": ["red delicious", "granny smith", "fuji", "gala"],
        "expression": ["fresh", "crisp", "healthy"],
        "distinctive marking": ["natural shine", "stem indent"],
        "Fine-grained classes": ["Red Delicious", "Granny Smith", "Fuji", "Gala", "Honeycrisp", "Golden Delicious"],
        "similar classes": {
            "orange": {
                "distinguished": ["different color", "smooth skin", "different taste"],
                "similar": ["round fruit", "similar size", "fresh produce"]
            },
            "sports ball": {
                "distinguished": ["edible", "organic", "softer"],
                "similar": ["round shape", "similar size", "spherical"]
            },
            "tomato": {
                "distinguished": ["firmer", "sweet taste", "different stem"],
                "similar": ["round shape", "smooth skin", "produce item"]
            }
        }
    },

    "sandwich": {
        "colors": ["brown bread", "white bread", "multicolored fillings"],
        "bread": ["white", "wheat", "sourdough", "bun", "sliced"],
        "shape": ["rectangular", "triangular", "round"],
        "layers": ["multiple layers", "visible fillings"],
        "fillings": ["meat", "cheese", "vegetables", "condiments"],
        "size": ["small", "regular", "large", "sub"],
        "cut": ["whole", "half", "quarters", "diagonal cut"],
        "presentation": ["stacked", "toothpick inserted", "wrapped"],
        "condition": ["fresh", "toasted", "grilled"],
        "type": ["deli", "grilled", "club", "submarine"],
        "expression": ["appetizing", "hearty", "satisfying"],
        "Fine-grained classes": ["Club Sandwich", "BLT", "Grilled Cheese", "Submarine", "Panini", "Open-faced"],
        "similar classes": {
            "hot dog": {
                "distinguished": ["bread slices", "stacked layers", "different shape"],
                "similar": ["bread-based food", "handheld meal", "common lunch item"]
            },
            "pizza": {
                "distinguished": ["stacked construction", "bread slices", "portable"],
                "similar": ["bread-based food", "multiple ingredients", "popular food"]
            },
            "cake": {
                "distinguished": ["savory food", "bread not cake", "lunch item"],
                "similar": ["layered structure", "stacked appearance", "can be sliced"]
            }
        }
    },

    "orange": {
        "colors": ["orange", "yellow-orange", "reddish-orange"],
        "shape": ["round", "spherical", "slightly oval"],
        "size": ["small", "medium", "large"],
        "peel": ["textured", "dimpled", "bumpy", "thick"],
        "surface": ["rough", "pebbled texture"],
        "stem": ["small green stem", "button top"],
        "condition": ["fresh", "ripe", "dried"],
        "segments": ["visible when peeled", "sectioned"],
        "expression": ["fresh", "juicy", "citrus"],
        "distinctive marking": ["pebbled texture", "bright color"],
        "Fine-grained classes": ["Navel Orange", "Valencia Orange", "Blood Orange", "Mandarin", "Tangerine", "Clementine"],
        "similar classes": {
            "apple": {
                "distinguished": ["orange color", "textured peel", "citrus"],
                "similar": ["round fruit", "similar size", "fresh produce"]
            },
            "sports ball": {
                "distinguished": ["edible", "organic", "peelable"],
                "similar": ["round shape", "similar size (basketball)", "spherical"]
            },
            "grapefruit": {
                "distinguished": ["smaller size", "orange color", "sweeter taste"],
                "similar": ["citrus fruit", "round shape", "textured peel"]
            }
        }
    },

    "broccoli": {
        "colors": ["green", "dark green", "forest green"],
        "shape": ["tree-like", "clustered florets", "crown"],
        "florets": ["tightly packed", "bumpy texture", "small buds"],
        "stalk": ["thick", "pale green", "fibrous"],
        "size": ["small", "medium", "large head"],
        "texture": ["rough", "bumpy florets", "smooth stalk"],
        "condition": ["fresh", "crisp", "wilted"],
        "presentation": ["whole", "cut florets", "with stem"],
        "expression": ["healthy", "fresh", "nutritious"],
        "distinctive marking": ["tree-like appearance", "dense florets"],
        "Fine-grained classes": ["Calabrese Broccoli", "Sprouting Broccoli", "Purple Broccoli", "Broccolini"],
        "similar classes": {
            "pottedplant": {
                "distinguished": ["edible", "cut vegetable", "no pot"],
                "similar": ["green color", "plant-based", "organic structure"]
            },
            "cauliflower": {
                "distinguished": ["green color", "different texture", "looser florets"],
                "similar": ["cruciferous vegetable", "floret structure", "similar shape"]
            },
            "tree": {
                "distinguished": ["small size", "edible", "vegetable"],
                "similar": ["tree-like appearance", "branching structure", "green canopy"]
            }
        }
    },

    "carrot": {
        "colors": ["orange", "purple", "yellow", "white"],
        "shape": ["elongated", "tapered", "conical"],
        "size": ["small", "medium", "large"],
        "top": ["green leafy tops", "trimmed"],
        "skin": ["smooth", "slightly rough"],
        "texture": ["firm", "crisp"],
        "condition": ["fresh", "peeled", "whole", "chopped"],
        "root": ["pointed tip", "root hairs"],
        "presentation": ["whole", "baby carrots", "sliced", "peeled"],
        "expression": ["fresh", "crunchy", "healthy"],
        "distinctive marking": ["orange color", "tapered shape"],
        "Fine-grained classes": ["Imperator", "Danvers", "Chantenay", "Nantes", "Baby Carrots", "Purple Carrots"],
        "similar classes": {
            "banana": {
                "distinguished": ["straight or tapered", "orange color", "vegetable"],
                "similar": ["elongated shape", "similar length", "natural food"]
            },
            "hot dog": {
                "distinguished": ["vegetable", "firm texture", "orange color"],
                "similar": ["elongated shape", "similar size", "tapered form"]
            },
            "baseball bat": {
                "distinguished": ["edible", "smaller", "vegetable"],
                "similar": ["elongated shape", "tapered", "held by one end"]
            }
        }
    },

    "hot dog": {
        "colors": ["brown", "reddish-brown", "pink"],
        "bun": ["white", "wheat", "sesame seeds"],
        "shape": ["elongated", "cylindrical sausage"],
        "size": ["regular", "foot-long"],
        "toppings": ["ketchup", "mustard", "relish", "onions"],
        "presentation": ["in bun", "loaded", "plain"],
        "condition": ["grilled", "boiled", "charred"],
        "style": ["classic", "Chicago-style", "New York-style"],
        "features": ["grill marks", "split bun", "overflowing toppings"],
        "expression": ["appetizing", "casual", "street food"],
        "distinctive marking": ["sausage in bun", "various toppings"],
        "Fine-grained classes": ["Classic Hot Dog", "Chicago Dog", "Chili Dog", "Corn Dog", "Bratwurst"],
        "similar classes": {
            "sandwich": {
                "distinguished": ["single sausage", "long bun", "different shape"],
                "similar": ["bread-based food", "handheld meal", "common food"]
            },
            "banana": {
                "distinguished": ["cooked food", "in bun", "savory"],
                "similar": ["elongated shape", "curved form", "similar length"]
            },
            "carrot": {
                "distinguished": ["cooked meat", "in bun", "prepared food"],
                "similar": ["elongated shape", "similar size", "cylindrical"]
            }
        }
    },

    "pizza": {
        "colors": ["red sauce", "yellow cheese", "brown crust", "varied toppings"],
        "shape": ["round", "square", "triangular slice"],
        "crust": ["thin", "thick", "stuffed", "crispy"],
        "sauce": ["tomato sauce", "white sauce"],
        "cheese": ["melted", "mozzarella", "stretchy"],
        "toppings": ["pepperoni", "vegetables", "meat", "variety"],
        "size": ["personal", "medium", "large", "extra-large"],
        "presentation": ["whole pizza", "sliced", "one slice"],
        "condition": ["hot", "fresh", "cheesy"],
        "style": ["New York", "Chicago", "Neapolitan", "Sicilian"],
        "expression": ["delicious", "cheesy", "satisfying"],
        "Fine-grained classes": ["Margherita", "Pepperoni", "Hawaiian", "Meat Lovers", "Veggie", "Deep Dish"],
        "similar classes": {
            "sandwich": {
                "distinguished": ["round flat shape", "baked", "sliced radially"],
                "similar": ["bread-based food", "multiple ingredients", "popular meal"]
            },
            "cake": {
                "distinguished": ["savory", "cheese and sauce", "dinner food"],
                "similar": ["round shape", "sliced", "layered ingredients"]
            },
            "frisbee": {
                "distinguished": ["edible", "thick", "topped with ingredients"],
                "similar": ["round flat shape", "disc-like", "circular"]
            }
        }
    },

    "donut": {
        "colors": ["brown", "golden", "pink frosting", "chocolate", "varied"],
        "shape": ["ring", "round with hole", "filled round"],
        "size": ["regular", "mini", "large"],
        "coating": ["glazed", "frosted", "powdered sugar", "plain"],
        "frosting": ["chocolate", "vanilla", "strawberry", "maple"],
        "toppings": ["sprinkles", "nuts", "coconut flakes", "crumbles"],
        "texture": ["fluffy", "cake-like", "yeast-raised"],
        "hole": ["center hole", "no hole if filled"],
        "condition": ["fresh", "glazed", "decorated"],
        "type": ["glazed", "jelly-filled", "cream-filled", "old-fashioned"],
        "expression": ["sweet", "indulgent", "tempting"],
        "Fine-grained classes": ["Glazed Donut", "Jelly Donut", "Chocolate Donut", "Old-Fashioned", "Cruller", "Boston Cream"],
        "similar classes": {
            "cake": {
                "distinguished": ["ring shape", "smaller size", "individual serving"],
                "similar": ["sweet dessert", "frosted", "baked good"]
            },
            "bagel": {
                "distinguished": ["sweet", "frosted", "softer texture"],
                "similar": ["ring shape", "baked good", "circular with hole"]
            },
            "frisbee": {
                "distinguished": ["edible", "smaller", "sweet food"],
                "similar": ["circular shape", "ring form", "flat"]
            }
        }
    },

    "cake": {
        "colors": ["white frosting", "chocolate", "pink", "varied colors"],
        "shape": ["round layers", "rectangular", "square"],
        "layers": ["single", "multiple", "tiered"],
        "frosting": ["smooth", "textured", "buttercream", "fondant"],
        "decoration": ["flowers", "writing", "candles", "sprinkles"],
        "size": ["small", "medium", "large", "wedding-sized"],
        "presentation": ["whole", "sliced", "plated"],
        "style": ["birthday", "wedding", "sheet cake", "cupcake"],
        "features": ["candles", "piped decorations", "fruit toppings"],
        "condition": ["decorated", "fresh", "celebration"],
        "expression": ["festive", "sweet", "celebratory"],
        "Fine-grained classes": ["Birthday Cake", "Wedding Cake", "Chocolate Cake", "Cheesecake", "Layer Cake", "Bundt Cake"],
        "similar classes": {
            "pizza": {
                "distinguished": ["sweet dessert", "frosted", "celebration food"],
                "similar": ["round shape", "sliced", "layered"]
            },
            "donut": {
                "distinguished": ["larger size", "layers", "served on occasions"],
                "similar": ["sweet dessert", "frosted", "baked good"]
            },
            "sandwich": {
                "distinguished": ["sweet", "frosted", "dessert item"],
                "similar": ["layered structure", "stacked", "can be sliced"]
            }
        }
    }
}

meta_COCO_info_T4 = {
    "bed": {
        "colors": ["white", "brown", "gray", "black", "beige"],
        "frame": ["wood", "metal", "upholstered"],
        "headboard": ["tall", "short", "padded", "slatted", "absent"],
        "footboard": ["present", "absent", "low", "high"],
        "size": ["twin", "full", "queen", "king"],
        "mattress": ["visible", "covered with bedding"],
        "bedding": ["sheets", "comforter", "pillows", "blankets"],
        "legs": ["short", "tall", "platform", "no legs"],
        "style": ["modern", "traditional", "minimalist", "canopy"],
        "features": ["storage drawers", "built-in nightstands", "adjustable"],
        "condition": ["made", "unmade", "neat"],
        "expression": ["comfortable", "inviting", "restful"],
        "Fine-grained classes": ["Platform Bed", "Sleigh Bed", "Canopy Bed", "Murphy Bed", "Bunk Bed", "Adjustable Bed"],
        "similar classes": {
            "sofa": {
                "distinguished": ["designed for sleeping", "horizontal use", "larger size"],
                "similar": ["soft surface", "provides comfort", "furniture for resting"]
            },
            "bench": {
                "distinguished": ["mattress", "bedding", "sleeping purpose"],
                "similar": ["long structure", "provides support", "can accommodate person"]
            },
            "chair": {
                "distinguished": ["horizontal orientation", "sleeping function", "much larger"],
                "similar": ["provides comfort", "furniture item", "used for resting"]
            }
        }
    },

    "toilet": {
        "colors": ["white", "beige", "cream"],
        "material": ["porcelain", "ceramic"],
        "bowl": ["round", "elongated"],
        "tank": ["attached", "wall-mounted", "concealed"],
        "seat": ["closed", "open", "with lid"],
        "flush": ["handle", "button", "dual-flush"],
        "height": ["standard", "comfort height"],
        "style": ["one-piece", "two-piece", "wall-hung"],
        "features": ["soft-close lid", "bidet function", "water-saving"],
        "condition": ["clean", "in use"],
        "expression": ["functional", "sanitary", "essential"],
        "Fine-grained classes": ["Two-Piece Toilet", "One-Piece Toilet", "Wall-Mounted Toilet", "Smart Toilet", "Bidet Toilet"],
        "similar classes": {
            "sink": {
                "distinguished": ["sitting fixture", "bowl shape", "different purpose"],
                "similar": ["porcelain fixture", "plumbing fixture", "bathroom item"]
            },
            "chair": {
                "distinguished": ["plumbing fixture", "porcelain material", "specific function"],
                "similar": ["sitting furniture", "bowl-like shape", "found in homes"]
            },
            "potted plant": {
                "distinguished": ["plumbing fixture", "porcelain", "functional purpose"],
                "similar": ["white color", "bowl shape", "found indoors"]
            }
        }
    },

    "laptop": {
        "colors": ["silver", "black", "gray", "white", "gold"],
        "body": ["thin", "compact", "rectangular"],
        "screen": ["LED", "LCD", "retina display", "matte", "glossy"],
        "keyboard": ["built-in", "backlit", "standard layout"],
        "touchpad": ["centered", "rectangular", "smooth"],
        "size": ["11-inch", "13-inch", "15-inch", "17-inch"],
        "ports": ["USB", "HDMI", "headphone jack", "charging port"],
        "logo": ["brand logo", "on lid", "illuminated"],
        "condition": ["open", "closed", "in use"],
        "features": ["webcam", "fingerprint sensor", "touchscreen"],
        "expression": ["portable", "modern", "productive"],
        "Fine-grained classes": ["Ultrabook", "Gaming Laptop", "Business Laptop", "2-in-1 Convertible", "Chromebook", "MacBook"],
        "similar classes": {
            "tvmonitor": {
                "distinguished": ["portable", "keyboard attached", "computing device"],
                "similar": ["screen display", "rectangular shape", "electronic device"]
            },
            "keyboard": {
                "distinguished": ["includes screen", "portable computer", "integrated device"],
                "similar": ["has keyboard", "rectangular", "input device"]
            },
            "book": {
                "distinguished": ["electronic", "screen", "powered device"],
                "similar": ["opens like book", "portable", "rectangular when closed"]
            }
        }
    },

    "mouse": {
        "colors": ["black", "white", "gray", "silver"],
        "shape": ["ergonomic", "curved", "symmetrical"],
        "size": ["small", "standard", "large"],
        "buttons": ["two buttons", "three buttons", "scroll wheel"],
        "connection": ["wired", "wireless", "bluetooth"],
        "sensor": ["optical", "laser"],
        "material": ["plastic", "rubber grip", "matte finish"],
        "features": ["programmable buttons", "adjustable DPI", "RGB lighting"],
        "style": ["office", "gaming", "travel"],
        "condition": ["new", "used"],
        "expression": ["precise", "functional", "ergonomic"],
        "Fine-grained classes": ["Wireless Mouse", "Gaming Mouse", "Ergonomic Mouse", "Trackball Mouse", "Vertical Mouse"],
        "similar classes": {
            "remote": {
                "distinguished": ["computer accessory", "smaller size", "pointing device"],
                "similar": ["handheld device", "has buttons", "wireless option"]
            },
            "cell phone": {
                "distinguished": ["computer peripheral", "no screen", "input device"],
                "similar": ["small handheld", "electronic device", "portable"]
            },
            "apple": {
                "distinguished": ["electronic device", "plastic material", "tech accessory"],
                "similar": ["small size", "rounded shape", "fits in hand"]
            }
        }
    },

    "remote": {
        "colors": ["black", "gray", "silver", "white"],
        "shape": ["rectangular", "elongated", "ergonomic"],
        "size": ["small", "standard", "large"],
        "buttons": ["many buttons", "number pad", "directional pad"],
        "display": ["LED indicator", "small screen", "no display"],
        "battery": ["compartment on back", "rechargeable"],
        "material": ["plastic", "rubber buttons"],
        "features": ["voice control", "touchpad", "backlit buttons"],
        "type": ["TV remote", "universal remote", "streaming remote"],
        "condition": ["new", "worn buttons"],
        "expression": ["functional", "convenient", "handheld"],
        "Fine-grained classes": ["TV Remote", "Universal Remote", "Streaming Remote", "Smart Remote", "Voice Remote"],
        "similar classes": {
            "mouse": {
                "distinguished": ["entertainment device", "many buttons", "infrared sensor"],
                "similar": ["handheld device", "wireless", "has buttons"]
            },
            "cell phone": {
                "distinguished": ["single purpose", "simpler display", "IR signal"],
                "similar": ["handheld device", "has buttons", "rectangular shape"]
            },
            "calculator": {
                "distinguished": ["control device", "different button layout", "entertainment use"],
                "similar": ["button array", "rectangular", "handheld"]
            }
        }
    },

    "keyboard": {
        "colors": ["black", "white", "gray", "RGB multicolor"],
        "shape": ["rectangular", "ergonomic split", "compact"],
        "size": ["full-size", "tenkeyless", "60%", "compact"],
        "keys": ["QWERTY layout", "mechanical", "membrane", "chiclet"],
        "connection": ["wired", "wireless", "bluetooth"],
        "features": ["numeric keypad", "function keys", "media keys", "backlit"],
        "material": ["plastic", "aluminum", "metal frame"],
        "switches": ["mechanical", "membrane", "scissor"],
        "style": ["gaming", "office", "ergonomic"],
        "condition": ["new", "worn keycaps"],
        "expression": ["functional", "tactile", "productive"],
        "Fine-grained classes": ["Mechanical Keyboard", "Membrane Keyboard", "Ergonomic Keyboard", "Gaming Keyboard", "Wireless Keyboard"],
        "similar classes": {
            "laptop": {
                "distinguished": ["separate device", "no screen", "input only"],
                "similar": ["has keys", "QWERTY layout", "rectangular"]
            },
            "piano": {
                "distinguished": ["computer input", "smaller keys", "letters not notes"],
                "similar": ["many keys in row", "pressed for input", "rectangular"]
            },
            "remote": {
                "distinguished": ["many more keys", "typing purpose", "larger size"],
                "similar": ["button array", "input device", "rectangular"]
            }
        }
    },

    "cell phone": {
        "colors": ["black", "white", "silver", "gold", "blue", "various"],
        "shape": ["rectangular", "rounded edges", "slim"],
        "screen": ["touchscreen", "large display", "edge-to-edge"],
        "size": ["small", "standard", "phablet"],
        "case": ["with case", "without case", "screen protector"],
        "camera": ["front camera", "rear camera", "multiple lenses"],
        "buttons": ["side buttons", "power button", "volume buttons"],
        "ports": ["charging port", "headphone jack"],
        "condition": ["new", "scratched", "cracked screen"],
        "features": ["notch", "hole-punch camera", "fingerprint sensor"],
        "expression": ["modern", "essential", "connected"],
        "Fine-grained classes": ["Smartphone", "iPhone", "Android Phone", "Flip Phone", "Folding Phone"],
        "similar classes": {
            "remote": {
                "distinguished": ["touchscreen", "many functions", "communication device"],
                "similar": ["handheld device", "rectangular", "has buttons"]
            },
            "tablet": {
                "distinguished": ["smaller size", "phone functions", "portable"],
                "similar": ["touchscreen", "rectangular", "portable device"]
            },
            "calculator": {
                "distinguished": ["touchscreen", "many apps", "communication"],
                "similar": ["rectangular", "handheld", "has display"]
            }
        }
    },

    "book": {
        "colors": ["varied cover colors", "white pages", "colorful"],
        "shape": ["rectangular", "thick", "thin"],
        "size": ["small", "standard", "large", "oversized"],
        "cover": ["hardcover", "paperback", "dust jacket"],
        "spine": ["visible title", "thick", "thin"],
        "pages": ["many pages", "white", "yellowed"],
        "condition": ["new", "worn", "open", "closed"],
        "features": ["bookmark", "illustrations", "text"],
        "type": ["novel", "textbook", "magazine", "comic"],
        "binding": ["perfect bound", "spiral", "hardbound"],
        "expression": ["informative", "classic", "literary"],
        "Fine-grained classes": ["Hardcover Book", "Paperback", "Textbook", "Novel", "Comic Book", "Magazine"],
        "similar classes": {
            "laptop": {
                "distinguished": ["paper pages", "no screen", "printed text"],
                "similar": ["opens like laptop", "rectangular", "portable"]
            },
            "magazine": {
                "distinguished": ["bound pages", "longer content", "book format"],
                "similar": ["printed pages", "rectangular", "reading material"]
            },
            "tablet": {
                "distinguished": ["physical pages", "no power needed", "printed"],
                "similar": ["rectangular", "portable", "reading device"]
            }
        }
    },

    "clock": {
        "colors": ["white", "black", "silver", "gold", "wood"],
        "shape": ["round", "square", "rectangular"],
        "face": ["analog", "digital", "numbered", "roman numerals"],
        "hands": ["hour hand", "minute hand", "second hand"],
        "size": ["small", "medium", "large", "wall-sized"],
        "mounting": ["wall-mounted", "tabletop", "standing"],
        "frame": ["wood", "metal", "plastic"],
        "display": ["LED", "LCD", "mechanical"],
        "features": ["alarm", "pendulum", "chimes", "date display"],
        "style": ["modern", "vintage", "minimalist", "ornate"],
        "expression": ["precise", "decorative", "functional"],
        "Fine-grained classes": ["Wall Clock", "Alarm Clock", "Grandfather Clock", "Digital Clock", "Cuckoo Clock", "Atomic Clock"],
        "similar classes": {
            "tvmonitor": {
                "distinguished": ["displays time only", "smaller", "simpler function"],
                "similar": ["displays information", "rectangular or circular", "found in homes"]
            },
            "plate": {
                "distinguished": ["displays time", "has hands or digits", "functional device"],
                "similar": ["circular shape", "flat face", "wall-mounted option"]
            },
            "picture frame": {
                "distinguished": ["displays time", "has mechanism", "functional"],
                "similar": ["wall-mounted", "framed", "decorative"]
            }
        }
    },

    "vase": {
        "colors": ["white", "blue", "clear", "multicolored", "ceramic colors"],
        "material": ["ceramic", "glass", "porcelain", "crystal"],
        "shape": ["cylindrical", "bulbous", "tapered", "wide mouth"],
        "size": ["small", "medium", "tall", "large"],
        "neck": ["narrow", "wide", "flared"],
        "base": ["stable", "flat", "rounded"],
        "surface": ["smooth", "textured", "glazed", "painted"],
        "pattern": ["floral", "geometric", "solid color", "decorative"],
        "style": ["modern", "traditional", "antique", "minimalist"],
        "condition": ["empty", "with flowers", "decorative"],
        "expression": ["elegant", "decorative", "artistic"],
        "Fine-grained classes": ["Flower Vase", "Decorative Vase", "Bud Vase", "Floor Vase", "Ceramic Vase", "Glass Vase"],
        "similar classes": {
            "bottle": {
                "distinguished": ["wider opening", "decorative purpose", "holds flowers"],
                "similar": ["cylindrical shape", "holds liquids", "glass or ceramic"]
            },
            "cup": {
                "distinguished": ["taller", "decorative use", "not for drinking"],
                "similar": ["holds contents", "cylindrical", "various materials"]
            },
            "pottedplant": {
                "distinguished": ["no soil", "holds cut flowers", "watertight"],
                "similar": ["holds plants", "decorative", "cylindrical container"]
            }
        }
    },

    "scissors": {
        "colors": ["silver blades", "black handles", "colored handles"],
        "blades": ["metal", "sharp", "stainless steel", "crossed"],
        "handles": ["plastic", "rubber grip", "metal", "finger holes"],
        "size": ["small", "medium", "large"],
        "type": ["straight", "curved", "serrated"],
        "pivot": ["screw joint", "rivet"],
        "tips": ["pointed", "blunt", "rounded"],
        "features": ["ergonomic grip", "soft grip", "spring-loaded"],
        "style": ["office", "kitchen", "craft", "medical"],
        "condition": ["sharp", "dull", "open", "closed"],
        "expression": ["sharp", "precise", "functional"],
        "Fine-grained classes": ["Office Scissors", "Kitchen Shears", "Craft Scissors", "Pinking Shears", "Medical Scissors"],
        "similar classes": {
            "knife": {
                "distinguished": ["two blades", "crossing design", "finger holes"],
                "similar": ["cutting tool", "sharp blades", "metal construction"]
            },
            "pliers": {
                "distinguished": ["sharp blades", "cutting function", "scissor action"],
                "similar": ["two handles", "pivot point", "hand tool"]
            },
            "tweezers": {
                "distinguished": ["larger size", "finger holes", "cutting ability"],
                "similar": ["two pieces joined", "gripping action", "precision tool"]
            }
        }
    },

    "teddy bear": {
        "colors": ["brown", "tan", "white", "pink", "various"],
        "fur": ["soft", "fluffy", "plush", "fuzzy"],
        "size": ["small", "medium", "large", "giant"],
        "ears": ["round", "oval", "sewn on"],
        "eyes": ["black button", "plastic", "embroidered"],
        "nose": ["stitched", "black", "button"],
        "limbs": ["movable", "jointed", "stuffed"],
        "body": ["stuffed", "plump", "soft"],
        "features": ["bow tie", "ribbon", "clothing", "accessories"],
        "condition": ["new", "worn", "loved"],
        "expression": ["cute", "friendly", "comforting"],
        "Fine-grained classes": ["Classic Teddy Bear", "Plush Bear", "Build-a-Bear", "Vintage Bear", "Character Bear"],
        "similar classes": {
            "dog": {
                "distinguished": ["inanimate", "plush toy", "no movement"],
                "similar": ["furry", "four limbs", "cute appearance"]
            },
            "bear": {
                "distinguished": ["toy", "soft material", "smaller size"],
                "similar": ["bear shape", "furry", "brown color"]
            },
            "backpack": {
                "distinguished": ["toy", "not functional", "decorative"],
                "similar": ["soft material", "carried around", "companion item"]
            }
        }
    },

    "hair drier": {
        "colors": ["black", "white", "red", "pink", "purple"],
        "body": ["plastic", "ergonomic", "compact"],
        "shape": ["gun-shaped", "cylindrical barrel"],
        "nozzle": ["concentrator", "diffuser", "wide"],
        "handle": ["pistol grip", "folding", "ergonomic"],
        "size": ["compact", "standard", "professional"],
        "cord": ["long cord", "retractable", "cordless"],
        "buttons": ["power switch", "heat settings", "speed settings"],
        "features": ["cool shot button", "ionic technology", "multiple attachments"],
        "condition": ["new", "used"],
        "expression": ["functional", "powerful", "practical"],
        "Fine-grained classes": ["Professional Hair Dryer", "Travel Hair Dryer", "Ionic Hair Dryer", "Ceramic Hair Dryer"],
        "similar classes": {
            "toothbrush": {
                "distinguished": ["larger size", "electrical appliance", "heat function"],
                "similar": ["handheld device", "personal care", "bathroom item"]
            },
            "remote": {
                "distinguished": ["heating element", "air blower", "larger size"],
                "similar": ["handheld", "has buttons", "pistol-grip shape"]
            },
            "hair brush": {
                "distinguished": ["electrical", "produces heat", "air flow"],
                "similar": ["hair care tool", "handheld", "personal grooming"]
            }
        }
    },

    "toothbrush": {
        "colors": ["blue", "green", "pink", "white", "multicolored"],
        "handle": ["plastic", "rubber grip", "ergonomic", "straight"],
        "bristles": ["soft", "medium", "firm", "angled"],
        "head": ["small", "medium", "large", "diamond-shaped"],
        "size": ["child", "adult"],
        "type": ["manual", "electric", "battery-powered"],
        "features": ["tongue cleaner", "flexible neck", "indicator bristles"],
        "condition": ["new", "used", "worn bristles"],
        "neck": ["straight", "angled", "flexible"],
        "expression": ["hygienic", "essential", "dental care"],
        "Fine-grained classes": ["Manual Toothbrush", "Electric Toothbrush", "Battery Toothbrush", "Kids Toothbrush", "Travel Toothbrush"],
        "similar classes": {
            "hair drier": {
                "distinguished": ["smaller", "manual use", "oral care"],
                "similar": ["handheld", "personal care", "bathroom item"]
            },
            "fork": {
                "distinguished": ["bristles not tines", "hygiene use", "softer material"],
                "similar": ["elongated handle", "pronged end", "held in hand"]
            },
            "pen": {
                "distinguished": ["bristled head", "cleaning tool", "dental care"],
                "similar": ["long thin handle", "handheld", "pointed end"]
            }
        }
    },

    "wine glass": {
        "colors": ["clear", "tinted", "colored"],
        "material": ["glass", "crystal"],
        "bowl": ["round", "wide", "tulip-shaped", "balloon"],
        "stem": ["long", "short", "thin"],
        "base": ["flat", "round", "stable"],
        "size": ["small", "standard", "large"],
        "rim": ["thin", "smooth", "wide opening"],
        "style": ["red wine", "white wine", "champagne flute"],
        "condition": ["empty", "filled", "clean"],
        "features": ["etched design", "colored stem", "elegant"],
        "expression": ["elegant", "sophisticated", "refined"],
        "Fine-grained classes": ["Red Wine Glass", "White Wine Glass", "Champagne Flute", "Port Glass", "Dessert Wine Glass"],
        "similar classes": {
            "cup": {
                "distinguished": ["stem present", "wider bowl", "wine-specific"],
                "similar": ["holds liquids", "glass material", "drinking vessel"]
            },
            "bottle": {
                "distinguished": ["drinking vessel", "open top", "stemmed"],
                "similar": ["holds liquid", "glass material", "wine-related"]
            },
            "vase": {
                "distinguished": ["smaller", "drinking purpose", "stemmed"],
                "similar": ["glass material", "holds liquids", "decorative"]
            }
        }
    },

    "cup": {
        "colors": ["white", "black", "colored", "patterned"],
        "material": ["ceramic", "porcelain", "glass", "plastic", "metal"],
        "shape": ["cylindrical", "tapered", "mug-shaped"],
        "size": ["espresso", "small", "medium", "large"],
        "handle": ["single handle", "no handle", "double-walled"],
        "rim": ["smooth", "thick", "thin"],
        "base": ["flat", "saucer", "stable"],
        "features": ["lid", "insulated", "decorative pattern", "logo"],
        "type": ["coffee cup", "tea cup", "travel mug"],
        "condition": ["empty", "filled", "clean"],
        "expression": ["warm", "inviting", "practical"],
        "Fine-grained classes": ["Coffee Mug", "Tea Cup", "Travel Mug", "Espresso Cup", "Disposable Cup"],
        "similar classes": {
            "wine glass": {
                "distinguished": ["no stem", "handle present", "everyday use"],
                "similar": ["drinking vessel", "holds liquids", "cylindrical"]
            },
            "bowl": {
                "distinguished": ["taller", "handle present", "drinking not eating"],
                "similar": ["holds contents", "rounded shape", "ceramic"]
            },
            "vase": {
                "distinguished": ["smaller", "drinking purpose", "handle"],
                "similar": ["cylindrical", "holds liquids", "ceramic material"]
            }
        }
    },

    "fork": {
        "colors": ["silver", "stainless steel", "gold-colored"],
        "material": ["stainless steel", "silver", "plastic"],
        "tines": ["three tines", "four tines", "pointed"],
        "handle": ["straight", "decorated", "ergonomic"],
        "length": ["short", "standard", "long"],
        "size": ["salad fork", "dinner fork", "dessert fork"],
        "finish": ["polished", "matte", "brushed"],
        "style": ["modern", "traditional", "ornate"],
        "weight": ["lightweight", "heavy-duty"],
        "condition": ["new", "tarnished", "clean"],
        "expression": ["functional", "elegant", "dining"],
        "Fine-grained classes": ["Dinner Fork", "Salad Fork", "Dessert Fork", "Serving Fork", "Carving Fork"],
        "similar classes": {
            "spoon": {
                "distinguished": ["tines instead of bowl", "piercing function", "different shape"],
                "similar": ["utensil", "metal", "used for eating"]
            },
            "knife": {
                "distinguished": ["multiple tines", "no blade", "piercing not cutting"],
                "similar": ["utensil", "metal", "eating tool"]
            },
            "toothbrush": {
                "distinguished": ["metal", "eating utensil", "tines"],
                "similar": ["elongated handle", "pronged/bristled end", "handheld"]
            }
        }
    },

    "knife": {
        "colors": ["silver blade", "black handle", "wooden handle"],
        "blade": ["stainless steel", "sharp", "serrated", "smooth edge"],
        "handle": ["wood", "plastic", "metal", "ergonomic grip"],
        "length": ["short", "medium", "long"],
        "size": ["paring", "utility", "chef's knife"],
        "tip": ["pointed", "rounded"],
        "edge": ["straight", "serrated", "scalloped"],
        "style": ["kitchen knife", "butter knife", "steak knife"],
        "weight": ["lightweight", "heavy", "well-balanced"],
        "condition": ["sharp", "dull", "clean"],
        "expression": ["sharp", "precise", "functional"],
        "Fine-grained classes": ["Chef's Knife", "Paring Knife", "Bread Knife", "Steak Knife", "Butter Knife", "Utility Knife"],
        "similar classes": {
            "fork": {
                "distinguished": ["single blade", "cutting edge", "no tines"],
                "similar": ["utensil", "metal", "eating tool"]
            },
            "scissors": {
                "distinguished": ["single blade", "no finger holes", "simpler design"],
                "similar": ["cutting tool", "sharp blade", "metal"]
            },
            "spoon": {
                "distinguished": ["flat blade", "cutting function", "sharp edge"],
                "similar": ["utensil", "metal handle", "eating tool"]
            }
        }
    },

    "spoon": {
        "colors": ["silver", "stainless steel", "gold-colored"],
        "material": ["stainless steel", "silver", "plastic", "wood"],
        "bowl": ["round", "oval", "deep", "shallow"],
        "handle": ["straight", "decorated", "ergonomic"],
        "length": ["short", "standard", "long"],
        "size": ["teaspoon", "tablespoon", "soup spoon", "serving spoon"],
        "finish": ["polished", "matte", "brushed"],
        "style": ["modern", "traditional", "ornate"],
        "weight": ["lightweight", "heavy"],
        "condition": ["new", "tarnished", "clean"],
        "expression": ["functional", "smooth", "practical"],
        "Fine-grained classes": ["Teaspoon", "Tablespoon", "Soup Spoon", "Dessert Spoon", "Serving Spoon", "Ladle"],
        "similar classes": {
            "fork": {
                "distinguished": ["bowl instead of tines", "scooping function", "rounded end"],
                "similar": ["utensil", "metal", "eating tool"]
            },
            "knife": {
                "distinguished": ["bowl shape", "no cutting edge", "scooping purpose"],
                "similar": ["utensil", "metal handle", "eating tool"]
            },
            "ladle": {
                "distinguished": ["smaller size", "eating utensil", "shorter handle"],
                "similar": ["bowl shape", "scooping function", "metal"]
            }
        }
    },

    "bowl": {
        "colors": ["white", "ceramic colors", "patterned", "wood"],
        "material": ["ceramic", "porcelain", "glass", "wood", "metal"],
        "shape": ["round", "oval", "deep", "shallow"],
        "size": ["small", "medium", "large", "serving size"],
        "rim": ["smooth", "rolled", "wide"],
        "base": ["flat", "footed", "stable"],
        "style": ["soup bowl", "cereal bowl", "mixing bowl", "serving bowl"],
        "features": ["handles", "decorative pattern", "stackable"],
        "condition": ["empty", "filled", "clean"],
        "finish": ["glazed", "matte", "polished"],
        "expression": ["functional", "versatile", "essential"],
        "Fine-grained classes": ["Soup Bowl", "Cereal Bowl", "Mixing Bowl", "Serving Bowl", "Salad Bowl", "Rice Bowl"],
        "similar classes": {
            "cup": {
                "distinguished": ["wider opening", "no handle usually", "eating not drinking"],
                "similar": ["holds food/liquid", "ceramic", "rounded shape"]
            },
            "plate": {
                "distinguished": ["deeper", "holds liquids", "rounded sides"],
                "similar": ["dining ware", "circular shape", "holds food"]
            },
            "vase": {
                "distinguished": ["wider opening", "food use", "shallower"],
                "similar": ["holds contents", "rounded shape", "ceramic"]
            }
        }
    }
}

meta_COCO_info = {**meta_COCO_info_T1, **meta_COCO_info_T2, **meta_COCO_info_T3, **meta_COCO_info_T4}
# ["bird", "bus", "cow", "motorbike", "sofa", ["aeroplane", "bicycle", "boat", "bottle", "car", "cat", "chair", "diningtable", "dog", "horse", "person", "pottedplant", "sheep", "train", "tvmonitor"]

PASCAL_VOC_NOVEL_CATEGORIES = {
    1: ["bird", "bus", "cow", "motorbike", "sofa"],
    2: ["aeroplane", "bottle", "cow", "horse", "sofa"],
    3: ["boat", "cat", "motorbike", "sheep", "sofa"],
}

PASCAL_VOC_BASE_CATEGORIES = {
    1: ["aeroplane", "bicycle", "boat", "bottle", "car",
        "cat", "chair", "diningtable", "dog", "horse",
        "person", "pottedplant", "sheep", "train", "tvmonitor",
        ],
    2: ["bicycle", "bird", "boat", "bus", "car",
        "cat", "chair", "diningtable", "dog", "motorbike",
        "person", "pottedplant", "sheep", "train", "tvmonitor",
        ],
    3: ["aeroplane", "bicycle", "bird", "bottle", "bus",
        "car", "chair", "cow", "diningtable", "dog",
        "horse", "person", "pottedplant", "train", "tvmonitor",
        ],
}

"""" CHAT GPT 
    list up to 20 fine-grained classes for each class in list=["bird", "bus", "cow", "motorbike", "sofa", "aeroplane", 
    "bicycle", "boat", "bottle", "car", "cat", "chair", "diningtable", "dog", "horse", "person", "pottedplant", 
    "sheep", "train", "tvmonitor"], note these fine-grained classes have distinguished appearance features 
    from the remaining classes in list. provide a dictionary in python

"""
voc_fine_grained_classes = {
    "bird": ["sparrow", "eagle", "parrot", "penguin", "owl", "hawk", "falcon", "peacock", "pigeon", "hummingbird",
             "canary", "crow", "duck", "goose", "swallow", "kingfisher", "woodpecker", "macaw", "flamingo", "seagull"],

    "bus": ["school bus", "double-decker bus", "shuttle bus", "minibus", "tourist bus", "coach bus", "city bus",
            "articulated bus", "trolleybus", "van", "airport shuttle", "electric bus", "fuel-cell bus",
            "diesel bus", "hybrid bus", "tram", "charter bus", "party bus", "open-top bus", "prison bus"],

    "cow": ["jersey cow", "holstein cow", "angus cow", "hereford cow", "guernsey cow", "brahman cow",
            "longhorn cow", "brown swiss cow", "ayrshire cow", "milking shorthorn cow", "beefmaster cow",
            "galloway cow", "dexter cow", "belted galloway cow", "zebu cow", "simmental cow", "charolais cow",
            "limousin cow", "wagyu cow", "texas longhorn cow"],

    "motorbike": ["sportbike", "cruiser", "dirt bike", "touring bike", "scooter", "moped", "café racer",
                  "adventure bike", "dual-sport", "naked bike", "chopper", "electric bike", "minibike",
                  "superbike", "motocross bike", "enduro bike", "streetfighter", "off-road bike", "trials bike",
                  "scrambler"],

    "sofa": ["sectional sofa", "chesterfield sofa", "sleeper sofa", "recliner sofa", "loveseat", "futon",
             "cabriole sofa", "chaise lounge", "tuxedo sofa", "divan", "settee", "modular sofa",
             "lawson sofa", "mid-century modern sofa", "english roll arm sofa", "camelback sofa",
             "slipcovered sofa", "convertible sofa", "slope arm sofa", "track arm sofa"],

    "aeroplane": ["commercial jet", "private jet", "fighter jet", "cargo plane", "glider", "biplane",
                  "helicopter", "seaplane", "airliner", "jumbo jet", "propeller plane", "airbus", "boeing",
                  "concorde", "light aircraft", "regional jet", "stealth bomber", "supersonic jet", "turboprop",
                  "drone"],

    "bicycle": ["mountain bike", "road bike", "hybrid bike", "electric bike", "folding bike", "BMX",
                "touring bike", "cruiser bike", "gravel bike", "tandem bike", "cyclocross bike",
                "recumbent bike", "track bike", "fixie bike", "triathlon bike", "cargo bike", "city bike",
                "fat bike", "kids bike", "balance bike"],

    "boat": ["sailboat", "yacht", "fishing boat", "speedboat", "canoe", "kayak", "dinghy", "rowboat",
             "catamaran", "ferry", "pontoon boat", "houseboat", "motorboat", "jet ski", "tugboat", "submarine",
             "cargo ship", "cruise ship", "barge", "raft"],

    "bottle": ["water bottle", "wine bottle", "beer bottle", "soda bottle", "milk bottle", "glass bottle",
               "plastic bottle", "sports bottle", "flask", "baby bottle", "insulated bottle", "thermos",
               "aluminum bottle", "juice bottle", "potion bottle", "oil bottle", "vinegar bottle", "whiskey bottle",
               "tequila bottle", "shampoo bottle"],

    "car": ["sedan", "SUV", "coupe", "convertible", "hatchback", "station wagon", "pickup truck",
            "sports car", "minivan", "crossover", "limousine", "electric car", "hybrid car", "diesel car",
            "luxury car", "compact car", "muscle car", "roadster", "supercar", "off-road vehicle"],

    "cat": ["persian cat", "siamese cat", "maine coon", "ragdoll", "sphynx cat", "bengal cat",
            "british shorthair", "scottish fold", "himalayan cat", "abyssinian cat", "birman cat",
            "oriental shorthair", "turkish van", "devon rex", "egyptian mau", "siberian cat",
            "american shorthair", "savannah cat", "chartreux", "norwegian forest cat"],

    "chair": ["rocking chair", "recliner", "dining chair", "office chair", "armchair", "bar stool",
              "folding chair", "accent chair", "lounge chair", "wingback chair", "slipper chair",
              "chaise lounge", "side chair", "parsons chair", "club chair", "bean bag chair", "director's chair",
              "ottoman", "hammock chair", "butterfly chair"],

    "diningtable": ["round dining table", "rectangular dining table", "square dining table",
                    "oval dining table", "drop-leaf dining table", "extendable dining table",
                    "pedestal dining table", "farmhouse dining table", "glass dining table",
                    "marble dining table", "wooden dining table", "contemporary dining table",
                    "rustic dining table", "modern dining table", "industrial dining table",
                    "mid-century dining table", "parsons dining table", "pub dining table", "counter-height table",
                    "tulip dining table"],

    "dog": ["labrador retriever", "german shepherd", "golden retriever", "bulldog", "beagle", "poodle",
            "rottweiler", "yorkshire terrier", "boxer", "dachshund", "shih tzu", "pomeranian", "border collie",
            "chihuahua", "french bulldog", "great dane", "siberian husky", "doberman pinscher", "pug",
            "cocker spaniel"],

    "horse": ["arabian horse", "thoroughbred", "mustang", "clydesdale", "quarter horse", "shetland pony",
              "friesian horse", "appaloosa", "paint horse", "belgian horse", "morgan horse", "andalusian horse",
              "haflinger horse", "icelandic horse", "lipizzaner horse", "shire horse", "tennessee walker",
              "gypsy vanner", "percheron", "welsh pony"],

    "person": ["adult", "child", "teenager", "elderly person", "woman", "man", "infant", "athlete",
               "student", "worker", "police officer", "doctor", "teacher", "firefighter", "artist",
               "musician", "actor", "dancer", "pilot", "scientist"],

    "pottedplant": ["succulent", "fern", "bonsai tree", "cactus", "orchid", "palm", "ivy",
                    "aloe vera", "snake plant", "peace lily", "philodendron", "rubber plant",
                    "spider plant", "jade plant", "bamboo", "money tree", "fiddle leaf fig",
                    "pothos", "zz plant", "air plant"],

    "sheep": ["merino sheep", "suffolk sheep", "dorper sheep", "dorset sheep", "katahdin sheep",
              "hampshire sheep", "southdown sheep", "jacob sheep", "romney sheep", "barbados blackbelly sheep",
              "texel sheep", "lincoln sheep", "columbia sheep", "cheviot sheep", "corriedale sheep",
              "black welsh mountain sheep", "icelandic sheep", "shropshire sheep", "wensleydale sheep", "tunis sheep"],

    "train": ["bullet train", "freight train", "passenger train", "steam locomotive", "electric train",
              "diesel train", "monorail", "subway train", "light rail", "high-speed rail", "metro train",
              "tram", "cog railway", "maglev train", "tilting train", "cable car", "funicular",
              "commuter train", "long-distance train", "intercity train"],

    "tvmonitor": ["LED TV", "OLED TV", "LCD TV", "plasma TV", "curved TV", "smart TV", "4K TV",
                  "8K TV", "portable TV", "touchscreen monitor", "gaming monitor", "widescreen monitor",
                  "ultrawide monitor", "dual-monitor setup", "projector", "CRT monitor", "flat-screen TV",
                  "desktop monitor", "HDR monitor", "QLED TV"]
}

# To access, just query the dictionary:
# Example: print(fine_grained_classes['dog'])
coco_fine_grained_classes_T1 = {
    "person": ["adult", "child", "teenager", "woman", "man", "baby", "athlete", "doctor", "police officer",
               "firefighter", "student", "worker", "teacher", "musician", "pilot", "chef", "artist",
               "actor", "soldier", "scientist"],

    "bicycle": ["mountain bike", "road bike", "hybrid bike", "electric bike", "BMX", "folding bike",
                "gravel bike", "tandem bike", "cruiser bike", "fixie", "track bike", "cargo bike",
                "racing bike", "fat bike", "cyclocross bike", "recumbent bike", "urban bike",
                "electric cargo bike", "folding e-bike", "kid’s bike"],

    "car": ["sedan", "SUV", "coupe", "convertible", "hatchback", "station wagon", "minivan", "pickup truck",
            "sports car", "electric car", "luxury car", "compact car", "supercar", "muscle car",
            "roadster", "hybrid car", "diesel car", "crossover", "off-road vehicle", "limousine"],

    "motorcycle": ["sportbike", "cruiser", "touring bike", "dirt bike", "scooter", "moped",
                   "adventure bike", "dual-sport", "naked bike", "café racer", "chopper",
                   "minibike", "motocross bike", "enduro bike", "scrambler", "electric motorcycle",
                   "sidecar motorcycle", "trials bike", "rally bike", "flat tracker"],

    "airplane": ["commercial jet", "private jet", "fighter jet", "cargo plane", "helicopter", "glider",
                 "seaplane", "biplane", "airliner", "jumbo jet", "propeller plane", "turboprop",
                 "supersonic jet", "light aircraft", "regional jet", "business jet", "ultralight plane",
                 "electric aircraft", "amphibious aircraft", "concorde"],

    "bus": ["school bus", "double-decker bus", "shuttle bus", "tourist bus", "minibus", "coach bus",
            "city bus", "articulated bus", "trolleybus", "party bus", "airport shuttle", "hybrid bus",
            "fuel-cell bus", "electric bus", "charter bus", "open-top bus", "transit bus",
            "paratransit bus", "tram", "commuter bus"],

    "train": ["bullet train", "freight train", "passenger train", "steam locomotive", "monorail",
              "electric train", "diesel train", "high-speed train", "metro train", "subway",
              "light rail", "intercity train", "regional train", "commuter train", "funicular",
              "tilting train", "tram", "long-distance train", "maglev train", "shinkansen"],

    "boat": ["sailboat", "yacht", "fishing boat", "speedboat", "canoe", "kayak", "dinghy",
             "pontoon boat", "houseboat", "motorboat", "ferry", "jet ski", "catamaran",
             "cargo ship", "cruise ship", "submarine", "tugboat", "barge", "gondola", "rowing boat"],

    "bird": ["sparrow", "eagle", "parrot", "penguin", "owl", "falcon", "peacock", "pigeon",
             "hummingbird", "crow", "canary", "duck", "goose", "swallow", "woodpecker",
             "macaw", "flamingo", "seagull", "kingfisher", "hawk"],

    "cat": ["persian cat", "siamese cat", "maine coon", "ragdoll", "sphynx cat", "bengal cat",
            "british shorthair", "scottish fold", "himalayan cat", "abyssinian cat", "birman cat",
            "oriental shorthair", "devon rex", "siberian cat", "egyptian mau", "turkish angora",
            "korat", "savannah cat", "ragamuffin", "norwegian forest cat"],

    "dog": ["labrador retriever", "german shepherd", "golden retriever", "bulldog", "beagle", "poodle",
            "rottweiler", "yorkshire terrier", "boxer", "shih tzu", "pomeranian", "border collie",
            "chihuahua", "french bulldog", "doberman", "great dane", "siberian husky", "pug",
            "cocker spaniel", "dalmatian"],

    "horse": ["arabian horse", "thoroughbred", "clydesdale", "mustang", "quarter horse",
              "shetland pony", "appaloosa", "friesian", "morgan horse", "andalusian",
              "haflinger", "icelandic horse", "lipizzaner", "shire horse", "belgian draft horse",
              "tennessee walker", "gypsy vanner", "paint horse", "percheron", "welsh pony"],

    "sheep": ["merino sheep", "suffolk sheep", "dorper sheep", "hampshire sheep", "katahdin sheep",
              "southdown sheep", "jacob sheep", "romney sheep", "texel sheep", "cheviot sheep",
              "columbia sheep", "black welsh mountain sheep", "icelandic sheep", "lincoln sheep",
              "corriedale sheep", "wensleydale sheep", "shropshire sheep", "tunis sheep",
              "barbados blackbelly", "dorper sheep"],

    "cow": ["holstein cow", "jersey cow", "angus cow", "hereford cow", "guernsey cow", "brahman cow",
            "longhorn cow", "brown swiss cow", "simmental cow", "ayrshire cow", "charolais cow",
            "limousin cow", "galloway cow", "belted galloway", "dexter cow", "zebu", "beefmaster cow",
            "wagyu cow", "red angus", "brangus"],

    "bottle": ["water bottle", "wine bottle", "beer bottle", "soda bottle", "milk bottle",
               "glass bottle", "plastic bottle", "sports bottle", "baby bottle", "flask",
               "thermos", "insulated bottle", "aluminum bottle", "juice bottle", "potion bottle",
               "oil bottle", "whiskey bottle", "tequila bottle", "vinegar bottle", "shampoo bottle"],

    "chair": ["rocking chair", "recliner", "office chair", "dining chair", "armchair", "lounge chair",
              "bar stool", "folding chair", "accent chair", "wingback chair", "club chair",
              "chaise lounge", "side chair", "parsons chair", "bean bag chair", "deck chair",
              "slipper chair", "butterfly chair", "director's chair", "ottoman"],

    "couch": ["sectional sofa", "sleeper sofa", "loveseat", "recliner sofa", "chaise lounge",
              "chesterfield sofa", "futon", "cabriole sofa", "mid-century modern sofa",
              "slipcovered sofa", "track arm sofa", "tuxedo sofa", "modular sofa", "daybed",
              "convertible sofa", "lawson sofa", "english roll arm sofa", "camelback sofa",
              "chaise sectional", "u-shaped sectional"],

    "potted plant": ["succulent", "fern", "bonsai tree", "cactus", "palm", "orchid",
                     "ivy", "snake plant", "aloe vera", "philodendron", "peace lily",
                     "rubber plant", "spider plant", "jade plant", "money tree",
                     "fiddle leaf fig", "bamboo plant", "pothos", "air plant", "zz plant"],

    "dining table": ["round dining table", "rectangular dining table", "square dining table",
                     "oval dining table", "drop-leaf table", "extendable table", "pedestal table",
                     "glass dining table", "wooden dining table", "contemporary dining table",
                     "farmhouse dining table", "industrial dining table", "mid-century dining table",
                     "rustic dining table", "marble dining table", "modern dining table",
                     "pub table", "counter-height table", "tulip dining table", "parsons table"],

    "tv": ["LED TV", "OLED TV", "LCD TV", "plasma TV", "smart TV", "curved TV", "4K TV",
           "8K TV", "flat-screen TV", "touchscreen monitor", "widescreen monitor",
           "projector", "HDR TV", "QLED TV", "portable TV", "gaming monitor", "CRT TV",
           "dual-monitor setup", "wall-mounted TV", "home theater screen"]
}

coco_fine_grained_classes_T2 = {
    "truck": ["pickup truck", "dump truck", "box truck", "semi-truck", "tow truck", "flatbed truck",
              "garbage truck", "fire truck", "delivery truck", "panel truck", "monster truck",
              "cement mixer truck", "tanker truck", "refrigerated truck", "moving truck",
              "logging truck", "food truck", "armored truck", "utility truck", "wrecker truck"],

    "traffic light": ["pedestrian signal", "vehicle signal", "arrow signal", "countdown signal",
                      "bicycle signal", "railway crossing signal", "flashing beacon", "LED signal",
                      "overhead signal", "post-mounted signal", "pedestrian crossing signal",
                      "smart traffic light", "solar-powered signal", "three-light signal",
                      "four-way signal", "emergency vehicle signal", "bus signal priority",
                      "tram signal", "variable message signal", "school zone signal"],

    "fire hydrant": ["wet barrel hydrant", "dry barrel hydrant", "flush hydrant", "pillar hydrant",
                     "post hydrant", "wall hydrant", "standpipe hydrant", "underground hydrant",
                     "above-ground hydrant", "pressure hydrant", "yard hydrant", "street hydrant",
                     "park hydrant", "industrial hydrant", "marine hydrant", "airport hydrant",
                     "rural hydrant", "urban hydrant", "painted hydrant", "vintage hydrant"],

    "stop sign": ["standard stop sign", "all-way stop", "multi-way stop", "school zone stop",
                  "four-way stop", "three-way stop", "rolling stop sign", "octagonal stop sign",
                  "reflective stop sign", "oversized stop sign", "pedestrian stop sign",
                  "temporary stop sign", "construction stop sign", "flashing stop sign",
                  "bilingual stop sign", "digital stop sign", "led-enhanced stop sign",
                  "high-visibility stop sign", "rural stop sign", "urban stop sign"],

    "parking meter": ["single-space meter", "multi-space meter", "smart meter", "solar meter",
                      "digital parking meter", "coin-operated meter", "pay-and-display meter",
                      "app-enabled meter", "touchscreen meter", "credit card meter",
                      "mechanical meter", "electronic meter", "wireless meter", "networked meter",
                      "pay station", "parking kiosk", "curbside meter", "garage meter",
                      "street parking meter", "time-limited meter"],

    "bench": ["park bench", "garden bench", "memorial bench", "transit bench", "picnic bench",
              "wooden bench", "metal bench", "concrete bench", "stone bench", "plastic bench",
              "backless bench", "curved bench", "straight bench", "bus stop bench", "plaza bench",
              "outdoor bench", "indoor bench", "decorative bench", "storage bench", "church pew"],

    "elephant": ["african elephant", "asian elephant", "forest elephant", "savanna elephant",
                 "bull elephant", "cow elephant", "baby elephant", "african bush elephant",
                 "african forest elephant", "indian elephant", "sri lankan elephant",
                 "sumatran elephant", "borneo elephant", "wild elephant", "captive elephant",
                 "circus elephant", "zoo elephant", "working elephant", "temple elephant",
                 "tusker elephant"],

    "bear": ["grizzly bear", "black bear", "polar bear", "brown bear", "panda bear",
             "kodiak bear", "sun bear", "sloth bear", "spectacled bear", "asiatic black bear",
             "american black bear", "eurasian brown bear", "giant panda", "red panda",
             "kermode bear", "cinnamon bear", "glacier bear", "golden bear", "himalayan bear",
             "syrian brown bear"],

    "zebra": ["plains zebra", "mountain zebra", "grevy's zebra", "burchell's zebra",
              "grant's zebra", "chapman's zebra", "crawshay's zebra", "hartmann's mountain zebra",
              "cape mountain zebra", "common zebra", "wild zebra", "young zebra", "adult zebra",
              "male zebra", "female zebra", "zebra foal", "savanna zebra", "quagga (extinct)",
              "hybrid zebra", "captive zebra"],

    "giraffe": ["masai giraffe", "reticulated giraffe", "northern giraffe", "southern giraffe",
                "rothschild's giraffe", "kordofan giraffe", "nubian giraffe", "west african giraffe",
                "angolan giraffe", "south african giraffe", "thornicroft's giraffe", "bull giraffe",
                "cow giraffe", "baby giraffe", "young giraffe", "adult giraffe", "wild giraffe",
                "zoo giraffe", "tall giraffe", "savanna giraffe"],

    "backpack": ["school backpack", "hiking backpack", "laptop backpack", "military backpack",
                 "daypack", "travel backpack", "camera backpack", "hydration backpack",
                 "tactical backpack", "rucksack", "messenger backpack", "rolling backpack",
                 "ultralight backpack", "frame backpack", "frameless backpack", "technical backpack",
                 "urban backpack", "cycling backpack", "ski backpack", "climbing backpack"],

    "umbrella": ["compact umbrella", "golf umbrella", "beach umbrella", "patio umbrella",
                 "automatic umbrella", "manual umbrella", "inverted umbrella", "transparent umbrella",
                 "windproof umbrella", "travel umbrella", "folding umbrella", "stick umbrella",
                 "parasol", "sun umbrella", "rain umbrella", "market umbrella", "cantilever umbrella",
                 "offset umbrella", "children's umbrella", "designer umbrella"],

    "handbag": ["tote bag", "shoulder bag", "clutch", "crossbody bag", "hobo bag",
                "satchel", "bucket bag", "saddle bag", "messenger bag", "wristlet",
                "evening bag", "bowling bag", "doctor bag", "barrel bag", "half-moon bag",
                "frame bag", "drawstring bag", "baguette bag", "top-handle bag", "mini bag"],

    "tie": ["necktie", "bow tie", "ascot", "bolo tie", "skinny tie", "wide tie",
            "silk tie", "knit tie", "wool tie", "polyester tie", "patterned tie",
            "solid tie", "striped tie", "paisley tie", "polka dot tie", "plaid tie",
            "novelty tie", "clip-on tie", "pre-tied bow tie", "self-tie bow tie"],

    "suitcase": ["carry-on luggage", "checked luggage", "rolling suitcase", "hard shell case",
                 "soft shell case", "spinner suitcase", "two-wheel suitcase", "duffel bag",
                 "garment bag", "trunk", "expandable suitcase", "lightweight suitcase",
                 "aluminum suitcase", "polycarbonate suitcase", "vintage suitcase",
                 "travel case", "cabin bag", "large suitcase", "medium suitcase", "small suitcase"],

    "microwave": ["countertop microwave", "over-the-range microwave", "built-in microwave",
                  "convection microwave", "solo microwave", "grill microwave", "combination microwave",
                  "compact microwave", "standard microwave", "large capacity microwave",
                  "smart microwave", "inverter microwave", "sensor microwave", "digital microwave",
                  "dial microwave", "commercial microwave", "residential microwave",
                  "stainless steel microwave", "white microwave", "black microwave"],

    "oven": ["gas oven", "electric oven", "convection oven", "double oven", "wall oven",
             "range oven", "steam oven", "combi-steam oven", "toaster oven", "commercial oven",
             "home oven", "built-in oven", "freestanding oven", "slide-in oven", "pizza oven",
             "brick oven", "self-cleaning oven", "smart oven", "conventional oven", "microwave oven combo"],

    "toaster": ["pop-up toaster", "toaster oven", "long slot toaster", "four slice toaster",
                "two slice toaster", "single slice toaster", "bagel toaster", "wide slot toaster",
                "digital toaster", "manual toaster", "stainless steel toaster", "chrome toaster",
                "retro toaster", "modern toaster", "compact toaster", "conveyor toaster",
                "commercial toaster", "home toaster", "smart toaster", "countdown toaster"],

    "sink": ["kitchen sink", "bathroom sink", "utility sink", "farmhouse sink", "vessel sink",
             "undermount sink", "top-mount sink", "drop-in sink", "pedestal sink", "wall-mount sink",
             "double bowl sink", "single bowl sink", "triple bowl sink", "bar sink", "prep sink",
             "laundry sink", "apron-front sink", "integrated sink", "corner sink", "island sink"],

    "refrigerator": ["top-freezer refrigerator", "bottom-freezer refrigerator", "side-by-side refrigerator",
                     "french door refrigerator", "mini fridge", "compact refrigerator", "counter-depth refrigerator",
                     "built-in refrigerator", "freestanding refrigerator", "smart refrigerator",
                     "wine refrigerator", "beverage refrigerator", "commercial refrigerator",
                     "residential refrigerator", "retro refrigerator", "stainless steel refrigerator",
                     "black refrigerator", "white refrigerator", "panel-ready refrigerator", "energy-efficient refrigerator"]
}

coco_fine_grained_classes_T3 = {
    "frisbee": ["ultimate frisbee", "disc golf disc", "freestyle disc", "dog frisbee", "beach frisbee",
                "glow disc", "putter disc", "mid-range disc", "driver disc", "mini frisbee",
                "competition frisbee", "recreational frisbee", "professional disc", "lightweight disc",
                "heavyweight disc", "floating disc", "aerodynamic disc", "trick disc",
                "tournament disc", "practice disc"],

    "skis": ["downhill skis", "cross-country skis", "freestyle skis", "touring skis", "powder skis",
             "racing skis", "backcountry skis", "all-mountain skis", "carving skis", "mogul skis",
             "twin-tip skis", "telemark skis", "ski jumping skis", "slalom skis", "giant slalom skis",
             "super-g skis", "alpine skis", "nordic skis", "freeride skis", "park skis"],

    "snowboard": ["freestyle snowboard", "freeride snowboard", "all-mountain snowboard", "powder snowboard",
                  "split board", "alpine snowboard", "jib board", "park snowboard", "backcountry snowboard",
                  "carving snowboard", "women's snowboard", "men's snowboard", "youth snowboard",
                  "wide snowboard", "directional snowboard", "twin-tip snowboard", "hybrid camber board",
                  "rocker snowboard", "camber snowboard", "beginner snowboard"],

    "sports ball": ["soccer ball", "basketball", "volleyball", "tennis ball", "baseball",
                    "football", "golf ball", "rugby ball", "cricket ball", "bowling ball",
                    "softball", "beach ball", "handball", "racquetball", "squash ball",
                    "medicine ball", "dodge ball", "kickball", "lacrosse ball", "polo ball"],

    "kite": ["diamond kite", "delta kite", "box kite", "stunt kite", "parafoil kite",
             "dragon kite", "cellular kite", "sled kite", "rokkaku kite", "tetrahedral kite",
             "single-line kite", "dual-line kite", "quad-line kite", "power kite", "foil kite",
             "fighter kite", "train kite", "windsock kite", "indoor kite", "outdoor kite"],

    "baseball bat": ["wood bat", "aluminum bat", "composite bat", "youth bat", "adult bat",
                     "softball bat", "training bat", "fungo bat", "tee ball bat", "little league bat",
                     "professional bat", "amateur bat", "maple bat", "ash bat", "birch bat",
                     "bamboo bat", "metal bat", "alloy bat", "slowpitch bat", "fastpitch bat"],

    "baseball glove": ["catcher's mitt", "first base glove", "infield glove", "outfield glove",
                       "pitcher's glove", "youth glove", "adult glove", "professional glove",
                       "recreational glove", "training glove", "fastpitch glove", "slowpitch glove",
                       "left-handed glove", "right-handed glove", "leather glove", "synthetic glove",
                       "web glove", "closed web glove", "open web glove", "basket web glove"],

    "skateboard": ["street skateboard", "longboard", "cruiser", "penny board", "electric skateboard",
                   "vert skateboard", "downhill skateboard", "freestyle skateboard", "slalom skateboard",
                   "trick board", "pool skateboard", "mini cruiser", "complete skateboard",
                   "custom skateboard", "pro skateboard", "beginner skateboard", "children's skateboard",
                   "dancing longboard", "carving board", "commuter skateboard"],

    "surfboard": ["shortboard", "longboard", "fish board", "funboard", "gun surfboard",
                  "stand-up paddleboard", "hybrid surfboard", "mini mal", "malibu board",
                  "performance shortboard", "step-up board", "retro fish", "twin fin",
                  "thruster", "quad fin", "single fin", "beginner board", "intermediate board",
                  "advanced board", "foam board"],

    "tennis racket": ["power racket", "control racket", "tweener racket", "junior racket",
                      "professional racket", "beginner racket", "intermediate racket", "advanced racket",
                      "oversized racket", "midsize racket", "standard racket", "extended length racket",
                      "lightweight racket", "heavyweight racket", "graphite racket", "aluminum racket",
                      "composite racket", "pre-strung racket", "unstrung racket", "demo racket"],

    "banana": ["cavendish banana", "plantain", "lady finger banana", "red banana", "burro banana",
               "manzano banana", "baby banana", "blue java banana", "pisang raja", "apple banana",
               "cooking banana", "dessert banana", "green banana", "ripe banana", "overripe banana",
               "organic banana", "fair trade banana", "tropical banana", "sweet banana", "starchy banana"],

    "apple": ["red delicious", "granny smith", "fuji apple", "gala apple", "honeycrisp apple",
              "golden delicious", "pink lady", "braeburn apple", "mcintosh apple", "jazz apple",
              "ambrosia apple", "cosmic crisp", "envy apple", "jonagold apple", "cortland apple",
              "empire apple", "idared apple", "mutsu apple", "northern spy", "winesap apple"],

    "sandwich": ["club sandwich", "blt sandwich", "grilled cheese", "submarine sandwich", "panini",
                 "open-faced sandwich", "wrap", "hoagie", "po' boy", "reuben sandwich",
                 "monte cristo", "croque monsieur", "bánh mì", "gyro", "pita sandwich",
                 "bagel sandwich", "breakfast sandwich", "deli sandwich", "pulled pork sandwich",
                 "chicken sandwich"],

    "orange": ["navel orange", "valencia orange", "blood orange", "mandarin orange", "tangerine",
               "clementine", "satsuma", "cara cara orange", "jaffa orange", "seville orange",
               "bergamot orange", "bitter orange", "sweet orange", "seedless orange", "juice orange",
               "organic orange", "florida orange", "california orange", "tropical orange", "winter orange"],

    "broccoli": ["calabrese broccoli", "sprouting broccoli", "purple broccoli", "broccolini",
                 "romanesco broccoli", "chinese broccoli", "broccoli rabe", "baby broccoli",
                 "crown broccoli", "gai lan", "tenderstem broccoli", "organic broccoli",
                 "frozen broccoli", "fresh broccoli", "steamed broccoli", "raw broccoli",
                 "roasted broccoli", "broccoli florets", "broccoli stalks", "winter broccoli"],

    "carrot": ["imperator carrot", "danvers carrot", "chantenay carrot", "nantes carrot",
               "baby carrot", "purple carrot", "white carrot", "yellow carrot", "orange carrot",
               "red carrot", "organic carrot", "wild carrot", "young carrot", "mature carrot",
               "mini carrot", "heirloom carrot", "rainbow carrot", "garden carrot",
               "storage carrot", "fresh carrot"],

    "hot dog": ["classic hot dog", "chicago dog", "chili dog", "corn dog", "bratwurst",
                "polish sausage", "italian sausage", "foot-long hot dog", "mini hot dog",
                "veggie dog", "turkey dog", "beef hot dog", "pork hot dog", "chicken hot dog",
                "loaded hot dog", "new york hot dog", "coney dog", "slaw dog", "danger dog",
                "bacon-wrapped hot dog"],

    "pizza": ["margherita pizza", "pepperoni pizza", "hawaiian pizza", "meat lovers pizza",
              "veggie pizza", "deep dish pizza", "thin crust pizza", "stuffed crust pizza",
              "neapolitan pizza", "new york style pizza", "chicago style pizza", "sicilian pizza",
              "greek pizza", "detroit style pizza", "california pizza", "flatbread pizza",
              "white pizza", "bbq chicken pizza", "four cheese pizza", "supreme pizza"],

    "donut": ["glazed donut", "jelly donut", "chocolate donut", "old-fashioned donut",
              "cruller", "boston cream donut", "powdered donut", "filled donut", "cake donut",
              "yeast donut", "french cruller", "apple fritter", "bear claw", "maple bar",
              "twist donut", "long john", "donut hole", "vegan donut", "gourmet donut",
              "mini donut"],

    "cake": ["birthday cake", "wedding cake", "chocolate cake", "cheesecake", "layer cake",
             "bundt cake", "sheet cake", "cupcake", "pound cake", "sponge cake",
             "carrot cake", "red velvet cake", "fruitcake", "upside-down cake", "angel food cake",
             "devil's food cake", "marble cake", "coffee cake", "ice cream cake", "tiered cake"]
}

coco_fine_grained_classes_T4 = {
    "bed": ["platform bed", "sleigh bed", "canopy bed", "murphy bed", "bunk bed",
            "adjustable bed", "four-poster bed", "daybed", "trundle bed", "waterbed",
            "panel bed", "storage bed", "captain's bed", "loft bed", "futon bed",
            "divan bed", "ottoman bed", "sofa bed", "brass bed", "wooden bed"],

    "toilet": ["two-piece toilet", "one-piece toilet", "wall-mounted toilet", "smart toilet",
               "bidet toilet", "dual-flush toilet", "composting toilet", "portable toilet",
               "squat toilet", "tankless toilet", "pressure-assisted toilet", "gravity-fed toilet",
               "comfort height toilet", "standard height toilet", "elongated toilet", "round toilet",
               "eco-friendly toilet", "low-flow toilet", "water-saving toilet", "modern toilet"],

    "laptop": ["ultrabook", "gaming laptop", "business laptop", "2-in-1 convertible", "chromebook",
               "macbook", "windows laptop", "linux laptop", "budget laptop", "premium laptop",
               "student laptop", "workstation laptop", "thin and light laptop", "desktop replacement",
               "netbook", "touchscreen laptop", "detachable laptop", "rugged laptop",
               "creator laptop", "enterprise laptop"],

    "mouse": ["wireless mouse", "gaming mouse", "ergonomic mouse", "trackball mouse", "vertical mouse",
              "wired mouse", "bluetooth mouse", "optical mouse", "laser mouse", "travel mouse",
              "ambidextrous mouse", "left-handed mouse", "right-handed mouse", "programmable mouse",
              "silent mouse", "compact mouse", "full-size mouse", "rgb mouse", "office mouse",
              "presentation mouse"],

    "remote": ["tv remote", "universal remote", "streaming remote", "smart remote", "voice remote",
               "learning remote", "rf remote", "infrared remote", "bluetooth remote", "cable box remote",
               "satellite remote", "dvd remote", "blu-ray remote", "projector remote", "soundbar remote",
               "air conditioner remote", "fan remote", "garage door remote", "toy remote", "drone remote"],

    "keyboard": ["mechanical keyboard", "membrane keyboard", "ergonomic keyboard", "gaming keyboard",
                 "wireless keyboard", "bluetooth keyboard", "wired keyboard", "compact keyboard",
                 "full-size keyboard", "tenkeyless keyboard", "60% keyboard", "split keyboard",
                 "backlit keyboard", "rgb keyboard", "chiclet keyboard", "scissor-switch keyboard",
                 "laptop keyboard", "desktop keyboard", "portable keyboard", "folding keyboard"],

    "cell phone": ["smartphone", "iphone", "android phone", "flip phone", "folding phone",
                   "feature phone", "phablet", "budget phone", "flagship phone", "mid-range phone",
                   "gaming phone", "camera phone", "rugged phone", "business phone", "5g phone",
                   "unlocked phone", "carrier phone", "dual-sim phone", "waterproof phone",
                   "compact phone"],

    "book": ["hardcover book", "paperback book", "textbook", "novel", "comic book",
             "magazine", "encyclopedia", "dictionary", "cookbook", "biography",
             "autobiography", "non-fiction book", "fiction book", "children's book", "young adult book",
             "graphic novel", "coffee table book", "reference book", "anthology", "journal"],

    "clock": ["wall clock", "alarm clock", "grandfather clock", "digital clock", "analog clock",
              "cuckoo clock", "atomic clock", "mantel clock", "desk clock", "travel clock",
              "pendulum clock", "anniversary clock", "skeleton clock", "world clock", "projection clock",
              "smart clock", "radio clock", "flip clock", "silent clock", "decorative clock"],

    "vase": ["flower vase", "decorative vase", "bud vase", "floor vase", "ceramic vase",
             "glass vase", "crystal vase", "porcelain vase", "antique vase", "modern vase",
             "tall vase", "short vase", "cylindrical vase", "bulbous vase", "narrow vase",
             "wide vase", "painted vase", "minimalist vase", "ornate vase", "contemporary vase"],

    "scissors": ["office scissors", "kitchen shears", "craft scissors", "pinking shears",
                 "medical scissors", "hair cutting scissors", "fabric scissors", "paper scissors",
                 "children's scissors", "left-handed scissors", "right-handed scissors",
                 "spring-loaded scissors", "ergonomic scissors", "titanium scissors", "stainless steel scissors",
                 "embroidery scissors", "pruning shears", "tailor scissors", "utility scissors",
                 "safety scissors"],

    "teddy bear": ["classic teddy bear", "plush bear", "build-a-bear", "vintage bear", "character bear",
                   "stuffed bear", "antique teddy bear", "collectible bear", "giant teddy bear",
                   "mini teddy bear", "jointed bear", "mohair bear", "fleece bear", "chenille bear",
                   "cuddle bear", "baby's first bear", "graduation bear", "holiday bear",
                   "personalized bear", "handmade bear"],

    "hair drier": ["professional hair dryer", "travel hair dryer", "ionic hair dryer", "ceramic hair dryer",
                   "tourmaline hair dryer", "infrared hair dryer", "blow dryer", "salon dryer",
                   "compact dryer", "folding dryer", "cordless dryer", "wall-mounted dryer",
                   "bonnet dryer", "hooded dryer", "diffuser dryer", "concentrator dryer",
                   "quiet hair dryer", "fast-drying dryer", "cool shot dryer", "dual voltage dryer"],

    "toothbrush": ["manual toothbrush", "electric toothbrush", "battery toothbrush", "kids toothbrush",
                   "travel toothbrush", "soft bristle toothbrush", "medium bristle toothbrush",
                   "hard bristle toothbrush", "sonic toothbrush", "rotating toothbrush",
                   "oscillating toothbrush", "charcoal toothbrush", "bamboo toothbrush",
                   "disposable toothbrush", "folding toothbrush", "orthodontic toothbrush",
                   "gum care toothbrush", "whitening toothbrush", "sensitive toothbrush",
                   "angled toothbrush"],

    "wine glass": ["red wine glass", "white wine glass", "champagne flute", "champagne coupe",
                   "port glass", "dessert wine glass", "bordeaux glass", "burgundy glass",
                   "stemless wine glass", "crystal wine glass", "balloon glass", "tulip glass",
                   "iso tasting glass", "oversized wine glass", "rosé glass", "sparkling wine glass",
                   "vintage wine glass", "modern wine glass", "etched wine glass", "colored wine glass"],

    "cup": ["coffee mug", "tea cup", "travel mug", "espresso cup", "disposable cup",
            "paper cup", "plastic cup", "ceramic cup", "porcelain cup", "glass cup",
            "insulated cup", "thermal cup", "sippy cup", "measuring cup", "collapsible cup",
            "cappuccino cup", "latte cup", "demitasse cup", "tumbler cup", "handled cup"],

    "fork": ["dinner fork", "salad fork", "dessert fork", "serving fork", "carving fork",
             "cocktail fork", "oyster fork", "pastry fork", "fondue fork", "pickle fork",
             "fish fork", "cake fork", "three-tine fork", "four-tine fork", "stainless steel fork",
             "silver fork", "plastic fork", "wooden fork", "disposable fork", "reusable fork"],

    "knife": ["chef's knife", "paring knife", "bread knife", "steak knife", "butter knife",
              "utility knife", "carving knife", "boning knife", "fillet knife", "santoku knife",
              "cleaver", "serrated knife", "table knife", "dinner knife", "pocket knife",
              "kitchen knife", "hunting knife", "survival knife", "ceramic knife", "steel knife"],

    "spoon": ["teaspoon", "tablespoon", "soup spoon", "dessert spoon", "serving spoon",
              "ladle", "slotted spoon", "wooden spoon", "metal spoon", "plastic spoon",
              "measuring spoon", "baby spoon", "demitasse spoon", "iced tea spoon", "grapefruit spoon",
              "caviar spoon", "stirring spoon", "long-handled spoon", "disposable spoon", "silver spoon"],

    "bowl": ["soup bowl", "cereal bowl", "mixing bowl", "serving bowl", "salad bowl",
             "rice bowl", "noodle bowl", "ramen bowl", "pasta bowl", "fruit bowl",
             "popcorn bowl", "pet bowl", "decorative bowl", "ceramic bowl", "glass bowl",
             "wooden bowl", "metal bowl", "plastic bowl", "large bowl", "small bowl"]
}
# Example: print(fine_grained_classes['dog'])
coco_fine_grained_classes = {**coco_fine_grained_classes_T1, **coco_fine_grained_classes_T2, **coco_fine_grained_classes_T3, **coco_fine_grained_classes_T4}

COCO_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicycle"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "car"},
    {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcycle"},
    {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "airplane"},
    {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "bus"},
    {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "train"},
    {"color": [0, 0, 70], "isthing": 1, "id": 8, "name": "truck"},
    {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "boat"},
    {"color": [250, 170, 30], "isthing": 1, "id": 10, "name": "traffic light"},
    {"color": [100, 170, 30], "isthing": 1, "id": 11, "name": "fire hydrant"},
    {"color": [220, 220, 0], "isthing": 1, "id": 13, "name": "stop sign"},
    {"color": [175, 116, 175], "isthing": 1,
     "id": 14, "name": "parking meter", },
    {"color": [250, 0, 30], "isthing": 1, "id": 15, "name": "bench"},
    {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "bird"},
    {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "cat"},
    {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "dog"},
    {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "horse"},
    {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sheep"},
    {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cow"},
    {"color": [110, 76, 0], "isthing": 1, "id": 22, "name": "elephant"},
    {"color": [174, 57, 255], "isthing": 1, "id": 23, "name": "bear"},
    {"color": [199, 100, 0], "isthing": 1, "id": 24, "name": "zebra"},
    {"color": [72, 0, 118], "isthing": 1, "id": 25, "name": "giraffe"},
    {"color": [255, 179, 240], "isthing": 1, "id": 27, "name": "backpack"},
    {"color": [0, 125, 92], "isthing": 1, "id": 28, "name": "umbrella"},
    {"color": [209, 0, 151], "isthing": 1, "id": 31, "name": "handbag"},
    {"color": [188, 208, 182], "isthing": 1, "id": 32, "name": "tie"},
    {"color": [0, 220, 176], "isthing": 1, "id": 33, "name": "suitcase"},
    {"color": [255, 99, 164], "isthing": 1, "id": 34, "name": "frisbee"},
    {"color": [92, 0, 73], "isthing": 1, "id": 35, "name": "skis"},
    {"color": [133, 129, 255], "isthing": 1, "id": 36, "name": "snowboard"},
    {"color": [78, 180, 255], "isthing": 1, "id": 37, "name": "sports ball"},
    {"color": [0, 228, 0], "isthing": 1, "id": 38, "name": "kite"},
    {"color": [174, 255, 243], "isthing": 1, "id": 39, "name": "baseball bat"},
    {"color": [45, 89, 255], "isthing": 1, "id": 40, "name": "baseball glove"},
    {"color": [134, 134, 103], "isthing": 1, "id": 41, "name": "skateboard"},
    {"color": [145, 148, 174], "isthing": 1, "id": 42, "name": "surfboard"},
    {"color": [255, 208, 186], "isthing": 1,
     "id": 43, "name": "tennis racket", },
    {"color": [197, 226, 255], "isthing": 1, "id": 44, "name": "bottle"},
    {"color": [171, 134, 1], "isthing": 1, "id": 46, "name": "wine glass"},
    {"color": [109, 63, 54], "isthing": 1, "id": 47, "name": "cup"},
    {"color": [207, 138, 255], "isthing": 1, "id": 48, "name": "fork"},
    {"color": [151, 0, 95], "isthing": 1, "id": 49, "name": "knife"},
    {"color": [9, 80, 61], "isthing": 1, "id": 50, "name": "spoon"},
    {"color": [84, 105, 51], "isthing": 1, "id": 51, "name": "bowl"},
    {"color": [74, 65, 105], "isthing": 1, "id": 52, "name": "banana"},
    {"color": [166, 196, 102], "isthing": 1, "id": 53, "name": "apple"},
    {"color": [208, 195, 210], "isthing": 1, "id": 54, "name": "sandwich"},
    {"color": [255, 109, 65], "isthing": 1, "id": 55, "name": "orange"},
    {"color": [0, 143, 149], "isthing": 1, "id": 56, "name": "broccoli"},
    {"color": [179, 0, 194], "isthing": 1, "id": 57, "name": "carrot"},
    {"color": [209, 99, 106], "isthing": 1, "id": 58, "name": "hot dog"},
    {"color": [5, 121, 0], "isthing": 1, "id": 59, "name": "pizza"},
    {"color": [227, 255, 205], "isthing": 1, "id": 60, "name": "donut"},
    {"color": [147, 186, 208], "isthing": 1, "id": 61, "name": "cake"},
    {"color": [153, 69, 1], "isthing": 1, "id": 62, "name": "chair"},
    {"color": [3, 95, 161], "isthing": 1, "id": 63, "name": "couch"},
    {"color": [163, 255, 0], "isthing": 1, "id": 64, "name": "potted plant"},
    {"color": [119, 0, 170], "isthing": 1, "id": 65, "name": "bed"},
    {"color": [0, 182, 199], "isthing": 1, "id": 67, "name": "dining table"},
    {"color": [0, 165, 120], "isthing": 1, "id": 70, "name": "toilet"},
    {"color": [183, 130, 88], "isthing": 1, "id": 72, "name": "tv"},
    {"color": [95, 32, 0], "isthing": 1, "id": 73, "name": "laptop"},
    {"color": [130, 114, 135], "isthing": 1, "id": 74, "name": "mouse"},
    {"color": [110, 129, 133], "isthing": 1, "id": 75, "name": "remote"},
    {"color": [166, 74, 118], "isthing": 1, "id": 76, "name": "keyboard"},
    {"color": [219, 142, 185], "isthing": 1, "id": 77, "name": "cell phone"},
    {"color": [79, 210, 114], "isthing": 1, "id": 78, "name": "microwave"},
    {"color": [178, 90, 62], "isthing": 1, "id": 79, "name": "oven"},
    {"color": [65, 70, 15], "isthing": 1, "id": 80, "name": "toaster"},
    {"color": [127, 167, 115], "isthing": 1, "id": 81, "name": "sink"},
    {"color": [59, 105, 106], "isthing": 1, "id": 82, "name": "refrigerator"},
    {"color": [142, 108, 45], "isthing": 1, "id": 84, "name": "book"},
    {"color": [196, 172, 0], "isthing": 1, "id": 85, "name": "clock"},
    {"color": [95, 54, 80], "isthing": 1, "id": 86, "name": "vase"},
    {"color": [128, 76, 255], "isthing": 1, "id": 87, "name": "scissors"},
    {"color": [201, 57, 1], "isthing": 1, "id": 88, "name": "teddy bear"},
    {"color": [246, 0, 122], "isthing": 1, "id": 89, "name": "hair drier"},
    {"color": [191, 162, 208], "isthing": 1, "id": 90, "name": "toothbrush"},
    {"color": [255, 255, 128], "isthing": 0, "id": 92, "name": "banner"},
    {"color": [147, 211, 203], "isthing": 0, "id": 93, "name": "blanket"},
    {"color": [150, 100, 100], "isthing": 0, "id": 95, "name": "bridge"},
    {"color": [168, 171, 172], "isthing": 0, "id": 100, "name": "cardboard"},
    {"color": [146, 112, 198], "isthing": 0, "id": 107, "name": "counter"},
    {"color": [210, 170, 100], "isthing": 0, "id": 109, "name": "curtain"},
    {"color": [92, 136, 89], "isthing": 0, "id": 112, "name": "door-stuff"},
    {"color": [218, 88, 184], "isthing": 0, "id": 118, "name": "floor-wood"},
    {"color": [241, 129, 0], "isthing": 0, "id": 119, "name": "flower"},
    {"color": [217, 17, 255], "isthing": 0, "id": 122, "name": "fruit"},
    {"color": [124, 74, 181], "isthing": 0, "id": 125, "name": "gravel"},
    {"color": [70, 70, 70], "isthing": 0, "id": 128, "name": "house"},
    {"color": [255, 228, 255], "isthing": 0, "id": 130, "name": "light"},
    {"color": [154, 208, 0], "isthing": 0, "id": 133, "name": "mirror-stuff"},
    {"color": [193, 0, 92], "isthing": 0, "id": 138, "name": "net"},
    {"color": [76, 91, 113], "isthing": 0, "id": 141, "name": "pillow"},
    {"color": [255, 180, 195], "isthing": 0, "id": 144, "name": "platform"},
    {"color": [106, 154, 176], "isthing": 0,
     "id": 145, "name": "playingfield"},
    {"color": [230, 150, 140], "isthing": 0, "id": 147, "name": "railroad"},
    {"color": [60, 143, 255], "isthing": 0, "id": 148, "name": "river"},
    {"color": [128, 64, 128], "isthing": 0, "id": 149, "name": "road"},
    {"color": [92, 82, 55], "isthing": 0, "id": 151, "name": "roof"},
    {"color": [254, 212, 124], "isthing": 0, "id": 154, "name": "sand"},
    {"color": [73, 77, 174], "isthing": 0, "id": 155, "name": "sea"},
    {"color": [255, 160, 98], "isthing": 0, "id": 156, "name": "shelf"},
    {"color": [255, 255, 255], "isthing": 0, "id": 159, "name": "snow"},
    {"color": [104, 84, 109], "isthing": 0, "id": 161, "name": "stairs"},
    {"color": [169, 164, 131], "isthing": 0, "id": 166, "name": "tent"},
    {"color": [225, 199, 255], "isthing": 0, "id": 168, "name": "towel"},
    {"color": [137, 54, 74], "isthing": 0, "id": 171, "name": "wall-brick"},
    {"color": [135, 158, 223], "isthing": 0, "id": 175, "name": "wall-stone"},
    {"color": [7, 246, 231], "isthing": 0, "id": 176, "name": "wall-tile"},
    {"color": [107, 255, 200], "isthing": 0, "id": 177, "name": "wall-wood"},
    {"color": [58, 41, 149], "isthing": 0, "id": 178, "name": "water-other"},
    {"color": [183, 121, 142], "isthing": 0,
     "id": 180, "name": "window-blind"},
    {"color": [255, 73, 97], "isthing": 0, "id": 181, "name": "window-other"},
    {"color": [107, 142, 35], "isthing": 0, "id": 184, "name": "tree-merged"},
    {"color": [190, 153, 153], "isthing": 0,
     "id": 185, "name": "fence-merged"},
    {"color": [146, 139, 141], "isthing": 0,
     "id": 186, "name": "ceiling-merged"},
    {"color": [70, 130, 180], "isthing": 0,
     "id": 187, "name": "sky-other-merged"},
    {"color": [134, 199, 156], "isthing": 0,
     "id": 188, "name": "cabinet-merged"},
    {"color": [209, 226, 140], "isthing": 0,
     "id": 189, "name": "table-merged"},
    {"color": [96, 36, 108], "isthing": 0,
     "id": 190, "name": "floor-other-merged"},
    {"color": [96, 96, 96], "isthing": 0,
     "id": 191, "name": "pavement-merged"},
    {"color": [64, 170, 64], "isthing": 0,
     "id": 192, "name": "mountain-merged"},
    {"color": [152, 251, 152], "isthing": 0,
     "id": 193, "name": "grass-merged"},
    {"color": [208, 229, 228], "isthing": 0, "id": 194, "name": "dirt-merged"},
    {"color": [206, 186, 171], "isthing": 0,
     "id": 195, "name": "paper-merged"},
    {"color": [152, 161, 64], "isthing": 0,
     "id": 196, "name": "food-other-merged"},
    {"color": [116, 112, 0], "isthing": 0,
     "id": 197, "name": "building-other-merged"},
    {"color": [0, 114, 143], "isthing": 0, "id": 198, "name": "rock-merged"},
    {"color": [102, 102, 156], "isthing": 0,
     "id": 199, "name": "wall-other-merged"},
    {"color": [250, 141, 255], "isthing": 0, "id": 200, "name": "rug-merged"},
]

T1_CLASS_NAMES = [
    'aeroplane','bicycle','bird','boat','bottle','bus','car','cat',
    'chair','cow','diningtable','dog','horse','motorbike','person',
    'pottedplant','sheep','sofa','train','tvmonitor'
] # 20classes

# M-OWODB(=VOC20 + COCO60)
T2_CLASS_NAMES = [
    'truck','traffic light','fire hydrant','stop sign','parking meter',
    'bench','elephant','bear','zebra','giraffe',
    'backpack','umbrella','handbag','tie','suitcase',
    'microwave','oven','toaster','sink','refrigerator'
] # 20classes
T3_CLASS_NAMES = [
    'frisbee','skis','snowboard','sports ball','kite',
    'baseball bat','baseball glove','skateboard','surfboard','tennis racket',
    'banana','apple','sandwich','orange','broccoli',
    'carrot','hot dog','pizza','donut','cake'
]
T4_CLASS_NAMES = [
    'bed','toilet','laptop','mouse','remote','keyboard','cell phone','book','clock',
    'vase','scissors','teddy bear','hair drier','toothbrush',
    'wine glass','cup','fork','knife','spoon','bowl'
] # 20classes

COCO_BASE_CATEGORIES = {
    1: T1_CLASS_NAMES,
    2: T1_CLASS_NAMES,
    3: T1_CLASS_NAMES,
}

COCO_NOVEL_CATEGORIES = {
    1: T2_CLASS_NAMES,
    2: T3_CLASS_NAMES,
    3: T4_CLASS_NAMES,
}

#Novel COCO categories
# COCO_NOVEL_CATEGORIES = [
#     {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
#     {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicycle"},
#     {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "car"},
#     {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcycle"},
#     {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "airplane"},
#     {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "bus"},
#     {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "train"},
#     {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "boat"},
#     {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "bird"},
#     {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "cat"},
#     {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "dog"},
#     {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "horse"},
#     {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sheep"},
#     {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cow"},
#     {"color": [197, 226, 255], "isthing": 1, "id": 44, "name": "bottle"},
#     {"color": [153, 69, 1], "isthing": 1, "id": 62, "name": "chair"},
#     {"color": [3, 95, 161], "isthing": 1, "id": 63, "name": "couch"},
#     {"color": [163, 255, 0], "isthing": 1, "id": 64, "name": "potted plant"},
#     {"color": [0, 182, 199], "isthing": 1, "id": 67, "name": "dining table"},
#     {"color": [183, 130, 88], "isthing": 1, "id": 72, "name": "tv"},
# ]

places_dict = {
    "aeroplane": {
        "Airport": ["runway", "hangar", "control tower", "gates", "passengers"],
        "Hangar": ["tools", "aircraft", "workers", "equipment", "wings"],
        "Runway": ["tarmac", "lights", "markings", "airplanes", "signs"],
        "Sky": ["clouds", "aircraft", "birds", "blue sky", "sun"],
        "Terminal": ["gates", "luggage", "passengers", "security", "check-in"],
        "Control Tower": ["radar", "communication", "screens", "air traffic", "controllers"],
        "Tarmac": ["planes", "runway", "fuel trucks", "luggage carts", "passengers"],
        "Airbase": ["jets", "pilots", "military", "hangars", "runways"],
        "Cargo Area": ["crates", "containers", "loading", "forklifts", "trucks"],
        "Helipad": ["helicopter", "markings", "landing", "pads", "wind sock"],
        "Flight School": ["planes", "students", "instructors", "runway", "controls"],
        "Maintenance Area": ["tools", "parts", "engineers", "equipment", "planes"],
        "Private Airport": ["runway", "hangars", "jets", "gates", "offices"],
        "Military Base": ["planes", "jets", "runways", "personnel", "equipment"],
        "International Terminal": ["passports", "gates", "security", "immigration", "airlines"],
        "Cargo Plane": ["crates", "cargo", "workers", "loading", "equipment"],
        "Runway Approach": ["lights", "signs", "aircraft", "landing", "tarmac"],
        "Remote Airstrip": ["gravel", "aircraft", "runway", "bushes", "small planes"],
        "Flight Deck": ["controls", "pilots", "navigation", "cockpit", "instruments"],
        "Hanger": ["tools", "aircraft", "parts", "technicians", "jet engines"]
    },
    "bicycle": {
        "Bike Path": ["lanes", "trees", "riders", "pavement", "signs"],
        "Street": ["crosswalks", "cars", "bike lane", "lights", "pavement"],
        "Park": ["trails", "grass", "riders", "benches", "playground"],
        "Garage": ["bikes", "tools", "tires", "helmets", "racks"],
        "Mountain Trail": ["rocks", "dirt", "bikes", "hills", "trees"],
        "Suburb": ["sidewalks", "driveways", "grass", "bikes", "fences"],
        "City": ["traffic", "bike lanes", "pedestrians", "buildings", "lights"],
        "Countryside": ["dirt roads", "bikes", "grass", "fences", "hills"],
        "School": ["bike racks", "students", "locks", "backpacks", "helmets"],
        "Beach": ["boardwalk", "bikes", "sand", "sun", "waves"],
        "Camping Ground": ["tents", "bikes", "trails", "grass", "trees"],
        "Bridge": ["bikes", "lanes", "traffic", "rails", "river"],
        "Velodrome": ["track", "bikes", "racers", "stands", "laps"],
        "Race Track": ["bikes", "racers", "corners", "finish line", "speed"],
        "Cycling Club": ["bikes", "helmets", "jerseys", "riders", "routes"],
        "Market": ["bike parking", "stalls", "shoppers", "locks", "baskets"],
        "Bike Shop": ["bikes", "helmets", "parts", "repair", "gear"],
        "Country Road": ["bikes", "fences", "fields", "clouds", "riders"],
        "Mountain Road": ["switchbacks", "bikes", "cliffs", "trees", "scenic views"],
        "City Park": ["lanes", "grass", "trees", "fountains", "cyclists"]
    },
    "boat": {
        "Harbor": ["docks", "boats", "water", "buoys", "fishermen"],
        "Marina": ["yachts", "pontoons", "water", "sails", "piers"],
        "Lake": ["water", "shoreline", "fishing", "kayaks", "reeds"],
        "Ocean": ["waves", "boats", "fish", "sky", "beaches"],
        "River": ["water", "banks", "boats", "current", "fish"],
        "Pier": ["boats", "fishermen", "water", "rods", "sunset"],
        "Shipyard": ["cranes", "ships", "cargo", "docks", "workers"],
        "Canal": ["boats", "locks", "waterways", "bridges", "paddles"],
        "Beach": ["boats", "sand", "shore", "umbrellas", "towels"],
        "Dock": ["boats", "ropes", "water", "pilings", "fish"],
        "Island": ["boats", "palm trees", "sand", "waves", "fish"],
        "Fishing Village": ["boats", "nets", "fish", "shacks", "fishermen"],
        "Boat House": ["boats", "water", "ramps", "paddles", "sails"],
        "Resort": ["boats", "kayaks", "beach", "sun", "snorkeling"],
        "Port": ["containers", "ships", "cranes", "water", "docks"],
        "Riverbank": ["boats", "trees", "shore", "fishing", "water"],
        "Cove": ["boats", "water", "cliffs", "sand", "fish"],
        "Yacht Club": ["boats", "sails", "pontoons", "dock", "competitions"],
        "Bay": ["boats", "water", "fishing", "islands", "waves"],
        "Cruise Ship": ["decks", "passengers", "water", "pools", "cabins"]
    },
    "bottle": {
        "Kitchen": ["counter", "fridge", "sink", "cups", "bottles"],
        "Dining Table": ["bottles", "glasses", "plates", "cutlery", "food"],
        "Recycling Bin": ["bottles", "cans", "trash", "plastic", "paper"],
        "Bar": ["bottles", "glasses", "shelves", "counter", "drinks"],
        "Picnic": ["bottles", "sandwiches", "blanket", "cooler", "grass"],
        "Restaurant": ["bottles", "wine", "glasses", "tables", "guests"],
        "Party": ["bottles", "cups", "snacks", "music", "guests"],
        "Store": ["shelves", "bottles", "products", "labels", "aisles"],
        "Office": ["bottles", "desks", "laptops", "files", "chairs"],
        "Gym": ["bottles", "towels", "weights", "machines", "lockers"],
        "Living Room": ["bottles", "glasses", "remote", "sofa", "TV"],
        "Fridge": ["bottles", "milk", "juice", "water", "vegetables"],
        "Bathroom": ["bottles", "shampoo", "soap", "sink", "towels"],
        "Beach": ["bottles", "sand", "water", "coolers", "towels"],
        "Coffee Shop": ["bottles", "cups", "menu", "baristas", "customers"],
        "Airport": ["bottles", "bags", "security", "check-in", "passengers"],
        "Bakery": ["bottles", "cakes", "counter", "pastries", "boxes"],
        "Hotel Room": ["bottles", "mini-bar", "bed", "TV", "remote"],
        "Vending Machine": ["bottles", "snacks", "coins", "buttons", "products"],
        "Supermarket": ["bottles", "aisles", "shopping carts", "checkout", "products"]
    },
    "car": {
        "Garage": ["cars", "tools", "oil", "tires", "workbench"],
        "Highway": ["lanes", "signs", "guardrails", "overpasses", "cars"],
        "Parking Lot": ["spaces", "lines", "cars", "pavement", "fences"],
        "Street": ["cars", "crosswalks", "lights", "buildings", "pavement"],
        "Race Track": ["asphalt", "cars", "stands", "speed", "helmets"],
        "Driveway": ["cars", "pavement", "garage", "grass", "fences"],
        "Dealership": ["cars", "showroom", "salesperson", "windows", "pricing"],
        "Intersection": ["traffic lights", "cars", "crosswalks", "buildings", "signs"],
        "Car Wash": ["brushes", "water", "soap", "car", "rollers"],
        "Gas Station": ["pumps", "cars", "gas", "cashier", "store"],
        "Repair Shop": ["tools", "lift", "car parts", "mechanic", "cars"],
        "Tunnel": ["cars", "lights", "pavement", "walls", "traffic"],
        "Bridge": ["cars", "lanes", "railings", "river", "signs"],
        "Parking Garage": ["cars", "spaces", "ramps", "tickets", "floors"],
        "Suburban Road": ["cars", "houses", "driveways", "fences", "mailboxes"],
        "Freeway": ["lanes", "cars", "signs", "overpasses", "exits"],
        "City Street": ["cars", "buildings", "crosswalks", "traffic", "lights"],
        "Rural Road": ["cars", "trees", "fields", "fences", "hills"],
        "Auto Show": ["cars", "displays", "spectators", "stages", "brands"],
        "Parking Deck": ["cars", "levels", "ramps", "guardrails", "lights"]
    },
    "cat": {
        "House": ["sofa", "carpet", "scratching post", "food bowl", "windows"],
        "Garden": ["flowers", "grass", "birds", "sunlight", "fences"],
        "Vet Clinic": ["cages", "cats", "examination table", "medicine", "waiting room"],
        "Apartment": ["sofa", "cat bed", "toys", "windows", "carpet"],
        "Pet Store": ["cages", "cats", "food", "toys", "aquariums"],
        "Backyard": ["grass", "fence", "trees", "birds", "patio"],
        "Living Room": ["sofa", "rug", "table", "window", "TV"],
        "Bedroom": ["bed", "pillows", "carpet", "cat", "closet"],
        "Kitchen": ["cat food", "table", "chairs", "sink", "fridge"],
        "Balcony": ["chairs", "plants", "cat", "birds", "view"],
        "Park": ["grass", "benches", "trees", "birds", "flowers"],
        "Shelter": ["cats", "cages", "volunteers", "food", "adoption forms"],
        "Laundry Room": ["washer", "dryer", "cat bed", "baskets", "carpet"],
        "Vet Hospital": ["cats", "examination room", "medicine", "x-ray", "cage"],
        "Farm": ["barn", "hay", "cats", "mice", "fence"],
        "Rooftop": ["cats", "tiles", "chimney", "sky", "pigeons"],
        "Pet Hotel": ["cages", "cats", "food", "toys", "litter box"],
        "Playroom": ["toys", "cats", "scratching post", "balls", "windows"],
        "Living Room": ["carpet", "cats", "coffee table", "lamps", "plants"],
        "Terrace": ["cats", "plants", "furniture", "birds", "potted plants"]
    },
    "chair": {
        "Living Room": ["chair", "sofa", "coffee table", "carpet", "lamp"],
        "Office": ["chair", "desk", "computer", "files", "lamp"],
        "Dining Room": ["chair", "table", "plates", "glasses", "cutlery"],
        "Classroom": ["desks", "chairs", "students", "chalkboard", "books"],
        "Conference Room": ["chairs", "table", "projector", "screens", "laptops"],
        "Waiting Room": ["chairs", "magazines", "receptionist", "clock", "plants"],
        "Kitchen": ["chairs", "table", "plates", "cups", "forks"],
        "Restaurant": ["chairs", "tables", "menus", "plates", "cutlery"],
        "Auditorium": ["seats", "stage", "lights", "speakers", "audience"],
        "Cafeteria": ["tables", "chairs", "trays", "plates", "people"],
        "Library": ["tables", "chairs", "books", "laptops", "students"],
        "Theater": ["chairs", "screens", "curtains", "lights", "audience"],
        "Hospital Room": ["chair", "bed", "table", "medicine", "pillows"],
        "Cafe": ["tables", "chairs", "menus", "coffee", "pastries"],
        "Balcony": ["chairs", "table", "view", "plants", "railings"],
        "Park": ["benches", "chairs", "trees", "grass", "people"],
        "Living Room": ["chair", "sofa", "carpet", "table", "bookshelves"],
        "Bedroom": ["chair", "desk", "lamp", "bed", "wardrobe"],
        "Patio": ["chairs", "table", "plants", "umbrella", "sunlight"],
        "Terrace": ["chairs", "table", "plants", "view", "sunlight"]
    },
    "diningtable": {
        "Dining Room": ["table", "chairs", "plates", "glasses", "cutlery"],
        "Restaurant": ["tables", "menus", "waiters", "guests", "food"],
        "Kitchen": ["table", "chairs", "plates", "cups", "utensils"],
        "Cafe": ["tables", "coffee", "menus", "chairs", "guests"],
        "Banquet Hall": ["tables", "decorations", "guests", "flowers", "candles"],
        "Ballroom": ["tables", "seating", "decorations", "food", "guests"],
        "Patio": ["table", "chairs", "plants", "drinks", "outdoors"],
        "Balcony": ["table", "chairs", "view", "plants", "umbrellas"],
        "Lounge": ["tables", "chairs", "sofas", "coffee", "magazines"],
        "Living Room": ["table", "chairs", "books", "remote", "plants"],
        "Garden": ["table", "chairs", "grass", "flowers", "plants"],
        "Backyard": ["table", "chairs", "fence", "plants", "patio"],
        "Conference Room": ["table", "chairs", "projector", "laptops", "papers"],
        "Beach": ["table", "chairs", "sand", "drinks", "umbrellas"],
        "Terrace": ["table", "chairs", "view", "sunlight", "plants"],
        "Reception Hall": ["tables", "guests", "decorations", "food", "drinks"],
        "Cafeteria": ["tables", "trays", "food", "chairs", "people"],
        "Hotel Room": ["table", "chairs", "bed", "lamps", "TV"],
        "Pavilion": ["table", "chairs", "flowers", "food", "decorations"],
        "Picnic Area": ["tables", "benches", "food", "grass", "trees"]
    },
    "dog": {
        "Park": ["grass", "trees", "benches", "playground", "dogs"],
        "House": ["sofa", "dog bed", "food bowl", "toys", "door"],
        "Vet Clinic": ["cages", "dogs", "medicine", "examination table", "waiting room"],
        "Backyard": ["fence", "grass", "doghouse", "trees", "toys"],
        "Pet Store": ["cages", "dogs", "food", "toys", "leashes"],
        "Living Room": ["sofa", "dog bed", "carpet", "TV", "coffee table"],
        "Farm": ["barn", "fence", "grass", "dogs", "animals"],
        "Car": ["dog seat", "windows", "leash", "dogs", "blanket"],
        "Beach": ["sand", "waves", "dogs", "toys", "people"],
        "Trail": ["path", "trees", "grass", "dogs", "sunlight"],
        "Vet Hospital": ["cages", "medicine", "vets", "dogs", "treatment"],
        "Training Center": ["dogs", "toys", "obstacles", "grass", "treats"],
        "Animal Shelter": ["cages", "dogs", "volunteers", "toys", "kennels"],
        "Apartment": ["dog bed", "toys", "sofa", "windows", "carpet"],
        "Dog Park": ["fence", "grass", "toys", "dogs", "trees"],
        "Pet Hotel": ["dogs", "cages", "beds", "food", "toys"],
        "Living Room": ["carpet", "sofa", "dog bed", "windows", "TV"],
        "Playground": ["dogs", "grass", "trees", "fence", "water bowls"],
        "Field": ["grass", "fence", "dogs", "trees", "animals"],
        "Dog Show": ["stage", "dogs", "audience", "judges", "awards"]
    },
    "horse": {
        "Stable": ["hay", "stalls", "saddle", "bridle", "horses"],
        "Field": ["grass", "fence", "horses", "trees", "sky"],
        "Race Track": ["horses", "jockeys", "stands", "sand", "gates"],
        "Ranch": ["fence", "horses", "cowboys", "grass", "barn"],
        "Pasture": ["grass", "horses", "trees", "fence", "barn"],
        "Farm": ["barn", "fence", "horses", "hay", "trough"],
        "Trail": ["path", "trees", "horses", "riders", "grass"],
        "Arena": ["horses", "fence", "riders", "jumps", "stands"],
        "Mountain Path": ["rocks", "trees", "horses", "sky", "trails"],
        "Paddock": ["horses", "grass", "fence", "barn", "feed"],
        "Corral": ["fence", "horses", "posts", "gates", "dirt"],
        "Hillside": ["grass", "horses", "trees", "rocks", "clouds"],
        "Meadow": ["grass", "horses", "wildflowers", "trees", "fence"],
        "Countryside": ["fields", "horses", "barns", "fences", "trails"],
        "Beach": ["sand", "horses", "waves", "sun", "riders"],
        "Equestrian Center": ["horses", "riders", "jumps", "fence", "stables"],
        "Field": ["grass", "horses", "fence", "barn", "sky"],
        "Horse Show": ["horses", "arena", "riders", "spectators", "jumps"],
        "Backyard": ["fence", "horses", "barn", "trees", "feed"],
        "Rodeo": ["horses", "cowboys", "fence", "stands", "arena"]
    },
    "person": {
        "Office": ["desk", "computer", "chair", "files", "phone"],
        "Home": ["sofa", "TV", "bed", "kitchen", "bathroom"],
        "Gym": ["treadmill", "weights", "machines", "mirrors", "lockers"],
        "Park": ["grass", "benches", "trees", "playground", "path"],
        "Classroom": ["desks", "students", "chalkboard", "books", "teacher"],
        "Restaurant": ["tables", "menus", "waiters", "guests", "food"],
        "Airport": ["luggage", "gates", "passengers", "security", "check-in"],
        "Beach": ["sand", "sun", "waves", "people", "umbrellas"],
        "Supermarket": ["carts", "aisles", "products", "checkout", "shelves"],
        "Hospital": ["beds", "patients", "doctors", "nurses", "equipment"],
        "Train Station": ["platforms", "trains", "passengers", "seats", "tickets"],
        "Cafe": ["tables", "chairs", "coffee", "people", "menus"],
        "Mall": ["shops", "carts", "people", "stores", "escalators"],
        "Living Room": ["sofa", "TV", "coffee table", "books", "lamp"],
        "Car": ["seat", "steering wheel", "windows", "dash", "radio"],
        "School": ["students", "desks", "teacher", "chalkboard", "books"],
        "Cinema": ["seats", "screen", "popcorn", "tickets", "projector"],
        "Library": ["books", "shelves", "tables", "librarian", "computers"],
        "Airport Lounge": ["seats", "tables", "passengers", "luggage", "screens"],
        "Bus Stop": ["sign", "bench", "passengers", "bus", "road"]
    },
    "pottedplant": {
        "Garden": ["flowers", "pots", "soil", "sunlight", "plants"],
        "Living Room": ["sofa", "potted plant", "table", "window", "carpet"],
        "Balcony": ["pots", "plants", "sunlight", "chairs", "railings"],
        "Office": ["desk", "potted plant", "files", "window", "chair"],
        "Greenhouse": ["plants", "pots", "sunlight", "watering can", "glass"],
        "Store": ["shelves", "plants", "soil", "pots", "customers"],
        "Patio": ["plants", "furniture", "sunlight", "pots", "umbrella"],
        "Terrace": ["plants", "table", "chairs", "view", "sunlight"],
        "Window Sill": ["plants", "sunlight", "pots", "curtains", "windows"],
        "Kitchen": ["pots", "plants", "table", "chairs", "window"],
        "Hallway": ["plants", "tables", "lights", "windows", "carpet"],
        "Restaurant": ["plants", "tables", "chairs", "sunlight", "decor"],
        "Bedroom": ["bed", "plants", "nightstand", "lamp", "curtains"],
        "Bathroom": ["plants", "sink", "mirror", "towels", "shower"],
        "Living Room": ["sofa", "plants", "coffee table", "window", "curtains"],
        "Dining Room": ["table", "plants", "chairs", "sunlight", "windows"],
        "Lobby": ["chairs", "plants", "reception desk", "lights", "windows"],
        "Porch": ["chairs", "plants", "railings", "sunlight", "floor"],
        "Veranda": ["plants", "chairs", "table", "railings", "sunlight"],
        "Coffee Shop": ["plants", "tables", "chairs", "windows", "menus"],
        "Rooftop": ["plants", "furniture", "sky", "sunlight", "wind"]
    },
    "sheep": {
        "Pasture": ["grass", "fence", "sheep", "trees", "barn"],
        "Farm": ["barn", "field", "fence", "sheep", "hay"],
        "Field": ["grass", "sheep", "fence", "trees", "sky"],
        "Hillside": ["grass", "sheep", "rocks", "trees", "slopes"],
        "Ranch": ["fence", "sheep", "barn", "cowboys", "grass"],
        "Meadow": ["grass", "sheep", "fence", "wildflowers", "sky"],
        "Mountainside": ["sheep", "rocks", "grass", "trees", "sky"],
        "Open Range": ["sheep", "grass", "fence", "barn", "hills"],
        "Countryside": ["fields", "sheep", "trees", "fences", "barn"],
        "Paddock": ["sheep", "fence", "grass", "gate", "barn"],
        "Grazing Land": ["sheep", "grass", "fence", "sky", "barn"],
        "Shepherd's Hut": ["sheep", "fence", "shepherd", "grass", "dogs"],
        "Stable": ["sheep", "stalls", "fence", "barn", "hay"],
        "Village": ["sheep", "fence", "grass", "roads", "houses"],
        "Valley": ["sheep", "grass", "mountains", "river", "trees"],
        "Farmyard": ["barn", "sheep", "fence", "animals", "hay"],
        "Watering Hole": ["sheep", "water", "fence", "grass", "mud"],
        "Grazing Area": ["sheep", "grass", "trees", "fence", "barn"],
        "Foothills": ["sheep", "grass", "mountains", "trees", "fence"],
        "Riverbank": ["sheep", "water", "grass", "trees", "fence"]
    },
    "train": {
        "Train Station": ["platform", "tracks", "ticket booth", "passengers", "train"],
        "Railway": ["tracks", "trains", "bridges", "tunnels", "signals"],
        "Subway": ["platform", "train", "tracks", "signs", "passengers"],
        "Train Yard": ["trains", "tracks", "signals", "workers", "cargo"],
        "Bridge": ["tracks", "trains", "river", "pillars", "view"],
        "Tunnel": ["trains", "tracks", "walls", "lights", "signs"],
        "Metro Station": ["trains", "platform", "passengers", "signs", "announcements"],
        "Railway Depot": ["trains", "tracks", "maintenance", "repair", "cargo"],
        "High-Speed Rail": ["tracks", "trains", "passengers", "tunnels", "signs"],
        "Countryside": ["tracks", "trains", "fields", "trees", "stations"],
        "City Center": ["tracks", "trains", "buildings", "lights", "signals"],
        "Terminal": ["trains", "passengers", "platforms", "luggage", "waiting areas"],
        "Freight Yard": ["trains", "cargo", "containers", "tracks", "workers"],
        "Mountain Pass": ["tracks", "trains", "mountains", "tunnels", "bridges"],
        "Rural Station": ["trains", "platform", "passengers", "trees", "sky"],
        "Commuter Station": ["platform", "trains", "tickets", "passengers", "announcements"],
        "Depot": ["trains", "tracks", "engines", "signals", "maintenance"],
        "Suburban Station": ["platform", "trains", "houses", "passengers", "roads"],
        "Train Bridge": ["trains", "tracks", "water", "views", "pillars"],
        "Industrial Yard": ["trains", "cargo", "machines", "containers", "tracks"]
    },
    "tvmonitor": {
        "Living Room": ["sofa", "TV", "remote", "coffee table", "carpet"],
        "Bedroom": ["bed", "TV", "remote", "dresser", "windows"],
        "Office": ["desk", "TV", "computer", "remote", "chair"],
        "Store": ["TV", "shelves", "price tags", "electronics", "customers"],
        "Conference Room": ["table", "chairs", "TV", "remote", "presentations"],
        "Hotel Room": ["bed", "TV", "remote", "lamps", "windows"],
        "Home Theater": ["TV", "sofa", "remote", "speakers", "carpet"],
        "Classroom": ["TV", "projector", "desks", "students", "chalkboard"],
        "Lobby": ["TV", "chairs", "reception", "magazines", "tables"],
        "Cafe": ["TV", "tables", "chairs", "menu", "patrons"],
        "Living Room": ["sofa", "TV", "remote", "plants", "lamps"],
        "Waiting Room": ["TV", "chairs", "magazines", "receptionist", "clock"],
        "Gaming Room": ["TV", "console", "controllers", "sofa", "posters"],
        "Apartment": ["TV", "sofa", "remote", "windows", "curtains"],
        "Kitchen": ["TV", "counters", "chairs", "fridge", "sink"],
        "Hospital Room": ["bed", "TV", "remote", "monitor", "equipment"],
        "Bar": ["TV", "drinks", "glasses", "people", "lights"],
        "Gym": ["TV", "treadmills", "weights", "people", "water bottles"],
        "Restaurant": ["TV", "tables", "chairs", "menus", "drinks"],
        "Reception": ["TV", "desk", "chairs", "magazines", "computer"]
    },
    "bird": {
        "Forest": ["trees", "canopy", "leaves", "branches", "nests"],
        "Wetlands": ["water", "reeds", "marsh", "mud", "aquatic plants"],
        "Meadow": ["grass", "wildflowers", "insects", "shrubs", "sunlight"],
        "Park": ["benches", "trees", "fountains", "people", "bird feeders"],
        "Garden": ["flowers", "hedges", "birdbath", "trees", "insects"],
        "Lake": ["water", "shoreline", "fish", "rocks", "reeds"],
        "Riverbank": ["water", "rocks", "sand", "trees", "fish"],
        "Coastline": ["beach", "sand", "waves", "cliffs", "seaweed"],
        "Mountains": ["peaks", "rocks", "trees", "sky", "nests"],
        "Desert": ["sand", "cactus", "rocks", "dunes", "sunlight"],
        "Savannah": ["grass", "trees", "shrubs", "sky", "termite mounds"],
        "Urban Area": ["buildings", "balconies", "power lines", "parks", "rooftops"],
        "Jungle": ["vines", "dense trees", "canopy", "insects", "wild animals"],
        "Cliffside": ["rocks", "ledges", "nests", "wind", "birds of prey"],
        "Tundra": ["ice", "snow", "shrubs", "wind", "cold"],
        "Grassland": ["grass", "sky", "insects", "shrubs", "wind"],
        "Island": ["beaches", "trees", "ocean", "nesting sites", "rocks"],
        "Marsh": ["water", "mud", "reeds", "insects", "fish"],
        "Pond": ["water", "lily pads", "ducks", "fish", "reeds"],
        "Rainforest": ["trees", "canopy", "vines", "flowers", "waterfalls"]
    },
    "bus": {
        "Bus Station": ["platform", "ticket booth", "benches", "schedule", "bus bays"],
        "City Street": ["traffic lights", "crosswalks", "vehicles", "pavement", "bus stops"],
        "Highway": ["lanes", "traffic signs", "overpasses", "guardrails", "billboards"],
        "Bus Depot": ["garages", "maintenance area", "fuel pumps", "parking spaces", "buses"],
        "Parking Lot": ["spaces", "signs", "pavement", "lines", "fences"],
        "Intersection": ["traffic lights", "crossroads", "pavement", "signs", "vehicles"],
        "Terminal": ["waiting area", "schedule board", "entrances", "gates", "announcements"],
        "School": ["buses", "parking lot", "students", "signs", "buildings"],
        "Airport": ["shuttles", "parking area", "terminals", "runways", "passengers"],
        "Bus Lane": ["painted lines", "traffic", "vehicles", "signs", "buses"],
        "Suburban Road": ["houses", "sidewalks", "trees", "street lamps", "driveways"],
        "Roundabout": ["traffic circle", "signs", "vehicles", "lanes", "exits"],
        "Bus Stop": ["sign", "bench", "shelter", "schedule", "passengers"],
        "Industrial Area": ["factories", "warehouses", "roads", "parking lots", "loading docks"],
        "Tourist Attraction": ["buses", "parking lots", "visitors", "signs", "guides"],
        "University Campus": ["buses", "students", "buildings", "pathways", "benches"],
        "Downtown": ["high-rises", "pavement", "bus stops", "shops", "traffic"],
        "Shopping Mall": ["parking lots", "entrances", "buses", "shoppers", "signs"],
        "Stadium": ["parking area", "entrance gates", "buses", "crowds", "concessions"],
        "Park and Ride": ["parking lot", "buses", "cars", "signs", "shuttle services"]
    },
    "cow": {
        "Farm": ["barn", "stable", "field", "silo", "fence"],
        "Pasture": ["grass", "meadow", "fence", "watering hole", "hedgerow"],
        "Field": ["grass", "soil", "fence", "trees", "gate"],
        "Barn": ["hay", "stalls", "feeding trough", "roof", "doors"],
        "Dairy": ["milking parlor", "storage tanks", "coolers", "machinery", "cowsheds"],
        "Ranch": ["ranch house", "fence", "grazing land", "horses", "corrals"],
        "Grassland": ["grass", "hills", "trees", "shrubs", "water source"],
        "Cattle yard": ["pens", "troughs", "chutes", "gates", "fences"],
        "Stable": ["stalls", "feeding area", "doors", "mangers", "tack room"],
        "Paddock": ["fences", "gates", "grass", "shade", "water trough"],
        "Grazing land": ["grass", "hills", "streams", "fence", "open sky"],
        "Corral": ["fence", "gate", "chute", "posts", "panels"],
        "Pen": ["fence", "water trough", "feeding trough", "gates", "shade"],
        "Hillside": ["grass", "trees", "rocks", "streams", "slopes"],
        "Open range": ["grass", "sky", "hills", "fence", "wildlife"],
        "Valley": ["river", "grass", "trees", "shade", "fences"],
        "Agricultural land": ["fields", "crops", "tractors", "irrigation", "barns"],
        "Countryside": ["farms", "fields", "streams", "trees", "hedgerows"],
        "Watering hole": ["water", "mud", "grass", "shade", "animals"]
    },
    "motorbike": {
        "Garage": ["tools", "workbench", "oil", "helmets", "spare parts"],
        "Street": ["lanes", "traffic", "pavement", "crosswalk", "curbs"],
        "Highway": ["lanes", "guardrails", "overpasses", "signs", "vehicles"],
        "Parking Lot": ["spaces", "pavement", "lines", "motorbikes", "fences"],
        "Race Track": ["asphalt", "corners", "stands", "speedometers", "helmets"],
        "Motorbike Showroom": ["bikes", "helmets", "gear", "displays", "pricing"],
        "Workshop": ["tools", "motorbikes", "repair", "mechanic", "tires"],
        "Motorcycle Club": ["bikes", "helmets", "patches", "routes", "meetings"],
        "Country Road": ["pavement", "bikes", "fences", "trees", "hills"],
        "Desert Road": ["sand", "motorbikes", "sun", "cactus", "hills"],
        "Mountain Road": ["turns", "bikes", "trees", "sky", "rocky cliffs"],
        "City Street": ["traffic", "lanes", "crosswalks", "motorbikes", "buses"],
        "Bridge": ["lanes", "bikes", "rails", "traffic", "water"],
        "Rest Stop": ["parking", "bikes", "fuel", "benches", "signs"],
        "Toll Road": ["lanes", "bikes", "toll booths", "traffic", "signs"],
        "Coastal Road": ["ocean", "cliffs", "motorbikes", "curves", "wind"],
        "Scenic Route": ["trees", "hills", "motorbikes", "signs", "fences"],
        "Motorbike Rally": ["bikes", "riders", "helmets", "flags", "crowd"],
        "City Park": ["parking", "bikes", "trees", "benches", "paths"],
        "Village Road": ["pavement", "houses", "bikes", "trees", "shops"]
    },
    "sofa": {
        "Living Room": ["cushions", "coffee table", "carpet", "TV", "lamps"],
        "Furniture Store": ["showroom", "tags", "tables", "armchairs", "display"],
        "Lounge": ["sofas", "pillows", "rugs", "windows", "tables"],
        "Office": ["sofas", "reception desk", "magazines", "chairs", "plants"],
        "Apartment": ["sofa", "TV", "carpet", "coffee table", "windows"],
        "Bedroom": ["sofa", "bed", "pillows", "lamp", "dresser"],
        "Library": ["sofa", "books", "shelves", "tables", "lamps"],
        "Hotel Lobby": ["sofa", "reception", "magazines", "lamps", "tables"],
        "Waiting Room": ["sofa", "magazines", "clock", "tables", "receptionist"],
        "Patio": ["sofa", "tables", "plants", "sunlight", "cushions"],
        "Terrace": ["sofa", "tables", "plants", "view", "shade"],
        "Sunroom": ["sofa", "windows", "plants", "table", "sunlight"],
        "Home Office": ["sofa", "desk", "books", "lamps", "plants"],
        "Reception Area": ["sofa", "magazines", "coffee table", "lamp", "chairs"],
        "TV Room": ["sofa", "TV", "remote", "table", "cushions"],
        "Living Room": ["sofa", "carpet", "coffee table", "TV", "lamps"],
        "Office": ["sofa", "desk", "plants", "magazines", "chairs"],
        "Playroom": ["sofa", "toys", "carpet", "pillows", "table"],
        "Guest Room": ["sofa", "bed", "pillows", "lamps", "table"],
        "Backyard Patio": ["sofa", "plants", "cushions", "table", "shade"]
    }
}

chatGPT_prompts = {
    "bird": [
        "A colorful parrot perched on a branch in a tropical rainforest.",
        "A majestic eagle soaring over snowy mountains at sunrise.",
        "A small yellow canary singing on a tree branch in spring.",
        "A flock of pigeons flying over a busy city street.",
        "A hummingbird hovering near a bright red flower.",
        "A blue jay sitting on a wooden fence in a backyard.",
        "A flamingo standing gracefully in shallow water.",
        "A barn owl flying through a misty forest at dusk.",
        "A peacock displaying its vibrant feathers in a garden.",
        "A robin searching for worms on a dewy lawn.",
        "A crow perched on a streetlamp in an urban setting.",
        "A penguin sliding on ice in an Antarctic landscape.",
        "A sparrow sitting on a park bench in a city.",
        "A seagull flying above crashing ocean waves.",
        "A cardinal perched on a snowy branch in winter.",
        "A woodpecker tapping on a tree trunk in a forest.",
        "A swan gliding across a calm lake at sunset.",
        "A toucan with a large colorful beak sitting on a branch.",
        "A kestrel hunting over an open field.",
        "A vibrant kingfisher diving into a river for fish."
    ],
    "bus": [
        "A yellow school bus driving down a suburban street.",
        "A double-decker bus in red on the streets of London.",
        "A modern city bus with digital advertisements driving downtown.",
        "An old-style green bus driving through a countryside road.",
        "A crowded bus during rush hour in an urban city.",
        "An electric bus driving on a quiet street with trees.",
        "A blue tourist bus parked in front of a famous landmark.",
        "A bus with graffiti art parked at a bus station.",
        "A bus with large tinted windows driving at night.",
        "A public bus navigating a winding mountain road.",
        "A small shuttle bus waiting at an airport terminal.",
        "A red and white bus on a scenic coastal road.",
        "A futuristic autonomous bus without a driver on a street.",
        "A bus with people boarding at a busy bus stop.",
        "A vintage bus driving through a historical part of town.",
        "A bus with a 'route closed' sign on a quiet street.",
        "A city bus with a colorful rainbow advertisement on its side.",
        "A crowded bus filled with tourists on a city tour.",
        "An empty bus parked under a streetlamp at night.",
        "A bus with a 'last stop' sign in a quiet neighborhood."
    ],
    "cow": [
        "A black and white dairy cow grazing in a green field.",
        "A brown cow standing near a barn in a rural farm setting.",
        "A herd of cows walking across a grassy hill at sunset.",
        "A cow lying down in a meadow filled with wildflowers.",
        "A calf standing next to its mother in a field.",
        "A Highland cow with long shaggy hair standing in a pasture.",
        "A cow drinking water from a small pond in a field.",
        "A group of cows resting under a large tree in summer.",
        "A cow standing near a wooden fence with mountains in the background.",
        "A cow chewing grass in a meadow under a blue sky.",
        "A dairy cow being milked in a farm's milking area.",
        "A cow standing in the shade of a barn on a hot day.",
        "A herd of cows walking along a dirt path in the countryside.",
        "A cow with a bell around its neck grazing in a field.",
        "A cow licking salt from a mineral block in a pasture.",
        "A group of cows standing on a grassy hill at sunrise.",
        "A cow and a sheep grazing side by side in a green field.",
        "A cow standing alone on a misty field in early morning.",
        "A black cow lying on hay inside a barn.",
        "A cow with curly fur standing on a snowy field."
    ],
    "motorbike": [
        "A red motorcycle speeding down an open highway.",
        "A vintage motorbike parked near a beach during sunset.",
        "A dirt bike racing on a muddy track with dust clouds.",
        "A group of bikers on Harley-Davidson motorcycles riding in a line.",
        "A sleek black motorcycle parked in an urban alley at night.",
        "A motorbike with chrome details parked in front of a diner.",
        "A motorbike with a sidecar driving on a scenic mountain road.",
        "A blue sport bike leaning into a sharp turn on a race track.",
        "A motorcyclist wearing leather gear riding in the rain.",
        "A cafe racer style motorbike parked outside a coffee shop.",
        "A motorbike crossing a small bridge over a stream.",
        "A custom chopper with a flame paint job on an empty road.",
        "A motorbike with a large headlight in a garage workshop.",
        "A motorbike with dirt splatters parked on a grassy trail.",
        "A biker on a Harley cruising down a road at sunset.",
        "A group of motorbikes parked together at a scenic lookout.",
        "A motorbike rider performing a wheelie on an open road.",
        "A motorbike with a GPS mounted on the handlebars.",
        "A motorbike with racing stripes parked by a roadside café.",
        "A biker with a helmet and goggles riding on a sunny day."
    ],
    "sofa": [
        "A luxurious leather sofa in a modern living room.",
        "A cozy fabric sofa with colorful cushions in a family room.",
        "A vintage velvet sofa with wooden legs in a Victorian-style room.",
        "A sleek white sofa in a minimalist, all-white room.",
        "A large sectional sofa with a soft blanket in a cozy home.",
        "A recliner sofa in a spacious home theater room.",
        "A small loveseat with floral patterns in a cozy reading nook.",
        "A dark blue sofa with golden pillows in an elegant setting.",
        "A comfortable sofa with a coffee table in front in a living room.",
        "A modern grey sofa on a patterned rug in a stylish apartment.",
        "A plush sofa with a matching ottoman in a sunlit room.",
        "A sleeper sofa in a guest room with a blanket folded on top.",
        "A green velvet sofa with tufted buttons in a luxurious setting.",
        "A worn leather sofa in a rustic cabin by the fireplace.",
        "A cozy sofa with a plaid blanket in a holiday-themed room.",
        "A contemporary sofa with metallic legs in a modern house.",
        "A white sofa with colorful throw pillows in a bright room.",
        "A tan leather sofa with a furry rug in a Bohemian-style room.",
        "A sofa with built-in cup holders in a media room.",
        "A cozy sofa with Christmas decorations in a festive room."
    ],
    "aeroplane": [
        "A commercial jet flying through a clear blue sky.",
        "A vintage propeller plane flying over rolling hills.",
        "A military fighter jet soaring over a desert landscape.",
        "A private jet landing on a modern runway at sunset.",
        "A seaplane taking off from a lake in a mountainous area.",
        "An airplane flying through thick clouds with a sunset glow.",
        "A biplane doing aerobatic maneuvers over an airshow.",
        "A commercial airplane landing on a busy airport runway.",
        "A small Cessna plane flying over a green forest.",
        "A jumbo jet taking off from an airport with a city skyline.",
        "A passenger plane flying above the clouds with a view of mountains.",
        "An airplane with a colorful livery flying above the ocean.",
        "A plane parked at a gate in an international airport.",
        "A private jet flying through a clear sky with a mountain view.",
        "A futuristic airplane concept with sleek, streamlined wings.",
        "A cargo airplane with a large load flying over the ocean.",
        "A rescue plane flying low over a forest during a fire.",
        "A space shuttle ascending with boosters and fire trails.",
        "An airplane wing view from the window seat flying over clouds.",
        "A glider plane soaring gracefully over a peaceful valley."
    ],
    # Continue similarly for "bicycle", "boat", "bottle", "car", "cat", "chair",
    # "diningtable", "dog", "horse", "person", "pottedplant", "sheep", "train", "tvmonitor"
    # using a similar format with various descriptive scenes, styles, and contexts.
}

coco2voc = {
    'motorcycle': 'motorbike',
    'airplane': 'aeroplane',
    'potted plant': 'pottedplant',
    'dining table': 'diningtable',
    'tv': 'tvmonitor',
    'couch': 'sofa',
}

voc2coco = {val: key for key, val in coco2voc.items()}
convert_object = {"diningtable": "dining table",
                  "pottedplant": "potted plant",
                  "tvmonitor": "tv monitor"}

# download pre-trained weights of diffusion models at
# https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-inpainting
# and
# https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5
stable_inpaint_path = 'mpad_generation/PowerPaint/models/stable-diffusion-inpainting'
stable_diffusion_path = 'mpad_generation/PowerPaint/models/stable-diffusion-v1-5'

# download pre-trained weights of PowerPaint at https://huggingface.co/JunhaoZhuang/PowerPaint-v1/tree/main
unet_path = "mpad_generation/PowerPaint/models/unet/unet.safetensors"
text_encoder_path = "mpad_generation/PowerPaint/models/text_encoder/text_encoder.safetensors"

# download extracted features of pre-processing step from https://drive.google.com/file/d/1DCiLXICXqVqrFd675DXGpC-jib2O2Pa7/view?usp=sharing
feature_dir = "mpad_generation/NovelClassSynthesis"
dataset_path = "datasets/"