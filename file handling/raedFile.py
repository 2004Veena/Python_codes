#to save data permanently.
#read data.txt file and print file

fp=open('data.txt','r')
data=fp.read()
print(data)
fp.close()
