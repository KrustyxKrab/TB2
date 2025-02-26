"I've wrote this list with the help of ChatGPT"

# all current tags of locations
# I would implement an option for the user to add a tag / but not done yet

poi_tags = {
    # 1️⃣ Food & Drink 🍽️🍹 (1-20)
    1: "Restaurant",
    2: "Cafe",
    3: "Bar",
    4: "Pub",
    5: "Bakery",
    6: "Ice Cream Shop",
    7: "Snack Bar",
    8: "Food Truck",
    9: "Winery",
    10: "Brewery",
    11: "Tea House",
    12: "Cocktail Bar",
    13: "Beer Garden",
    14: "Supermarket",
    15: "Market",
    16: "Organic Store",
    17: "Grocery Store",
    18: "Deli",
    19: "Farmers' Market",
    20: "Butcher Shop",

    # 2️⃣ Shopping & Commerce 🛍️🏦 (21-35)
    21: "Bookstore",
    22: "Clothing Store",
    23: "Shoe Store",
    24: "Electronics Store",
    25: "Furniture Store",
    26: "Second-Hand Store",
    27: "Shopping Center",
    28: "Jewelry Store",
    29: "Art Gallery",
    30: "Pharmacy",
    31: "Toy Store",
    32: "Department Store",
    33: "Florist",
    34: "Pet Store",
    35: "Hardware Store",

    # 3️⃣ Entertainment & Culture 🎭🎶 (36-55)
    36: "Cinema",
    37: "Theater",
    38: "Museum",
    39: "Concert Hall",
    40: "Opera",
    41: "Comedy Club",
    42: "Karaoke Bar",
    43: "Escape Room",
    44: "Casino",
    45: "Amusement Park",
    46: "Zoo",
    47: "Aquarium",
    48: "Planetarium",
    49: "Arcade",
    50: "Bowling Alley",
    51: "Stadium",
    52: "Sports Field",
    53: "Skatepark",
    54: "Playground",
    55: "Climbing Hall",

    # 4️⃣ Nature & Outdoor 🌿🏞️ (56-75)
    56: "Park",
    57: "Botanical Garden",
    58: "Beach",
    59: "Lake",
    60: "River",
    61: "Mountain",
    62: "Forest",
    63: "Cave",
    64: "Waterfall",
    65: "Glacier",
    66: "Desert",
    67: "National Park",
    68: "Nature Reserve",
    69: "Island",
    70: "Clearing",
    71: "Vineyard",
    72: "Windmill",
    73: "Lighthouse",
    74: "Observation Deck",
    75: "Ruins",

    # 5️⃣ Infrastructure & Public Services 🏛️🚉 (76-100)
    76: "Monument",
    77: "Church",
    78: "Temple",
    79: "Mosque",
    80: "Synagogue",
    81: "Library",
    82: "Co-Working Space",
    83: "University",
    84: "School",
    85: "Hospital",
    86: "Medical Center",
    87: "Fire Station",
    88: "Police Station",
    89: "Bank",
    90: "Train Station",
    91: "Airport",
    92: "Bus Stop",
    93: "Car Rental",
    94: "Hotel",
    95: "Hostel",
    96: "Campground",
    97: "Port",
    98: "Bridge",
    99: "Tunnel",
    100: "Town Hall",

    # 6️⃣ Sports & Recreation ⚽🏋️‍♂️ (101-130)
    101: "Gym",
    102: "Swimming Pool",
    103: "Tennis Court",
    104: "Golf Course",
    105: "Basketball Court",
    106: "Football Field",
    107: "Ice Rink",
    108: "Ski Resort",
    109: "Surfing Spot",
    110: "Cycling Trail",
    111: "Hiking Trail",
    112: "Yoga Studio",
    113: "Martial Arts School",
    114: "CrossFit Gym",
    115: "Dance Studio",
    116: "Equestrian Center",
    117: "Shooting Range",
    118: "Archery Range",
    119: "Rock Climbing Gym",
    120: "Trampoline Park",
    121: "Go-Kart Track",
    122: "Paintball Arena",
    123: "Billiards Hall",
    124: "Mini-Golf Course",
    125: "Skydiving Center",
    126: "Scuba Diving Center",
    127: "Paragliding Spot",
    128: "Motorsports Track",
    129: "Fishing Spot",
    130: "Rowing Club",

    # 7️⃣ Health & Wellness 💆‍♂️💊 (131-150)
    131: "Spa",
    132: "Massage Therapy Center",
    133: "Sauna",
    134: "Wellness Retreat",
    135: "Nail Salon",
    136: "Hair Salon",
    137: "Tattoo Parlor",
    138: "Cosmetic Clinic",
    139: "Chiropractic Clinic",
    140: "Acupuncture Clinic",
    141: "Physiotherapy Center",
    142: "Herbal Medicine Shop",
    143: "Weight Loss Clinic",
    144: "Mental Health Clinic",
    145: "Yoga Retreat",
    146: "Rehabilitation Center",
    147: "Organic Spa",
    148: "Barber Shop",
    149: "Dermatology Clinic",
    150: "Orthodontic Clinic",

# 8️⃣ Technology & Innovation 💻🔬 (151-170)
    151: "Startup Hub",
    152: "Tech Incubator",
    153: "Coworking Cafe",
    154: "VR Experience Center",
    155: "Esports Arena",
    156: "Gaming Lounge",
    157: "Makerspace",
    158: "Robotics Lab",
    159: "Hackerspace",
    160: "AI Research Center",
    161: "Blockchain Hub",
    162: "3D Printing Shop",
    163: "Software Development Studio",
    164: "Innovation Lab",
    165: "Data Center",
    166: "Cryptocurrency Exchange",
    167: "Tech Museum",
    168: "Augmented Reality Studio",
    169: "Drones & Robotics Store",
    170: "Cybersecurity Lab",

    # 9️⃣ Transportation & Logistics 🚗🚢 (171-190)
    171: "Car Dealership",
    172: "Electric Vehicle Charging Station",
    173: "Gas Station",
    174: "Bike Rental",
    175: "Scooter Rental",
    176: "Parking Garage",
    177: "Shipping Center",
    178: "Logistics Hub",
    179: "Public Transport Hub",
    180: "Freight Terminal",
    181: "Trucking Company",
    182: "Metro Station",
    183: "Helipad",
    184: "Spaceport",
    185: "Bicycle Repair Shop",
    186: "Taxi Stand",
    187: "Motorcycle Dealership",
    188: "Railway Depot",
    189: "Car Wash",
    190: "Towing Service",

    # 🔟 Education & Research 🎓📚 (191-210)
    191: "Primary School",
    192: "High School",
    193: "Vocational School",
    194: "Community College",
    195: "Technical Institute",
    196: "Music School",
    197: "Language School",
    198: "Dance Academy",
    199: "Driving School",
    200: "Flight School",
    201: "Cooking School",
    202: "Fashion Design School",
    203: "Film School",
    204: "Photography Studio",
    205: "STEM Learning Center",
    206: "Science Lab",
    207: "Astronomy Observatory",
    208: "Research Institute",
    209: "Historical Archive",
    210: "Anthropology Museum",

    # 1️⃣1️⃣ Government & Services 🏛️⚖️ (211-230)
    211: "City Hall",
    212: "Post Office",
    213: "Court House",
    214: "Embassy",
    215: "Consulate",
    216: "Military Base",
    217: "Customs Office",
    218: "Public Administration Office",
    219: "Voting Station",
    220: "Immigration Office",
    221: "Public Records Office",
    222: "Tax Office",
    223: "Social Services Center",
    224: "Labor Office",
    225: "Environmental Protection Agency",
    226: "Waste Recycling Center",
    227: "Water Treatment Facility",
    228: "Electric Power Station",
    229: "Weather Station",
    230: "Disaster Relief Center",

    # 1️⃣2️⃣ Religion & Spirituality ⛪🕌 (231-250)
    231: "Cathedral",
    232: "Chapel",
    233: "Monastery",
    234: "Abbey",
    235: "Shrine",
    236: "Mosque",
    237: "Hindu Temple",
    238: "Buddhist Temple",
    239: "Sikh Gurdwara",
    240: "Jewish Synagogue",
    241: "Christian Orthodox Church",
    242: "Pagan Ritual Site",
    243: "Spiritual Retreat",
    244: "Faith Healing Center",
    245: "Pilgrimage Destination",
    246: "Mediation Center",
    247: "Gospel Choir Hall",
    248: "Bible Study Center",
    249: "Sacred Spring",
    250: "Interfaith Center",

    # 1️⃣3️⃣ Housing & Real Estate 🏠🏢 (251-270)
    251: "Residential Neighborhood",
    252: "Apartment Complex",
    253: "Condominium",
    254: "Townhouse",
    255: "Gated Community",
    256: "Retirement Home",
    257: "Dormitory",
    258: "Luxury Mansion",
    259: "Co-Living Space",
    260: "Real Estate Office",
    261: "Property Development Site",
    262: "Tiny House Village",
    263: "Eco-Friendly Housing",
    264: "Houseboat Dock",
    265: "Off-Grid Settlement",
    266: "Homestead",
    267: "Urban Loft",
    268: "Penthouse",
    269: "Rural Farmhouse",
    270: "Beachfront Villa",

    # 1️⃣4️⃣ Media & Communications 📻📺 (271-290)
    271: "Radio Station",
    272: "Television Studio",
    273: "Podcast Recording Studio",
    274: "News Agency",
    275: "Printing Press",
    276: "Film Production Studio",
    277: "Advertising Agency",
    278: "Public Relations Firm",
    279: "Social Media Hub",
    280: "Content Creator Studio",
    281: "Publishing House",
    282: "Photography Agency",
    283: "Live Streaming Studio",
    284: "Animation Studio",
    285: "Comic Book Store",
    286: "Fan Convention Venue",
    287: "Creative Writing Workshop",
    288: "Documentary Film Center",
    289: "Press Club",
    290: "Editorial Office",

    # 1️⃣5️⃣ Festivals & Events 🎉🎆 (291-310)
    291: "Music Festival Grounds",
    292: "Food Festival Venue",
    293: "Film Festival Theater",
    294: "Cultural Fairground",
    295: "Trade Show Convention Center",
    296: "Art Exhibition Venue",
    297: "Fashion Show Runway",
    298: "Street Parade Route",
    299: "Marathon Starting Line",
    300: "Fireworks Display Area",
    301: "Carnival Fairground",
    302: "Themed Party Venue",
    303: "LGBTQ+ Pride Parade Route",
    304: "Gaming Convention Hall",
    305: "Car Show Pavilion",
    306: "Wedding Banquet Hall",
    307: "Charity Fundraiser Venue",
    308: "Seasonal Christmas Market",
    309: "National Holiday Celebration Venue",
    310: "E-Sports Tournament Arena",

    # 1️⃣6️⃣ Nightlife & Clubs 🎶🍾 (311-330)
    311: "Nightclub",
    312: "Dance Club",
    313: "Jazz Club",
    314: "Live Music Venue",
    315: "Underground Club",
    316: "Lounge Bar",
    317: "Speakeasy",
    318: "Rooftop Bar",
    319: "Wine Bar",
    320: "Karaoke Lounge",
    321: "Burlesque Club",
    322: "Hookah Lounge",
    323: "After-Hours Club",
    324: "Piano Bar",
    325: "Reggae Club",
    326: "Salsa Club",
    327: "Electronic Music Venue",
    328: "Comedy Lounge",
    329: "Billiards & Bar",
    330: "Retro Themed Club",

    # 1️⃣7️⃣ Automotive & Transport 🚗🛵 (331-350)
    331: "Car Rental Agency",
    332: "Motorcycle Rental",
    333: "Luxury Car Dealership",
    334: "Truck Stop",
    335: "Auto Repair Shop",
    336: "Tire Shop",
    337: "Oil Change Center",
    338: "Car Wash & Detailing",
    339: "Driving School",
    340: "RV Park",
    341: "Boat Rental",
    342: "Marina",
    343: "Helicopter Tours",
    344: "Air Charter Service",
    345: "Private Jet Terminal",
    346: "Ferry Terminal",
    347: "Cargo & Freight Terminal",
    348: "Ride-Sharing Pickup Zone",
    349: "EV Battery Swap Station",
    350: "Self-Driving Car Hub",

    # 1️⃣8️⃣ Adventure & Extreme Sports 🧗‍♂️🏄‍♀️ (351-370)
    351: "Bungee Jumping Site",
    352: "Paragliding Launch Area",
    353: "Skydiving Drop Zone",
    354: "Base Jumping Cliff",
    355: "Windsurfing Spot",
    356: "Kite Surfing Beach",
    357: "Caving Expedition Site",
    358: "Rappelling Cliff",
    359: "White Water Rafting",
    360: "Ski Jumping Ramp",
    361: "Extreme Rock Climbing",
    362: "High Altitude Hiking",
    363: "Snowboarding Terrain Park",
    364: "Motocross Track",
    365: "ATV Trail",
    366: "Sled Dog Racing Course",
    367: "Glacier Trekking",
    368: "Deep Sea Diving",
    369: "Shark Cage Diving",
    370: "Extreme Endurance Race",

    # 1️⃣9️⃣ Eco & Sustainable Places 🌱♻️ (371-390)
    371: "Eco-Friendly Resort",
    372: "Sustainable Farm",
    373: "Zero-Waste Grocery Store",
    374: "Renewable Energy Park",
    375: "Urban Community Garden",
    376: "Solar Energy Hub",
    377: "Hydroponic Garden",
    378: "Vertical Farming Center",
    379: "Composting Facility",
    380: "Permaculture Institute",
    381: "Wildlife Rehabilitation Center",
    382: "Plastic-Free Market",
    383: "Fair Trade Coffee Shop",
    384: "Recycling Innovation Lab",
    385: "Carbon Neutral Office",
    386: "Sustainable Clothing Store",
    387: "Zero-Emission Transport Hub",
    388: "Eco-Tourism Center",
    389: "Organic Vineyard",
    390: "Green Technology Lab",

    # 2️⃣0️⃣ Travel & Hospitality ✈️🏨 (391-410)
    391: "Luxury Resort",
    392: "Eco-Lodge",
    393: "All-Inclusive Resort",
    394: "Bed & Breakfast",
    395: "Motel",
    396: "Boutique Hotel",
    397: "Capsule Hotel",
    398: "Glamping Site",
    399: "Treehouse Accommodation",
    400: "Overwater Bungalow",
    401: "Historic Hotel",
    402: "Hostel with Co-Working",
    403: "Floating Hotel",
    404: "Train Hotel",
    405: "Desert Camp",
    406: "Snow Igloo Hotel",
    407: "Themed Hotel",
    408: "Jungle Retreat",
    409: "Underwater Hotel",
    410: "Wellness & Spa Resort",

    # 2️⃣1️⃣ Unique & Unusual Places 🏕️🦄 (411-430)
    411: "Abandoned Castle",
    412: "Underground City",
    413: "Secret Bunker",
    414: "Futuristic City",
    415: "Artificial Island",
    416: "Floating Market",
    417: "Hobbit Village",
    418: "UFO Watchtower",
    419: "Mysterious Ruins",
    420: "Magnetic Hill",
    421: "Haunted Mansion",
    422: "Cursed Village",
    423: "Alien-Themed Attraction",
    424: "Underground Waterfall",
    425: "Crystal Cave",
    426: "Mirror Lake",
    427: "Upside-Down House",
    428: "Gravity-Defying Place",
    429: "Bioluminescent Bay",
    430: "Lava Cave",

    # 2️⃣2️⃣ Pet-Friendly Locations 🐶🐱 (431-450)
    431: "Dog Park",
    432: "Pet-Friendly Cafe",
    433: "Cat Cafe",
    434: "Dog Beach",
    435: "Pet Spa",
    436: "Pet Adoption Center",
    437: "Dog Training School",
    438: "Animal Shelter",
    439: "Pet Boarding Facility",
    440: "Equestrian Riding Trail",
    441: "Pet Boutique",
    442: "Veterinary Clinic",
    443: "Pet-Friendly Hotel",
    444: "Bird Sanctuary",
    445: "Doggy Daycare",
    446: "Exotic Animal Rescue",
    447: "Petting Zoo",
    448: "Reptile House",
    449: "Pet Travel Agency",
    450: "Pet Cemetery",

    # 2️⃣3️⃣ Scientific & Space Exploration 🔬🚀 (451-470)
    451: "Space Observatory",
    452: "Rocket Launch Site",
    453: "Planetarium",
    454: "Astrobiology Lab",
    455: "Deep Space Communications Center",
    456: "Meteorite Impact Crater",
    457: "Black Hole Research Center",
    458: "Mars Simulation Base",
    459: "Space Tourism Center",
    460: "Telescope Array",
    461: "Gravity Research Lab",
    462: "Futuristic Space Hub",
    463: "Satellite Tracking Station",
    464: "Meteorological Research Center",
    465: "Antarctic Science Base",
    466: "Cryonics Facility",
    467: "Space Elevator Concept Site",
    468: "Terraforming Research Center",
    469: "Alien Signal Detection Lab",
    470: "Interstellar Travel Hub",
}