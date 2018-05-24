# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()


# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()


# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     sdd = local_school.teacher
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#     print('Hello, %s (in %s)' % (sdd, threading.current_thread().name))

# def process_thread(names,namet):
#     # 绑定ThreadLocal的student:
#     local_school.student = names
#     local_school.teacher = namet
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice','juy'), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob','kgt'), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

import threading
#创建全局threadlocad对象
local = threading.local()
class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def getInfo():
    stu = local.student
    print('this is %s, %d, %d in %s' %(stu.name, stu.age, stu.score, threading.current_thread().name))

def setInfo(name, age, score):
    # local.student =Student()
    local.student = Student(name, age, score)
    getInfo()

t1 = threading.Thread(target=setInfo, args=('Alice', 25, 88), name='Thread_1')
t2 = threading.Thread(target=setInfo, args=('Bob', 27, 90), name='Thread_2')
t1.start()
t2.start()
t1.join()
t2.join()
print('print complete...')
