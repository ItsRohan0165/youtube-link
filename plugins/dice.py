import random

def getDice():
    random.seed()
    message = 'You rolled a {}'.format(random.randrange(0,100))
    return message