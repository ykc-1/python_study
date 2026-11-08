import time
'''
1、延时操作
time.sleep(5)
print(55555)


2、时间戳
从1970年1月1日 00：00：00：到现在的时间差（秒）
print(type(time.time()))

3、time.localtime() 当前地区的时间元组
t=time.localtime()
print(t[2])

print(t.tm_year)

4、time.asctime()直接输出时间，

t=time.localtime()
print(time.asctime(t))
将time.localtime()转化为标准时间

5、time.ctime()直接输出时间
将time.time()转化为标准时间

'''