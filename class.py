class Student(object):
    pass
    __slots__ = ('name', 'age')


s = Student()
s.name = "changan"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType
# s.set_age=MethodType(set_age,s)
# print(s.age)
s2 = Student()
Student.set_age = set_age
s2.set_age(100)
print(s2.age)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('请输入整数！')
        if value < 0:
            raise ValueError('请输入正整数！')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('请输入整数！')
        if value < 0:
            raise ValueError('请输入正整数！')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class Animal(object):

    def __init__(self,name):
        self.__name=name
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

dg = Animal('孙二哥')
print(dg.get_name())
dg.set_name('猪八姐')
print(dg.get_name())
dg.set_name('唐小三')
print(dg.get_name())