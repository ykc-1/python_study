'''
1、文件重新命名
os.rename(旧名字,新名字)
    a=r'E:\study\python_study\wenjian\wenjian3.txt'
    b=r'E:\study\python_study\wenjian\wenjian4.txt'
    os.rename(a,b)

2、删除文件
os.remove(路径)
    a=r'E:\study\python_study\wenjian\wenjian3.txt'
    os.remove(a)

3、创建文件夹
os.mkdir(文件夹名)

4、删除文件夹
os.rmdir(文件夹名)

5、获取当前目录
os.getcwd()

6、获取目录列表
os.listdir()
'''
import os
#a=r'E:\study\python_study\wenjian\wenjian4.txt'
#b=r'E:\study\python_study\wenjian\wenjian3.txt'

#os.rename(a,b)
#os.remove(b)
os.mkdir('dd')
os.rmdir('dd')
print(os.getcwd())
print(os.listdir())
print(os.listdir('../'))#获取上一级列表