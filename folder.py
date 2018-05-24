'''

#实现dir -l
import os

def mydir(path):
  if os.path.exists(path):
    L = [(path+x) for x in os.listdir(path)]
    print(L)
  else:
    print('The path not exists!')
#  mydir('D:\\test')



# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def findrelapath(path):
  if os.path.exists(path):
    L = os.listdir(path)
    for x in L:
      newpath = os.path.join(path,x)
      if os.path.isfile(newpath):  
        print(x)
      elif os.path.isdir(newpath):
        findrelapath(newpath)
  else:
    print('The path not exists!')

def main():
  mydir('D:\\test')
  print('++++++++++++++++++++')
  findrelapath('D:\\test')
main()

'''
import os
# os.path.join('D:\\test', 'testdir')
# os.mkdir('D:\\test\\testdir')
import pickle
# 写入文件
path = 'D:\\test\\test.txt'
# d = dict(name='Bob',age=20,score=88)
# f=open(path,'wb')
# pickle.dump(d,f)
# f.close()
d = dict(name='Bob',age=20,score=88)
sttr=pickle.dumps(d)
with open(path,'wb') as e:
  e.write(sttr)


#文件读取
with open(path,'rb') as e:
  print(pickle.load(e))
  pass



# with open(path,'wb') as e:
#   pickle.load(e)


