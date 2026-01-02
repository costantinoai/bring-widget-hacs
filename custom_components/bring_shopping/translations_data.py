"""Translation data for Bring! items - German to English and category mappings."""
from typing import Final

# Category translations (German -> English)
CATEGORY_TRANSLATIONS: Final[dict[str, str]] = {
    "Fleisch & Fisch": "Meat & Fish",
    "Milch & Käse": "Dairy & Cheese",
    "Früchte & Gemüse": "Fruits & Vegetables",
    "Getränke & Tabak": "Beverages",
    "Brot & Gebäck": "Bread & Bakery",
    "Haushalt & Gesundheit": "Household & Health",
    "Snacks & Süsswaren": "Snacks & Sweets",
    "Zutaten & Gewürze": "Ingredients & Spices",
    "Fertig- & Tiefkühlprodukte": "Frozen & Ready Meals",
    "Baumarkt & Garten": "Hardware & Garden",
    "Getreideprodukte": "Grains & Cereals",
}

# Category icons (used as fallback)
CATEGORY_ICONS: Final[dict[str, str]] = {
    "Meat & Fish": "🥩",
    "Fleisch & Fisch": "🥩",
    "Dairy & Cheese": "🧀",
    "Milch & Käse": "🧀",
    "Fruits & Vegetables": "🥬",
    "Früchte & Gemüse": "🥬",
    "Beverages": "🥤",
    "Getränke & Tabak": "🥤",
    "Bread & Bakery": "🍞",
    "Brot & Gebäck": "🍞",
    "Household & Health": "🧴",
    "Haushalt & Gesundheit": "🧴",
    "Snacks & Sweets": "🍫",
    "Snacks & Süsswaren": "🍫",
    "Ingredients & Spices": "🧂",
    "Zutaten & Gewürze": "🧂",
    "Frozen & Ready Meals": "🧊",
    "Fertig- & Tiefkühlprodukte": "🧊",
    "Hardware & Garden": "🔧",
    "Baumarkt & Garten": "🔧",
    "Grains & Cereals": "🌾",
    "Getreideprodukte": "🌾",
}

