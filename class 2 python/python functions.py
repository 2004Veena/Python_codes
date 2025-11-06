# class is variable and method
# functions : group of statements for specific task., where code can be reused.
#def         sub                       (a,b):
#key word    #user defined function    #parameter


'''def login():
    print('login success')
login()   #login success
login()   #login success
login()   #login success
login()   #login success

def add(a,b):          # (a,b) is formal arguments.
    print(a+b)
add(10,20)             #30   (10,20) is actaul arguments.
add(1,2)               #3
add('rahul','gandhi')  # Concatination  because both arguments are #String
#add(10,'rahul')       # TYPE ERROR  unsupported operand type(s) for +: 'int' and 'str'
#add()                 #TypeError: add() missing 2 required positional arguments: 'a' and 'b'
#add(1)                #TypeError: add() missing 1 required positional argument: 'b'


# Arguments are 4 Types   1) Positional  2)Keyword  3)Default  4)Variable Length

# 1) Positional Arguments
def calc(a,b):
    print(a-b)
calc(100,200)             #-100
calc(200,100)             # 100


# 2)  Keyword Arguments
def calc(a,b):
    print(a-b)
calc(a=100,b=200)         #-100
calc(b=200,a=100)         #-100


# 3)  Default  Argumrnts
def sum(a,b,c=100):       #Default argument c=100
    print(a+b+c)
sum(1,2,3)                #6  
sum(1,2)                  #103   c=100 default value


# 3)  Default  Argumrnts
def sum(a,b,c):           # no default arguments passed
    print(a+b+c)
sum(1,2,3)                # 6  
sum(1,2)                  # TypeError: sum() missing 1 required positional argument: 'c'


def sum(a,b,c=100,d):     # SyntaxError: parameter without a default follows parameter with a default
    print(a+b+c)          # Default argumrnts should be defined in the last position.
sum(1,2,3)                #6  
sum(1,2)



# variable length arguments
def sum(a,*b):             # without *  its a TYPE ERROR
    print("a",a,"b",b)
sum(10,20)                 # a 10 b (20,)
sum(10,20,30)              # a 10 b (20, 30)
sum(10,20,30,40)           # a 10 b (20, 30, 40)
sum(10,20,30,40,50)        # a 10 b (20, 30, 40, 50) 
sum(10,20,30,40,50,60)     # a 10 b (20, 30, 40, 50, 60)



# example 1
def add(a,b):
    c=1
    return a+b+c
r1=add(10,20)
print(r1)



# example 2
def get_bal(acc_bal):
    min_bal=500
    return acc_bal-min_bal
bal1=get_bal(5000)
print(bal1)                 #4500
bal2=get_bal(15000)
print(bal2)                 #14500



# example 3
def get_bal(name,acc_bal):
    min_bal=500
    return acc_bal-min_bal
bal1=get_bal("rahul",5000)
print(bal1)
bal2=get_bal("sonia",15000)
print(bal2)    '''



# USE CASES OF 1) break   2)return     3)continue
prod_price=[99,199,299,399,499,599,699,799,899,999]
for price in prod_price:
    if price>500:
        break
    print(price)

# while statement
prod_price=[99,199,299,399,499,599,699,799,899,999]
i=99
while i<=len(prod_price)-1:
    if prod_price[i]>500:
       break
print(prod_price[i])
i=i+1
    


#display 
#i=0
#while i<=prod_price:
