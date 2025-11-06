#read data.txt file and
#write data into new file ie wish.txt file
fp=open('wish.txt','w')
data="hello veena! good morning."
fp.write(data)
print("new file created successfully")
fp.close()