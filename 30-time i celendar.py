import time
 
print(time.time())
print(time.localtime(time.time()))
 
import calendar
 
print(calendar.month(2000,8))
calendar.setfirstweekday(6)
print(calendar.month(2000,8))
 
print('2000 is leap: ', calendar.isleap(2000))
 
print(calendar.calendar(2019))
