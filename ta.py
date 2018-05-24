import re

# re_email1=re.compile(r'^[a-zA-Z\][0-9a-zA-Z.]+@[0-9a-zA-Z_]+.com$')
re_email1 = re.compile(r'^[a-zA-Z][0-9a-zA-Z.]+@[0-9a-zA-Z]+.com$')
def is_valid_email(addr):
    if re_email1.match(addr):
    	return True
    else:
        return False
# 测试:

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
	m = re.match(r'^\<?([a-zA-Z\s]+)>?.*@.+$', addr) 
	return m.group(1)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

from datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2015,4,19,13,59,23)
dtt = dt.timestamp()
ddt = datetime.utcfromtimestamp(dtt)
print(ddt)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
# def to_timestamp(dt_str, tz_str):
	#str转换为datetime
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    #取时区
    tz = tz_str.split('UTC')[1]
    tz = tz.split(':')[0]
    # 强制转换时区
    tz_utc = timezone(timedelta(hours=int(tz)))
    date = date.replace(tzinfo=tz_utc)
    return date.timestamp()
# 测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

sh = re.match(r'^UTC([+|-]{1}[0-9]+)','UTC+7:00').group(1)
print(sh)

import base64

def safe_base64_decode(s):
    k = len(s) % 4
    if isinstance(s,str):
      while k:
        k -= 1;
        s += '='
    else:
      s = str(s, encoding = "utf-8")
      while k:
        k -= 1;
        s += '='

    s = bytes(s, encoding = "utf8")
    return base64.urlsafe_b64decode(s)    

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

 # Collapse
 import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    return {
        'width': 200,
        'height': 100,
        'color': 24
    }
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')