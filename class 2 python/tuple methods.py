# TUPLE METHODS: 
# has no UPDATE and DELETE as TUPLE is 

#employee=({'eid':101},{'eid':102},{'eid':103})
#employee.insert(1,{'eid':104})             #AttributeError: 'tuple' object has no attribute 'insert'
#print(len(employee))




#SET METHODS:
#create
#copy()
eids={102,103,104,105}
uids=eids.copy()
print(uids)                   # {104, 105, 102, 103}


#update
eids={101,102,103}
eids.add(104)
print(eids)                 #{104, 101, 102, 103}

#insert
eid={101,102,103}
eids.pop()
print(eids)                   # {101, 102, 103}

eids={101, 102, 103}
# eids.remove(104)              # KeyError: 104  there is no value called 104 in the SET.

eids={101, 102, 103}
eids.discard(104)       # if element not present it will not return any ERROR.
print(eids)




#DIC :
# CREATE       # empty dic
emp={
    "eid":101,
    "name":"rahul",
    "esal":45000,
    "loc":'wayanad'
}
user=emp.copy()


#READ
emp={
    "eid":101,
    "name":"rahul",
    "esal":45000,
    "loc":'wayanad'
}
keys=emp.keys()
values=emp.values()
kv=emp.items()
print(keys)                # dict_keys(['eid', 'name', 'esal', 'loc'])
print(values)              # dict_values([101, 'rahul', 45000, 'wayanad'])
print(kv)                  # dict_items([('eid', 101), ('name', 'rahul'), ('esal', 45000), ('loc', 'wayanad')])


# dict.get(key) # return value of specified key
print(emp.get("eid"))  # 101


# return all the key-values
for key in emp.keys():
    print(key,"-",emp.get(key) ) 