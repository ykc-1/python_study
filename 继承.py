'''
class 类名(父类名):
'''

class Person:
    def eat(self):
        print("人吃饭")

class Man(Person):
    def lunch(self):
       self.eat()           #注意区别
       Person.eat(self)
       Man.eat(self)


man=Man()
man.lunch()

'''
多重继承
class Grandfather:
    def eat(self):
        print('吃饭')

class Father(Grandfather):
    pass

    
class Son(Father):
    pass
'''

'''
改写方法
'''
class Father:
    def money(self):
        print('Father有100万')

class Son(Father):
    def money(self):
        print('Son赚到了1000万')
        Father.money(self)      #Father.money(self) 固定使用Father的方法
        super().money()         #使用上一层父类的方法，当上一层父类发生改变，调用的方法随着改变
        super(Son,self).money() #上面的是此代码的简写

son=Son()
son.money()

'''
多继承，子类可以拥有多个父类，可以具有所以父类的属性和方法

'''
class Father:
    def money(self):
        print('100w')

class Mom:
    def money2(self):
        print('120w')

class Son(Father,Mom):
    pass

son=Son()
son.money()
son.money2()







