# FOR LOOPS IN PYTHON
'''eids=[101,102,103,104]
enames=('RG','SG','PG','NM')
numbers={10,20,10,20,30}
name="rahul gandhi"

for eid in eids:
    print(eid)

for ename in enames:
    print(ename)    

for num in numbers:
    print(num)

for ch in name:
    print(ch)   

for value in range(10,100):    # generate sequence of integer
    print(value)


# RANGE() FUNCTION 
for value in range(2,20,2):
    print(value)
     #2 is start value .........0 is default start value in python
     #20 is stop value 
     #2 step by value ........1 is default step by value in pyhton    


# RANGE() FUNCTION
for value in range(100,9,-2):
    print(value,end='\t')
# 100 is start value 
# 9 is stop value
# -2 is step by value '''


# for loop using list  
enames=['rg','sg','pg','nm']
for ename in enames:
    print(ename)

# WHILE LOOP using LIST
enames=['rg','sg','pg','nm']  
i=0
while i<=len(enames)-1:
    print(enames[i])  
    i=i+1


# for loop iteration using SET OBJECTS
eids={101,102,103,104} 
for eid in eids:
    print(eid)   

#
