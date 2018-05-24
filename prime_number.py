'''
计算素数的一个方法：埃氏筛法
1.构造一个从3开始的奇数列
'''
def _odd_iter():
    n=1
    while True:
        n+=2
        yield n
'''
2.筛选函数
'''
def _not_divisible(d):
    return lambda x:x % d > 0

'''
3.打印
'''
def primes():
    yield 2
    it=_odd_iter()
    while True:
        c=next(it)
        yield c
        it=filter(_not_divisible(c),it)


for x in primes():
    if x<20:
        print(x)
    else:
        break