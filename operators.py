'''a=10
b=20
c=30.5
d='ragul'
e='gandhi'
f=True
g=False

print(a+b)   #addition
print(a+c)   #float
#print(a+d)   #type error
print(d+e)   #concatination

# multiplication
print(a*d)   # repetation of string with number of int
print(a+b)   # multiplication
print(a*f)   # int*bool ->flag = 10

#print("rahul"*1000)  # Repetation
#print('rahul'*1000.0)    # type error


# Division operator
a=10
b=2
print(a/b)  # always written in floating point value
print(a//b) # floor dividion


#Floor division operator
import math
print(math.ceil(7.6))     # output : 8
print(math.floor(7.6))    # output : 7

#BINARY OPERATORS:
#A unary operator in Python is an operator that performs an operation on a single operand.


#membership operators: to verify a specific value is present in sequence
enames=['RG','SG','PG','NM']
print('RG' in enames)     #true
print('SG' in enames)     #true
print('pg' in enames)     # false  (because it is case sensitive)
print('Alia' not in enames)   # true 




enames=['RG','SG','PG','NM']
unames=("rahul","sonia","priyanka")
eids={101,102,103,101,102,103}
ename='rahul'
bytes_obj=bytes([10,20,30,40])
bytearray_obj=bytearray()'''




#identity operator : address comparision operator
a=10
b=[10,20,30]
c=[10,"rahul","sonia"]
print(id(a))
print(id(b))
print(id(b[0]))
print(id(c[0]))
print(id(b))
print(id(c))
print(b is c)   #false


b=[10,20,30]
c=[10,20,30]
print(b[0] is c[0])  # true
print(b is c)        #false   (address comparision)
print(b==c)          #true    (content comparision)