# Item icons (German and English) - used as fallback when CDN fails
ITEM_ICONS: Final[dict[str, str]] = {
    # Dairy
    "Milch": "🥛", "Milk": "🥛",
    "Butter": "🧈",
    "Käse": "🧀", "Cheese": "🧀",
    "Joghurt": "🥛", "Yogurt": "🥛", "Yoghurt": "🥛",
    "Sahne": "🥛", "Cream": "🥛",
    "Eier": "🥚", "Eggs": "🥚", "Egg": "🥚",
    "Mozzarella": "🧀", "Mozarella": "🧀",
    "Parmesan": "🧀", "Pecorino": "🧀",
    "Feta": "🧀",

    # Fruits
    "Bananen": "🍌", "Banana": "🍌", "Bananas": "🍌",
    "Apfel": "🍎", "Apple": "🍎", "Äpfel": "🍎", "Apples": "🍎",
    "Orange": "🍊", "Orangen": "🍊", "Oranges": "🍊",
    "Zitrone": "🍋", "Lemon": "🍋", "Zitronen": "🍋", "Lemons": "🍋",
    "Erdbeeren": "🍓", "Strawberries": "🍓", "Strawberry": "🍓",
    "Weintrauben": "🍇", "Grapes": "🍇",
    "Wassermelone": "🍉", "Watermelon": "🍉",
    "Ananas": "🍍", "Pineapple": "🍍",
    "Mango": "🥭",
    "Pfirsich": "🍑", "Peach": "🍑",
    "Birne": "🍐", "Pear": "🍐",
    "Kirschen": "🍒", "Cherries": "🍒", "Cherry": "🍒",
    "Kiwi": "🥝",
    "Avocado": "🥑",
    "Kokosnuss": "🥥", "Coconut": "🥥",

    # Vegetables
    "Tomaten": "🍅", "Tomato": "🍅", "Tomatoes": "🍅",
    "Karotten": "🥕", "Carrot": "🥕", "Carrots": "🥕", "Möhren": "🥕",
    "Zwiebeln": "🧅", "Onion": "🧅", "Onions": "🧅",
    "Knoblauch": "🧄", "Garlic": "🧄",
    "Kartoffeln": "🥔", "Potato": "🥔", "Potatoes": "🥔",
    "Brokkoli": "🥦", "Broccoli": "🥦",
    "Salat": "🥬", "Lettuce": "🥬", "Salad": "🥗",
    "Gurke": "🥒", "Cucumber": "🥒",
    "Paprika": "🫑", "Pepper": "🫑", "Bell Pepper": "🫑",
    "Mais": "🌽", "Corn": "🌽",
    "Pilze": "🍄", "Mushrooms": "🍄", "Mushroom": "🍄",
    "Aubergine": "🍆", "Eggplant": "🍆",
    "Spinat": "🥬", "Spinach": "🥬",
    "Kürbis": "🎃", "Pumpkin": "🎃",
    "Ingwer": "🫚", "Ginger": "🫚",

    # Meat & Fish
    "Poulet": "🍗", "Chicken": "🍗", "Hähnchen": "🍗", "Huhn": "🍗",
    "Rindfleisch": "🥩", "Beef": "🥩", "Steak": "🥩",
    "Schweinefleisch": "🥓", "Pork": "🥓",
    "Speck": "🥓", "Bacon": "🥓", "Pancetta": "🥓",
    "Würste": "🌭", "Sausage": "🌭", "Sausages": "🌭", "Wurst": "🌭",
    "Schinken": "🍖", "Ham": "🍖",
    "Fisch": "🐟", "Fish": "🐟",
    "Lachs": "🍣", "Salmon": "🍣",
    "Thunfisch": "🐟", "Tuna": "🐟",
    "Garnelen": "🦐", "Shrimp": "🦐", "Prawns": "🦐",
    "Sardinen": "🐟", "Sardines": "🐟",

    # Bread & Bakery
    "Brot": "🍞", "Bread": "🍞",
    "Brötchen": "🥖", "Rolls": "🥖", "Baguette": "🥖",
    "Croissant": "🥐", "Gipfeli": "🥐",
    "Toast": "🍞",
    "Kuchen": "🍰", "Cake": "🍰",
    "Kekse": "🍪", "Cookies": "🍪", "Biscuits": "🍪",
    "Muffin": "🧁", "Muffins": "🧁",
    "Pretzel": "🥨", "Brezel": "🥨",
    "Tortillas": "🫓",
    "Pizza": "🍕",

    # Beverages
    "Wasser": "💧", "Water": "💧", "Mineralwasser": "💧",
    "Kaffee": "☕", "Coffee": "☕",
    "Tee": "🍵", "Tea": "🍵",
    "Saft": "🧃", "Juice": "🧃", "Orangensaft": "🍊",
    "Cola": "🥤", "Coke": "🥤",
    "Limonade": "🍋", "Lemonade": "🍋",
    "Bier": "🍺", "Beer": "🍺",
    "Wein": "🍷", "Wine": "🍷", "Rotwein": "🍷", "Weisswein": "🥂",
    "Milchshake": "🥛",
    "Smoothie": "🥤",

    # Snacks & Sweets
    "Schokolade": "🍫", "Chocolate": "🍫",
    "Chips": "🍟",
    "Nüsse": "🥜", "Nuts": "🥜", "Erdnüsse": "🥜", "Peanuts": "🥜",
    "Popcorn": "🍿",
    "Eis": "🍨", "Ice cream": "🍨", "Eiscreme": "🍨",
    "Bonbons": "🍬", "Candy": "🍬", "Süssigkeiten": "🍬", "Sweets": "🍬",
    "Gummibärchen": "🍬", "Gummy bears": "🍬",
    "Honig": "🍯", "Honey": "🍯",
    "Marmelade": "🍯", "Jam": "🍯",
    "Nutella": "🍫", "Nougatcreme": "🍫",

    # Grains & Pasta
    "Reis": "🍚", "Rice": "🍚",
    "Nudeln": "🍝", "Pasta": "🍝", "Noodles": "🍝",
    "Spaghetti": "🍝",
    "Müsli": "🥣", "Cereal": "🥣", "Cereals": "🥣", "Cornflakes": "🥣",
    "Haferflocken": "🥣", "Oats": "🥣", "Oatmeal": "🥣",
    "Mehl": "🌾", "Flour": "🌾",
    "Gnocchi": "🥟",

    # Condiments & Spices
    "Salz": "🧂", "Salt": "🧂",
    "Pfeffer": "🌶️",
    "Zucker": "🍬", "Sugar": "🍬",
    "Öl": "🫒", "Oil": "🫒", "Olivenöl": "🫒", "Olive oil": "🫒",
    "Essig": "🍶", "Vinegar": "🍶",
    "Ketchup": "🍅",
    "Mayonnaise": "🥚", "Mayo": "🥚",
    "Senf": "🌭", "Mustard": "🌭",
    "Sojasoße": "🥢", "Soy sauce": "🥢",
    "Tomatensauce": "🍅", "Tomato sauce": "🍅",
    "Pesto": "🌿",
    "Basilikum": "🌿", "Basil": "🌿",
    "Oregano": "🌿",
    "Zimt": "🍂", "Cinnamon": "🍂",
    "Vanille": "🍦", "Vanilla": "🍦",

    # Household & Health
    "Zahnpasta": "🪥", "Toothpaste": "🪥",
    "Seife": "🧼", "Soap": "🧼",
    "Shampoo": "🧴",
    "Duschgel": "🧴", "Shower gel": "🧴", "Body wash": "🧴",
    "Toilettenpapier": "🧻", "Toilet paper": "🧻",
    "Taschentücher": "🤧", "Tissues": "🤧",
    "Waschmittel": "🧺", "Detergent": "🧺", "Laundry": "🧺",
    "Spülmittel": "🧽", "Dish soap": "🧽",
    "Müllbeutel": "🗑️", "Trash bags": "🗑️", "Garbage bags": "🗑️",
    "Reiniger": "🧹", "Cleaner": "🧹",
    "Deodorant": "🧴", "Deo": "🧴",
    "Rasierer": "🪒", "Razor": "🪒",
    "Pflaster": "🩹", "Bandages": "🩹", "Band-aids": "🩹",
    "Medikamente": "💊", "Medicine": "💊", "Medication": "💊",
    "Vitamine": "💊", "Vitamins": "💊",
    "Sonnencreme": "🧴", "Sunscreen": "🧴",

    # Frozen
    "Pommes": "🍟", "Fries": "🍟", "French fries": "🍟",
    "Tiefkühlpizza": "🍕", "Frozen pizza": "🍕",
    "Erbsen": "🟢", "Peas": "🟢",

    # Other
    "Kaugummi": "🫧", "Gum": "🫧", "Chewing gum": "🫧",
    "Kerzen": "🕯️", "Candles": "🕯️",
    "Batterien": "🔋", "Batteries": "🔋",
    "Blumen": "💐", "Flowers": "💐",
}

DEFAULT_ICON: Final = "🛒"
