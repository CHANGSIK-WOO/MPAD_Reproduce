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

meta_COCO_info = {
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
coco_fine_grained_classes = {
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

# Example: print(fine_grained_classes['dog'])

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
    1: T2_CLASS_NAMES + T3_CLASS_NAMES + T4_CLASS_NAMES,
    2: T1_CLASS_NAMES + T3_CLASS_NAMES + T4_CLASS_NAMES,
    3: T1_CLASS_NAMES + T2_CLASS_NAMES + T4_CLASS_NAMES,
    4: T1_CLASS_NAMES + T2_CLASS_NAMES + T3_CLASS_NAMES,
}

COCO_NOVEL_CATEGORIES = {
    1: T1_CLASS_NAMES,
    2: T2_CLASS_NAMES,
    3: T3_CLASS_NAMES,
    4: T4_CLASS_NAMES,
}

#Novel COCO categories
COCO_NOVEL_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicycle"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "car"},
    {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcycle"},
    {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "airplane"},
    {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "bus"},
    {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "train"},
    {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "boat"},
    {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "bird"},
    {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "cat"},
    {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "dog"},
    {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "horse"},
    {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sheep"},
    {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cow"},
    {"color": [197, 226, 255], "isthing": 1, "id": 44, "name": "bottle"},
    {"color": [153, 69, 1], "isthing": 1, "id": 62, "name": "chair"},
    {"color": [3, 95, 161], "isthing": 1, "id": 63, "name": "couch"},
    {"color": [163, 255, 0], "isthing": 1, "id": 64, "name": "potted plant"},
    {"color": [0, 182, 199], "isthing": 1, "id": 67, "name": "dining table"},
    {"color": [183, 130, 88], "isthing": 1, "id": 72, "name": "tv"},
]

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