import random
num=0
for i in range(8):
    for j in range(8):
        if not (i+j>7):
            print((i,j))
            num+=1
print(num)
'''num1=0
num2=0
for i in range(1000):
    a=random.randint(0,7)
    if(a==0):num1+=1
    if(a==7):num2+=1
print(num1)
print(num2)'''
'''
a=[1.333,2.345,5.432]
f=open('/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/Q_dct_res.txt','w')
for i in a:
    f.write(str(i))
f.close()'''