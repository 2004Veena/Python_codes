#how to hold multiple datasets
'''eids=101,102,103
print(eids)
print(type(eids))  #tuple



#LIST DATA STRUCTURE(GROUP OF ELEMENTS OR VALUES ,OBJECTS AS ONE ENTITY ....ALLOWED DUPLICATES AND HETEROGENEOUS)

#create
a=[]     #empty list
eids=[101,102,103,104]
numbers=[10,20,10,10,30]
o=[10,20.5,'rahul',False,[],{},'y']

#READ
print(a)
print(eids)
print(numbers)
print(o)


#create
enames=["rahul","sonia","priyanka","modi"]

#read using INDEX
print(enames[0])
print(enames[1])
print(enames[2])
print(enames[3])
print(enames[8])  #index error

print(enames[-1])
print(enames[-2])
print(enames[-3])
print(enames[-4])'''



#DATA TYPES IN PYTHON
'''eid=102
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
'''a=15
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
print(hex(15))'''


# type casting of 101
b=101
print(int(101))       #101          
print(bin(101))       #0b1100101
print(oct(101))       #0o145
print(hex(101))       #0x65