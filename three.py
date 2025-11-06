''' # function to add two numbers
def add(a,b):
    return a+b

# initializing numbers
a = 10
b = 5

# calling function
res = add(a,b)

print(res)



def fact(n):
    
    # single line to find factorial
    return 1 if(n==1 or n==0) else n * fact(n - 1) 

# Driver Code
num = 5
print(fact(num))


a=10
b=20
print(a+b)
print(c))

eid=101
ename='rahul'
print(id(eid))

def wish():
    print('GM')
    print('GA')
    print('GE')

    wish()

    class account:
        pass # maintain dummy block

_eid=101
print(_eid)

#key words in python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


#DATA TYPES IN PYTHON
eid=102
ename='rahul'
esal=45000.45
avail=True
C=10+20j
eids=[101,102,103,104]
unames=('RG','SG','Priya','Modi')
numbers={10,10,10,20}
emp={
    'eid':101,
    'ename':'Rahul'
}

b = bytes([10,20,30,255])
ba=bytearray([10,20,30,255])
fz=frozenset({10,10,10})
r=range(100)
n=None
print(type(eid))        #int
print(type(ename))      #str
print(type(esal))       #float
print(type(avail))      #bool
print(type(eids))       #list
print(type(unames))     #tuple
print(type(numbers))    #set
print(type(emp))        #dict
print(type(ba))         #bytearray
print(type(fz))         #frozenset
print(type(r))          #range
print(type(n))          #none'''


# type casting functions(int,bin,oct,hex)
a=15
b=0b1111
c=0o17
d=0xA
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(int(15))
print(bin(15))
print(oct(15))
print(hex(15))


# Range()
#In Python, range() is a built-in function that generates an immutable sequence of numbers