import random

s_subjects = [
    "MS Dhoni",
    "Bumrah"
]

s_actions = [
    " won",
    " plays",
]

s_objects = [
    " for Italy",
    " Kabaddi",

]

c_subjects = [
    "Shahrukh Khan",
    "Yash"
]

c_actions = [
    " seen eating",
    " sleeping"
]

c_objects = [
   " on footpath",
   " small pizza"
]

n_subjects = [
    "Prime Minister",
    "MLA"
]

n_actions = [
    " working for",
    " living in"

]

n_objects = [
    "  Italy",
    " development"
]


def working():
    news_category = input("Enter s for sports, c for celebrity, n for national: ").strip().lower()
    if news_category == 's':
        print(f"BREAKING NEWS: {s_news}")
    elif news_category =='c':
        print(f"BREAKING NEWS: {c_news}")
    elif news_category == 'n':
        print(f"BREAKING NEWS: {n_news}")
    else:
        print("Enter a valid category!")
        working()

    
while True:

    s_news = random.choice(s_subjects) + random.choice(s_actions) + random.choice(s_objects)
    c_news = random.choice(c_subjects) + random.choice(c_actions) + random.choice(c_objects)
    n_news = random.choice(n_subjects) + random.choice(n_actions) + random.choice(n_objects)

    
    user_input = input("Enter y to generate fake news or n to stop: ").strip().lower()
    
    if user_input == 'y': 
        working()
            
    elif user_input == 'n':
        break
    else:
        print("Enter a valid input!")
        continue
