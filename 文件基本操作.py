# 1.3 文件对象的方法1
# 1. open()：创建一个file对象，默认是以只读模式打开
# 2. read(n)：n表示从文件中读取的数据的长度，没有传n值就默认一次性读取文件的所有内容
# 3. write()：将指定内容写入文件
# 4. close()：关闭文件

# 1.4 属性
# 文件名.name：返回要打开的文件的文件名，可以包含文件的具体路径
# 文件名.mode：返回文件的访问模式
# 文件名.closed:检测文件是否关闭，关闭就返回True
'''

r =open('test.txt')
print(r.name)
print(r.mode)
print(r.closed)
r.close()
print(r.closed)



文件读写 
read(n):
readline():读取一行
readlines():读取所有，以行输出
write():写入文件

访问模式
f1=open(r'wenjian\wenjian1.txt','r')
r只能读、若文件不存在则报错
r+可读可写、若文件不存在则报错
w只能写、若文件不存在则创建、文件存在则覆盖
w+可读可写、若文件不存在则创建、文件存在则覆盖
a只能写、文件不存在则创建、文件存在追加写
a+可读可写、文件不存在则创建、文件存在追加写


文件定位操作
tell():显示文件内指针当前位置
seek(offset,whence):移动文件读取指针到指定位置
offset:偏移量
whence:起始位置，0文件开头、1当前位置、2文件结尾位置

with open代码运行结束后，自动调用close方法

encoding='utf-8'
'''

f=open(r'E:\study\python_study\wenjian\wenjian1.txt')
f1=open(r'wenjian\wenjian1.txt')

print(f.read())
print(f1.read())
print(f.name)
#f.write('dddd') 由于访问模式，不可写
f.close()
f1.close()

f2=open(r'wenjian\wenjian1.txt','a+')
f2.write('\n1\n')
print(f2.read())
f2.close()

with open(r'wenjian\wenjian2.txt','w',encoding='utf-8') as f3:
    f3.write('123六')


