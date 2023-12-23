import random
from random import choice

cards = ["jack", "queen", "king", "kaido"]

n = random.choice(["heads", "tails"])
x = choice(range(0,20))
y = random.randint(1,10)

print(n,x,y)

z = random.shuffle(cards)

for card in cards:
    print(card)