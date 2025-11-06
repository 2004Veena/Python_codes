# FUNCTIONS
def calc():
    print('calculation')
    def add():
        print('addition')

        add()
        add()
    
    def multi():
            print('multiplication')
    multi()               # multiplication
calc()                    # calculation



# invoke inner function using reference
'''def calc():
    print('calculation')
    def add():
        print('addition')

        
    def multi():
            print('multiplication')
    return add
inner=calc() 
inner()
inner()'''



#
def calc():
    print('calculation')
    def add():
        print('addition')

        
    def multi():
            print('multiplication')
    return add
inner=calc() 
inner()
inner()