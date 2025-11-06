#how to create a function
def add(a,b):
    def inner():
        print('inner')
    return a+b,"veena",inner

result=add(10,20)
print(result)            # (30, 'veena', <function add.<locals>.inner at 0x00000268CBABEFC0>)


result[2]()            # inner
result[2]()            # inner




# file handling
#WAP to read the data,txt file and print file data
