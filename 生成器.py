#生成器是一种特殊的迭代器、yield关键字可以将一个函数变成生成器，生成器可以在函数执行过程中暂停和恢复
'''
def func():
    print('123')
    yield 456
    print (789)
    yield 632
it=func()
print(next(it))
print(it.__next__())
'''

def func():
    list=[]
    for i in range(1000):
        list.append(f"number{i}")
        if len(list)==50:
            yield list
            list=[]

print(func().__next__())
print(next(func()))

'''
生成器表达式是一次性的
'''
gen= (i for i in range(10))
print(gen)  #打印出来的是迭代器
print(next(gen))
print("------")
for i in gen:
    print(i)
