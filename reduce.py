from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L )

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
     L=s.split('.');
     return reduce(lambda x,y:y+x*10,map(int,L[0]))+reduce(lambda x,y:y+x*10,map(int,L[1]))/10**len(L[1])

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')