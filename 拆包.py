#对于函数中多个返回数据，去掉元组、列表或者字典，直接获取里面的值
lis=[1,2,3,4]

#方法一
a,b,c,d=lis
print(a,b,c,d)

#方法二
a,*b=lis
print(a,b) #1 [2, 3, 4]
print(a,*b) #1 2 3 4