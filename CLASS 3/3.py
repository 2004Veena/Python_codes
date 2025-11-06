# how to invoke inner function ?

'''def outer():
    print("outer function")
    def inner():
        print('inner function')
        return inner
outer()   
inner()      '''  # NameError: name 'inner' is not defined.




# solution
def outer():
    print("outer function")
    def inner():
        print('inner function')
    #return 100,200 
    return inner
inn=outer()   
print(inn)
print(type(inn))       # function
inn()                  # inner function