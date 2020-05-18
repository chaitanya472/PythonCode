import random
import string

adjectives = ['sleepy', 'slow', 'green', 'huge', "rainbow", "fluffy",
              "pretty","soft", 'crazy', 'colossal', 'sticky', "slippery",
              'super', 'hollow','hissing', 'ancient',  'tough', 'wild',
              'impossible', 'small', 'tiny', 'tired', 'mega', 'basic',
              'critical', 'easy', 'bitter','angry' 'cool', 'expensive',
              'fuzzy', 'grumpy', 'modern', 'frail', 'busy', 'elegant', 'dizzy',
              'empty', 'wicked', 'young', 'dull','mute', 'rapid', 'red', 'blue',
              'indigo', 'orange', 'violet', 'brown', 'suprised']
nouns = ['apple', "blade", "explosion", "slime", "fire", 'thunder', 'monsters'
         'tornado', 'tank', 'rocket', 'laser', 'dragons', 'robots', 'volcano',
         'titans', 'potatoe', 'churo', 'book', 'chair', 'core', 'app', 'card',
         'chip', 'hand', 'pig', 'cat', 'dog', 'bat', 'track', 'cow', 'table',
         'flower', 'rose', 'printer', 'statue', 'trip', 'brain', 'lake', 'snow',
         'formula', 'ice', 'gravel', 'ship', 'clock', 'hourglass', 'jacket',
         'coat', 'mask', 'cloud', 'leg', 'trophy', 'spider', 'hero', 'train','tool']
print("Welcome to password generator.")

while True:
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    number = random.randrange(0, 100)
    special = random.choice(string.punctuation)

    password = word1 + word2 + str(number) + special
    print(" Here is your password: %s" %password)
    answer = input("Do you want another password? (y/n): ")
    if(answer == "n"):
        break
