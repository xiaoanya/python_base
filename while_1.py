sum_1=1
i=0
while i<10 :
    i += 1
    sum_1 *= i
    
print(sum_1)

sum_1=0
i=0
while i<100 :
    i += 2
    sum_1 += i
    
print(sum_1)


#数字游戏
import random
c = random.randint(1, 100+1)

while True:
    ft = int(input('请输入一个整数1--100：'))
    if   ft > c:
        print('Bigger,请重输')
    elif ft < c:
        print('less,请重输')
    else:
        print('victory')
        break