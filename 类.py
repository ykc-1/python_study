class washer:
    weight=400
    def wash(self):         #定义方法时，必须有一个参数
        print("洗衣服")     #定义一个类
        
    def wash2(self):
        self.wash()
        print("洗衣服2")
        
wa=washer()     #实例化对象，且可以实例化多个对象
print(wa.weight)    #通过 对象.方法名或类属性名进行调用
'''wa.wash()  
wa.wash2()        
'''
wa.wash()
washer.wash(wa) #wa.wash()与washer.wash(wa)等价，其中wash(self)中self用于指明是哪一个实例对象在使用washer类中的方法，
                #wa.wash()直接表明是wa对象在使用washer类中的wash方法，所以不用加self，
                #washer.wash(wa)只有通过添加self，来表明是wa实例对象在调用washer类的wash方法


wa.wash2()      #在方法中使用self可以实现方法的嵌套



class person:
    def __init__(self,a):
        self.sex=a

ykc=person('nan')
print(ykc.sex)          #构造函数

#析构函数
class person2:
    def __init__(self,name):
        print(f"这是2{name}")
    def __del__(self):
        print("person2结束")

class person:
    def __init__(self,name):
        print(f"这是{name}")
    def __del__(self):
        print("person结束")

ysy=person2('ysy')
ykc=person('ykc')
print("----------")
