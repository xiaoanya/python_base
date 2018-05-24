# f=open('C:/Users/zf111/Documents/C_language/test/test/test.txt','r')
# print(f.read())
# f.close()

# try :
#     f=open('C:/Users/zf111/Documents/C_language/test/test/test.txt','r')
#     print(f.read())
# finally :
#     if f:
#         f.close()


# with open('C:/Users/zf111/Documents/C_language/test/test/test.txt','r') as f:
#     # print(f.read())
#     print(f.readline())
#     pass


# with open('C:/Users/zf111/Documents/C_language/test/test/test.txt','r') as f:
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉

# f = open('C:/Users/zf111/Documents/C_language/test/test/test.txt', 'r', encoding='gbk', errors='ignore')

# fpath = 'C:\Windows\system.ini'

# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)


# with open('C:/Users/zf111/Documents/C_language/test/test/test.txt','w') as f:
#     # print(f.read())
#     f.writelines('woshixiaoan\n我是小安')
#     # f.writelines('我是小安')
    
#     pass

# from io import BytesIO

# # write to BytesIO:
# f = BytesIO()
# f.write(b'hello')
# f.write(b' ')
# f.write(b'world!')
# print(f.getvalue())

# # read from BytesIO:
# data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
# f = BytesIO(data)
# print(f.read())

import os
print(os.name)
print(os.environ.get('Path'))
print(os.path.abspath('.'))

# os.path.join()