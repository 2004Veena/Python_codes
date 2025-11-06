#LIST CRUD OPERATIONS :

#CREATE :

#copy()
enames=["rahul","sonia","priyanka","modi"]



#READ :

# count()
print(enames.count('rahul'))        # 1

# index()
print(enames.index("modi"))         # 3

# len() in-built function
print(len(enames))                  # 4
print(len("rahul"))                 # 5




#UPDATE:

# append()
enames.append("amith")
print(enames)                   #['rahul', 'sonia', 'priyanka', 'modi', 'amith']
                   

# insert()
enames.insert(1,"veena")
print(enames)                   # ['rahul', 'veena', 'sonia', 'priyanka', 'modi', 'amith']

# extend() 
enames.extend(["alia","karina"])
print(enames)                    #['rahul', 'veena', 'sonia', 'priyanka', 'modi', 'amith', 'alia', 'karina']

# reverse()
enames.reverse()
print(enames)                    # ['karina', 'alia', 'amith', 'modi', 'priyanka', 'sonia', 'veena', 'rahul']

# sort()
enames.sort()
print(enames)                    # ['alia', 'amith', 'karina', 'modi', 'priyanka', 'rahul', 'sonia', 'veena']


# sort() in descending order
enames.sort(reverse=True)  
print(enames)                    # ['veena', 'sonia', 'rahul', 'priyanka', 'modi', 'karina', 'amith', 'alia']



# DELETE :

# pop()
enames.pop()
print(enames)                   # ['alia', 'amith', 'karina', 'modi', 'priyanka', 'rahul', 'sonia']

# remove()
enames.remove("karina")
print(enames)                   # ['alia', 'amith', 'modi', 'priyanka', 'rahul', 'sonia']

# clear()
enames.clear()
print(enames)                   # []










  

