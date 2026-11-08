'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''
d=int(input("第几个数"))
an=[0,1]
def fn(m):
    for i in range(2,m):
        an.append(an[i-2]+an[i-1])

fn(d)
print(an)
