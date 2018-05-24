import random

a = random.random()
b = random.uniform(2,9)
c = random.randint(1,6)
print(c)

def fun1():
    x=int(input('请输入X：'))
    if x > 1:
        return 3*x-5
    elif x < -1:
        return 5*x+3
    else :
        return x+2
def fun2():
    x=int(input('请输入成绩：'))
    if x > 80:
        return 'A'
    elif x > 70:
        return 'B'
    elif x > 60:
        return 'C'
    else :
        return 'D'
def fun3():
    a=int(input('请输入a边：'))
    b=int(input('请输入b边：'))
    c=int(input('请输入c边：'))
    if (a+b>c and a+c>b and b+c>c) and (abs(a-b)<c and abs(a-c)<b and abs(b-c)<a):
        return True
    else :
        return False
def fun4():
    x=int(input('请输入年龄：'))
    if  2<= x <4 :
        print('正蹒跚学步')
    elif 4<= x <=13 :
        print('他是儿童')
    elif 13<= x <20 :
        print('他是青少年')
    elif 20<= x <65 :
        print('他是成年人')
    elif x >=65 :
        print('他是老年人')
    else :
        print('他是小屁孩')

print(fun1())
print(fun2())
print(fun3())
fun4()