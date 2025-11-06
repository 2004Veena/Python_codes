#simulation task
# 1 COIN TOSS 
'''from random import choice
coin=["Head","Tail"]

head_count=0
for i in range(100):
    result=choice(coin)
    if result =="Head":
       head_count=head_count+1
print("Number of head coin flips:",head_count)          #53  
print("Number of tail coin flips:",100-head_count)      #47'''



# 1 coin toss simulation

'''import random
#intialize counters
heads =0
tails =0

# simulate 100 coin flips
for i in range(100):
    flip=random.choice(["Head","Tails"])
    if flip =="Head":
        heads += 1
    else:
        tails +=1

# display results
print("coin flip simulation 100 flips")
print(f"Heads:{heads}")           # 54
print(f"Tails:{tails}")           # 46'''


# 2. lottery number generator
#generate a random set of 6 unique numbers b/w 1 and 49.

'''import random
lottery_numbers=random.sample(range(1,50),6)
lottery_numbers.sort()

print("Lottery_numbers:",lottery_numbers)'''


#password generator
# generate a random password of length 10 using UPPER CASE,LOWER CASE,SPECIAL CHAR,DIGITS.
'''import random
import string

characters = string.ascii_letters + string.digits + "!@#$%^&*"
password = ''.join(random.choice(characters) for i in range(10))

print("Generated Password:",password)   # VHXoHFF#S1'''


# ROCK,PAPER ,SCISSORS GAME
'''import random

choices = ['rock', 'paper', 'scissors']
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")         # Computer wins!'''


# class monitor
'''import random

students = ["Aarav", "Diya", "Kiran", "Ravi", "Neha", "Vikram", "Sana", "Rohan", "Priya", "Manish"]

class_monitor = random.choice(students)
print("Class Monitor:", class_monitor)'''


# shuffle student names
'''import random

students = ["Aarav", "Diya", "Kiran", "Ravi", "Neha", "Vikram", "Sana", "Rohan", "Priya", "Manish"]

random.shuffle(students)
print("Shuffled Student List:")
print(students)'''


#random 3 student without repitation
'''import random

students = ["Aarav", "Diya", "Kiran", "Ravi", "Neha", "Vikram", "Sana", "Rohan", "Priya", "Manish"]

project_group = random.sample(students, 3)
print("Selected Students for Project Group:", project_group)'''



# RANDOM COLOR PIC
'''import random

colors = ["red", "blue", "green", "yellow", "black", "white"]

while True:
    user_input = input("Press Enter to pick a random color (or type 'exit' to stop): ").lower()
    if user_input == "exit":
        print("Program stopped.")
        break
    print("Random Color Picked:", random.choice(colors))'''



# RANDOM NTEGER 1-100
'''import random

num = random.randint(1, 100)
print("Random Integer between 1 and 100:", num)'''


# FLOATING POINT NUMBER
'''import random

num = random.random()
print("Random Floating-Point Number between 0 and 1:", num)'''



# GENERATE RANDOM NUMBER 1-100 STEP BY 5
'''import random

num = random.randrange(50, 101, 5)
print("Random Number (50 to 100 with steps of 5):", num)'''



# ROLLING 6 SIDED DIE
import random

print("Rolling a six-sided die 10 times:")
for i in range(10):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)




