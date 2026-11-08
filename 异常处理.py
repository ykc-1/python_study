'''
方式1：

try:
    print(a)
except NameError as e:
    print(e)


 try:
    print(a)
except Exception as e:  Exception捕获任意错误
    print(e)   


try:
    print(a)
except NameError as e:  Exception捕获任意错误
    print(e)  
except KeyError as a:
    print(a)
......


方式二

try:
    print(a)
except:
.....
else:                当try中没有异常时，先执行try，再执行else，try中有异常时，except
.....
finally:            无论有没有异常，finally都要执行
                                 


'''
