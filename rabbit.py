
#兔子
def rabbit():

    b=0
    c=1
    while True:
        yield c
        b,c = c,c+b
n=0
L=[]
for x in rabbit():
    # print(x)
    L.append(x)
    n+=1
    if n==20:
        break
print(L)
#素数
import math
q=[]
number=0
for x in range(101,200+1):
    i= 0 
    for y in range(2,int(math.sqrt(x))):
        if x%y ==0:
            i +=1
            break
    if i ==0 :
        q.append(x)
        number +=1
print('共有%d个素数\n'%number,q)

#水仙花
for x in range(100,1000):
    if (x//100)**3 + ((x//10)%10)**3 + (x%10)**3 == x :
        print('\n水仙花数是：',x)

#乘法表
for x in range(1,10):
    print('\n')
    for y in range(1,x+1):
        # print(x *y,end = ' ')
        print('%d x %d = %d\t'%(y,x,x*y), end = ' ')

#分数
def fun(x):

    a=1;  b=2; l=[2/1]
    for n in range(1,x+1):
        l.append(b/a)
        a,b=b,a+b
    return l
print()
print(str(fun(20)[-1]))

#求数字位数
a=int(input('请输入一个整数（五位以内）：'))
n1=10;i=1
while True:
    if a//n1 >0:
        n1*=10
        i+=1
    else:
        print()
        print(i,str(a)[::-1])
        break

#数字游戏
# import random
# c = random.randint(1, 100+1)

# while True:
#     ft = int(input('请输入一个整数1--100：'))
#     if   ft > c:
#         print('Bigger,请重输')
#     elif ft < c:
#         print('less,请重输')
#     else:
#         print('victory')
#         break

#金字塔
n=4
for x in range (1,n+1):
    print()
    for y_1 in range(n-x):
        print(' ',end = '')
    for y_2 in range((2*x-1)):
        print('*',end = '')
