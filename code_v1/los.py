a=list()


for j in range(64):
    b=list()
    a.append(b)
    for j in range(64):
        c=list()
        b.append(c)
        for i in range(8):
            cc=list()
            c.append(cc)
            for j in range(8):
                cc.append("0")

#a为(8^3)*(8^3)数组，即8*8 block 的三重嵌套


for ii in a:
    for i in ii:
        for x_ in range(8):
            for y_ in range(8):
                x=x_+1
                y=y_+1
                m=0
                #if(y<5 and (x-2*y+16)%8==0):
                if(y_<4 and (x_-y_*2+14)%8 ==m):
                    i[x_][y_]="1"
                #if(y>4 and (x+9-2*y+16)%8 ==0):
                if(y_>3 and (x_+9-y_*2+14)%8 ==m):
                    i[x_][y_]="1"
'''
for ii in a:
    for i in ii:
        for x_ in range(8):
            for y_ in range(8):
                print(x_,y_)
                print(i[x_][y_])
            print('\n')
'''
f=open("/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/los_rec2.txt",'w')
#for ii in a:#ii是无序的64block组
'''
for m in range(8):
    for x in range(8):
        for n in range(8):
            for i in a[0][m*8+n]:#i是无序的64个block
                for y in range(8):
                    f.write(i[x][y])
                    f.write(" ")
            f.write('  ')
        f.write('\r\n')
    f.write('************')
    f.write('\r\n')
'''


for m in range(8):
    for x in range(8):
        for n in range(8):
            ii=a[0][m*8+n]
            for y in range(8):
                f.write(ii[x][y])
                f.write(" ")
            f.write(" ")
        f.write('\r\n')
    f.write('\r\n')
    