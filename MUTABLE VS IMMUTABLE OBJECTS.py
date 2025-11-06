'''b=bytes([10,20,30,40])
#ba[0]=100    immutable
for value in b:
    print(value)


b=bytes([10,20,30,40])
b[0]=100   # immutable   #type error 'bytes' object does not support item assignment
for value in b:
    print(value)'''

# MUTABLE
ba=bytearray([10,20,30,40])
#ba[0]=100
for value in ba:
    print(value)


#changing index 0 value to 100
ba=bytearray([10,20,30,40])
ba[0]=100
for value in ba:
    print(value) 