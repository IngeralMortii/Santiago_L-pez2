# List of 200 words
words = [
    "apple", "banana", "grape", "orange", "kiwi", "melon", "peach", "plum", "pear", "cherry",
    "mango", "berry", "papaya", "apricot", "fig", "date", "lime", "lemon", "coconut", "tangerine",
    "watermelon", "cantaloupe", "pineapple", "pomegranate", "blueberry", "raspberry", "strawberry", "blackberry", "passionfruit", "nectarine",
    "dragonfruit", "lychee", "jackfruit", "quince", "persimmon", "starfruit", "soursop", "guava", "mandarin", "blood orange",
    "kiwifruit", "custard apple", "longan", "rhubarb", "currant", "honeydew", "tamarind", "barberry", "clementine", "zucchini",
    "asparagus", "broccoli", "carrot", "celery", "corn", "cucumber", "eggplant", "garlic", "ginger", "lettuce",
    "onion", "pepper", "potato", "radish", "spinach", "squash", "tomato", "turnip", "pumpkin", "artichoke",
    "beet", "brussels sprout", "cauliflower", "kale", "basil", "parsley", "cilantro", "sage", "thyme", "rosemary",
    "chive", "dill", "fennel", "marjoram", "oregano", "tarragon", "mint", "bay leaf", "lavender", "lemongrass",
    "poppy seed", "sesame", "sunflower", "flaxseed", "chia", "hemp", "quinoa", "barley", "oats", "rice",
    "wheat", "millet", "cornmeal", "buckwheat", "sorghum", "spelt", "rye", "amaranth", "teff", "farro",
    "chickpea", "lentil", "bean", "pea", "tofu", "tempeh", "seitan", "nut", "almond", "walnut",
    "pecan", "hazelnut", "macadamia", "pistachio", "cashew", "peanut", "brazil nut", "chestnut", "pine nut", "coconut meat",
    "pumpkin seed", "sunflower seed", "watermelon seed", "safflower", "cardamom", "cinnamon", "clove", "nutmeg", "vanilla", "gingerbread",
    "bread", "bagel", "biscuit", "cake", "cookie", "brownie", "muffin", "scone", "pie", "tart",
    "pudding", "custard", "gelato", "ice cream", "sorbet", "chocolate", "candy", "cereal", "popcorn", "snack",
    "sandwich", "wrap", "burger", "taco", "pizza", "pasta", "noodle", "sushi", "salad", "soup",
    "stew", "curry", "stir-fry", "grill", "bake", "roast", "fry", "boil", "steam", "sauté",
    "marinate", "season", "spice", "sauce", "dressing", "dip", "condiment", "pickle", "jam", "jelly",
    "honey", "vinegar", "oil", "butter", "margarine", "cream", "milk", "cheese", "yogurt", "ice",
    "water", "juice", "smoothie", "shake", "soda", "tea", "coffee", "beer", "wine", "cocktail"
]

# Print the list
print(words[-1])


#list slicing

list = [3, 22, 30, 5.3, 20]

print(list[:])

print(list[1:3])

print(list[2:-1])


#update a list

science = ["art", "chemistry", "geology"]

science[0] = "Biology"

print(science)

science[2] = "geology"

print(science)

integers = [2,5,9,20,27]

integers.remove(5)

print(integers)

integers.remove(27)

print(integers)

integers.pop(0)

print(integers)

list_fruits = ["Lemon", "Orange", "melon"]

#pop, remove, del

del list_fruits[0]

print(list_fruits)

#name_apemd

list_names = ["Juan", "pepe", "Felix"]

list_names.append("Carlos")

print(list_names)