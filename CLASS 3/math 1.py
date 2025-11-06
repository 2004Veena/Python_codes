# IN-BUILT MODULES :

'''from math import pi,sqrt,ceil,floor
print(pi)                 #3.141592653589793
print(sqrt(100))          #10.0
print(ceil(7.8))          #8
print(floor(7.8))         #7


# form module import member 1 as m1
from math import pi as rajani
print(rajani)          # rajani


import data 
help(data)
print(dir(data))


#WAP to generate 10.....4 digit OTP numbers   # RANDOM MODULE
#import random 
from random import randint
for num in range(10) :     # 10 times
    print(randint(1000,9999))

# LUCKY DRAW 
from random import choice
enames=["veena",'RAHUL',"SONIA","PRIYANKA"]
print(len(enames))      # 4
print(choice(enames))   # some random name from enames'''


# generate a random integer between 1 and 100

from random import randint
for num in range(10) :     
    print(randint(1,100))

#rolling a 6 sided die
import random
print("Die rolling 6 sided ")
