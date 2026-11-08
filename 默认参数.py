'''
def func(a,b=100):
    print(a,b)
func(5)
func(5,6)

def func1(**kwargs):
    print(kwargs)
func1(name='yk')


def func1():
    print("----")
    def func2():
        print('func2')
        func2()
    func2()

func1()


global  nonlocal
'''

def a():
    global b
    b=10
a()

def c():
    print(b)

c()