# Simple game
import random

rando =random.randint(0,9)
print(type(rando))

Marks = int(input("what is the random number Im thinking from zero to nine :"))
print(type(Marks))


if(rando==Marks): 
  print('bageeels')
else:
  print("you are a flying bacoon try again")
