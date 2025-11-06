employees=[{"id":1,"enames":"Liesa","gender":"Female"},
{"id":2,"enames":"Abbie","gender":"Male"},
{"id":3,"enames":"Karon","gender":"Female"},
{"id":4,"enames":"Dalston","gender":"Male"},
{"id":5,"enames":"Johnnie","gender":"Male"},
{"id":6,"enames":"Xena","gender":"Female"},
{"id":7,"enames":"Vale","gender":"Male"},
{"id":8,"enames":"Dall","gender":"Male"},
{"id":9,"enames":"Lannie","gender":"Male"},
{"id":10,"enames":"Ned","gender":"Male"},
{"id":11,"enames":"Phyllida","gender":"Female"},
{"id":12,"enames":"Hyatt","gender":"Male"},
{"id":13,"enames":"Audre","gender":"Female"},
{"id":14,"enames":"Kalie","gender":"Female"},
{"id":15,"enames":"Marley","gender":"Non-binary"},
{"id":16,"enames":"Lorie","gender":"Female"},
{"id":17,"enames":"Evyn","gender":"Male"},
{"id":18,"enames":"Kane","gender":"Male"},
{"id":19,"enames":"Britta","gender":"Female"},
{"id":20,"enames":"Donelle","gender":"Female"},
{"id":21,"enames":"Griffy","gender":"Male"},
{"id":22,"enames":"Jordain","gender":"Female"},
{"id":23,"enames":"Dorella","gender":"Polygender"},
{"id":24,"enames":"Deane","gender":"Female"},
{"id":25,"enames":"Arley","gender":"Male"},
{"id":26,"enames":"Dacia","gender":"Female"},
{"id":27,"enames":"Amargo","gender":"Female"},
{"id":28,"enames":"Alanson","gender":"Male"},
{"id":29,"enames":"Constance","gender":"Female"},
{"id":30,"enames":"Lucilia","gender":"Female"},
{"id":31,"enames":"Adelind","gender":"Bigender"},
{"id":32,"enames":"Fabio","gender":"Male"},
{"id":33,"enames":"Abdul","gender":"Male"},
{"id":34,"enames":"Kendall","gender":"Male"},
{"id":35,"enames":"Maurita","gender":"Agender"},
{"id":36,"enames":"Renelle","gender":"Female"},
{"id":37,"enames":"Philis","gender":"Female"},
{"id":38,"enames":"Stu","gender":"Genderqueer"},
{"id":39,"enames":"Rorke","gender":"Male"},
{"id":40,"enames":"Haskel","gender":"Male"},
{"id":41,"enames":"Jethro","gender":"Male"},
{"id":42,"enames":"Jeremias","gender":"Male"},
{"id":43,"enames":"Antonius","gender":"Male"},
{"id":44,"enames":"Katti","gender":"Female"},
{"id":45,"enames":"Alia","gender":"Female"},
{"id":46,"enames":"Nico","gender":"Male"},
{"id":47,"enames":"Claudetta","gender":"Female"},
{"id":48,"enames":"Tucker","gender":"Male"},
{"id":49,"enames":"Gibby","gender":"Male"},
{"id":50,"enames":"Auberta","gender":"Female"},
{"id":51,"enames":"Teri","gender":"Female"},
{"id":52,"enames":"Roselia","gender":"Female"},
{"id":53,"enames":"Patsy","gender":"Male"},
{"id":54,"enames":"Guinevere","gender":"Female"},
{"id":55,"enames":"Tom","gender":"Male"},
{"id":56,"enames":"Denny","gender":"Genderqueer"},
{"id":57,"enames":"Lindsy","gender":"Female"},
{"id":58,"enames":"Caty","gender":"Female"},
{"id":59,"enames":"Georgine","gender":"Polygender"},
{"id":60,"enames":"Tore","gender":"Male"},
{"id":61,"enames":"Rip","gender":"Genderqueer"},
{"id":62,"enames":"Carl","gender":"Male"},
{"id":63,"enames":"Averell","gender":"Male"},
{"id":64,"enames":"Lorenzo","gender":"Male"},
{"id":65,"enames":"Shea","gender":"Female"},
{"id":66,"enames":"Eberto","gender":"Male"},
{"id":67,"enames":"Binnie","gender":"Female"},
{"id":68,"enames":"Marcus","gender":"Male"},
{"id":69,"enames":"Cindelyn","gender":"Female"},
{"id":70,"enames":"Rudyard","gender":"Male"},
{"id":71,"enames":"Heriberto","gender":"Male"},
{"id":72,"enames":"Rosco","gender":"Male"},
{"id":73,"enames":"Eugene","gender":"Male"},
{"id":74,"enames":"Alvan","gender":"Male"},
{"id":75,"enames":"Nat","gender":"Male"},
{"id":76,"enames":"Corie","gender":"Female"},
{"id":77,"enames":"Chickie","gender":"Bigender"},
{"id":78,"enames":"Darren","gender":"Male"},
{"id":79,"enames":"Drucie","gender":"Female"},
{"id":80,"enames":"Judas","gender":"Male"},
{"id":81,"enames":"Forest","gender":"Male"},
{"id":82,"enames":"Randi","gender":"Bigender"},
{"id":83,"enames":"Tiffy","gender":"Female"},
{"id":84,"enames":"Doroteya","gender":"Female"},
{"id":85,"enames":"Tracee","gender":"Female"},
{"id":86,"enames":"Zaccaria","gender":"Male"},
{"id":87,"enames":"Blancha","gender":"Female"},
{"id":88,"enames":"Jaquenetta","gender":"Female"},
{"id":89,"enames":"Evangeline","gender":"Female"},
{"id":90,"enames":"Drusy","gender":"Polygender"},
{"id":91,"enames":"Isadora","gender":"Female"},
{"id":92,"enames":"Noe","gender":"Genderqueer"},
{"id":93,"enames":"Tilly","gender":"Polygender"},
{"id":94,"enames":"Dosi","gender":"Female"},
{"id":95,"enames":"Lurette","gender":"Female"},
{"id":96,"enames":"Carla","gender":"Female"},
{"id":97,"enames":"Mathilde","gender":"Female"},
{"id":98,"enames":"Loretta","gender":"Female"},
{"id":99,"enames":"Gabby","gender":"Male"},
{"id":100,"enames":"Israel","gender":"Male"}]

'''# using for loop
for emp in employees:
    print(emp['enames'])

# using while loop
i=0
while i<=len(employees)-1:
    print(employees[i]['enames'])   
    i=i+1 '''

# print number of female employees and male employees
 
male_count=0
female_count=0
bigender=0
for emp in employees:
    if emp['gender']=='Male':
        male_count=male_count+1
    elif emp['gender']=='Female':
        female_count=female_count+1  
    else:
        bigender+=1

print('number of male employees:',male_count) 
print('number of female employees:',female_count)
print('number of Bigender employees:',bigender)