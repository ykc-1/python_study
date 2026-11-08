'''
多态性使得同名方法，根据对象不同，执行不同结果
'''
class Animal:
    def eat(self):
        print('动物会吃东西')

class Dog(Animal):
    def eat(self):
        print('狗吃狗粮')

class Cat(Animal):
    def eat(self):
        print('猫吃猫粮')

def Eat(donwu):
    donwu.eat()

dog=Dog()
cat=Cat()
Eat(dog)
Eat(cat)