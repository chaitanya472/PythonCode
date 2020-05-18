import random
print ("I am going to make a bandname for you.")
adjectives =["Rainbow ", "Fluffy ", "Pretty ", "Soft ", 'Crazy ', 'Colossal ',
             'Sticky ', "Slippery ", 'Super ', 'Hollow ', 'Hissing ', 'Ancient ',
             'Tough ', 'Wild ', 'Impossible ' ]
nouns = ["Blade", "Explosion", "Slime", "Fire", 'Thunder', 'Monsters', 'Tornado',
         'Tank', 'Rocket', 'Laser', 'Dragons', 'Robots', 'Volcano', 'Titans'  ]
answer = "y"

while answer == "y":
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    bandName = word1 + word2
    print("The %s" %bandName)
    answer = input("Create another band name (y/n): ")
