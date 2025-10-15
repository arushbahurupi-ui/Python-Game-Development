import random
words = [
    "apple", "banana", "cherry", "grape", "orange", "lemon", "lime", "peach",
    "pear", "plum", "mango", "apricot", "pineapple", "strawberry", "blueberry",
    "raspberry", "blackberry", "watermelon", "cantaloupe", "kiwi", "papaya",
    "guava", "nectarine", "fig", "date", "coconut", "avocado", "tomato",
    "carrot", "potato", "onion", "garlic", "broccoli", "cauliflower", "spinach",
    "lettuce", "cabbage", "celery", "pepper", "cucumber", "zucchini", "eggplant",
    "mushroom", "radish", "beet", "pumpkin", "squash", "corn", "peas", "bean",
    "olive", "herb", "basil", "oregano", "thyme", "rosemary", "mint", "parsley",
    "sugar", "salt", "butter", "oil", "vinegar", "honey", "jam", "cheese",
    "yogurt", "milk", "cream", "bread", "bagel", "muffin", "cake", "cookie",
    "brownie", "pie", "pancake", "waffle", "cereal", "rice", "pasta", "noodle",
    "soup", "stew", "salad", "sandwich", "burger", "pizza", "taco", "burrito",
    "sushi", "noodles", "ramen", "dumpling", "sausage", "chicken", "beef",
    "pork", "lamb", "fish", "shrimp", "crab", "lobster", "oyster", "clam",
    "egg", "omelet", "breakfast", "lunch", "dinner", "snack", "dessert",
    "kitchen", "oven", "stove", "pan", "pot", "knife", "fork", "spoon",
    "plate", "bowl", "cup", "glass", "table", "chair", "sofa", "bed",
    "pillow", "blanket", "lamp", "mirror", "curtain", "window", "door",
    "floor", "ceiling", "wall", "roof", "garden", "flower", "tree", "bush",
    "grass", "rock", "mountain", "river", "lake", "ocean", "beach", "island",
    "valley", "forest", "desert", "canyon", "waterfall", "sun", "moon", "star",
    "planet", "comet", "meteor", "cloud", "rain", "snow", "wind", "storm",
    "thunder", "lightning", "season", "spring", "summer", "autumn", "winter",
    "holiday", "birthday", "festival", "party", "music", "song", "melody",
    "rhythm", "dance", "movie", "film", "theater", "actor", "actress", "director",
    "camera", "stage", "audience", "book", "novel", "poem", "story", "author",
    "paper", "pen", "pencil", "eraser", "notebook", "desk", "school", "teacher",
    "student", "class", "lesson", "homework", "exam", "quiz", "grade", "subject",
    "math", "science", "history", "geography", "language", "art", "music",
    "computer", "internet", "email", "phone", "tablet", "keyboard", "mouse",
    "screen", "monitor", "printer", "camera", "photo", "picture", "image",
    "game", "puzzle", "riddle", "challenge", "score", "team", "player", "coach",
    "stadium", "field", "court", "ball", "basket", "goal", "race", "run",
    "walk", "swim", "jump", "climb", "fly", "drive", "ride", "train", "plane",
    "ship", "boat", "bicycle", "motorcycle", "car", "traffic", "road", "bridge",
    "station", "airport", "ticket", "passport", "hotel", "room", "luggage",
    "map", "guide", "tour", "museum", "gallery", "park", "zoo", "market", "shop",
    "store", "merchant", "price", "sale", "discount", "cash", "credit", "bank",
    "money", "coin", "bill", "wallet", "phonebook", "calendar", "clock", "time",
    "minute", "hour", "day", "week", "month", "year", "decade", "century",
    "history", "future", "present", "memory", "dream", "idea", "plan", "goal",
    "project", "work", "job", "career", "office", "boss", "colleague", "meeting",
    "email", "message", "chat", "call", "voice", "language", "sentence", "word",
    "letter", "alphabet", "grammar", "dictionary", "translation", "speech",
    "debate", "argument", "opinion", "belief", "value", "culture", "tradition",
    "religion", "philosophy", "science", "technology", "innovation", "robot",
    "machine", "engine", "battery", "power", "energy", "light", "heat", "cold",
    "pressure", "force", "motion", "speed", "velocity", "distance", "length",
    "width", "height", "depth", "volume", "mass", "weight", "balance", "scale",
    "measure", "meter", "ruler", "compass", "map", "route", "signal", "sign",
    "symbol", "color", "red", "blue", "green", "yellow", "black", "white",
    "purple", "orange", "brown", "pink", "gray", "silver", "gold", "bronze",
    "diamond", "ruby", "sapphire", "emerald", "pearl", "gem", "jewel", "treasure",
    "king", "queen", "prince", "princess", "castle", "palace", "knight", "sword",
    "shield", "battle", "war", "peace", "treaty", "law", "court", "judge",
    "jury", "crime", "police", "prison", "freedom", "rights", "vote", "election",
    "president", "minister", "leader", "citizen", "community", "nation", "world",
    "universe", "society", "economy", "market", "industry", "company", "brand",
    "product", "service", "customer", "user", "client", "support", "help",
    "assist", "create", "build", "design", "plan", "prepare", "organize", "arrange",
    "connect", "solve", "discover", "explore", "learn", "teach", "study", "read",
    "write", "listen", "speak", "watch", "look", "see", "hear", "feel", "touch",
    "taste", "smell", "love", "like", "hate", "prefer", "choose", "decide",
    "remember", "forget", "hope", "wish", "believe", "doubt", "trust", "care"
]


lives = 3

def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

while True:
    rand_word = random.choice(words)
    jumbled_word = shuffle_word(rand_word)
    print(jumbled_word)


    while True:
        ans = input("What word was jumbled: ")
        if ans == rand_word:
            print("Correct")
            break
        else:
            print("False, Try Again")
            lives -= 1
            if lives == 0:
                print("You've lost")
                break

    again = input("Do you want to play again: ")
    if again == "No":
        break
