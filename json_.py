import json
d=dict(name='Bob',age=20,score=88)
L=json.dumps(d)
print(L)

# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score =score
#     def Student2dict(std):
#         return {
#             'name':std.name,
#             'age':std.age,
#             'score':std.score
#             }
#         # dict(name=self.name,age=self.age,score=self.score)
        
# s= Student('Bob',20,88)
# print(json.dumps(s,default=lambda obj : obj.__dict__))

