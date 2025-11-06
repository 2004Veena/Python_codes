# USE CASES OF 1) break   2)return     3)continue
'''prod_price=[99,199,299,399,499,599,699,799,899,999]
for price in prod_price:
    if price>500:
        break
    print(price)

# while statement
prod_price=[99,199,299,399,499,599,699,799,899,999]
i=99
while i<=len(prod_price)-1:
    if prod_price[i]>500:
       break
print(prod_price[i])
i=i+1 '''

#continue : skip current iteration and execute next.
num=[]
for num in range(1,11):
    if num==7:
        continue
    print(num)     # 1 2 3 4 5 6 8 9 10


#prod_price below 500
prod_price=[99,199,299,399,499,599,699,799,899,999] 
for price in prod_price:
    if price > 500:
        continue
    print(price)   #  99 199 299 399 499




# method in python
# functions ...inneer functions....recursive functions...lamda fun...modules...packages...error