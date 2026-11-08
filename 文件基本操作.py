# 1.3 文件对象的方法
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
'''

f=open(r'E:\study\python_study\wenjian\wenjian1.txt')
f1=open(r'wenjian\wenjian1.txt')

print(f.read())
print(f1.read())
print(f.name)
f.close()
f1.close()


