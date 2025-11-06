# write a python script to read emp.json file and 
# print no of male employees
# print no of female employees 


import json
with open("emp.json",'r') as fp:
    employees= json.load(fp)

print("no of employees:-",len(employees))         # no of employees:- 99

male_count=0
female_count=0
for emp in employees:
    if emp['GENDER']== 'Male':
       male_count=male_count+1
    elif emp['GENDER']=="Female":
        female_count=female_count+1
        
print("no of male employees:",male_count)          # no of male employees: 45
print("no of female employees:",female_count)      # no of female employees: 44
print(fp.closed)                                   # True