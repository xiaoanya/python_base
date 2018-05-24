class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0:
            raise ValueError('score must over zero')
        self._width = value
		
    @property
    def height(self):
        return self._height
		
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0:
            raise ValueError('score must over zero')
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