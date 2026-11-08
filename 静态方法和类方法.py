'''
静态方法：只是将普通函数定义在了类里面，与类无关，与普通函数一样，只是调用方式有两种。
用于将功能类似或配套的函数打包在一个类中，易于调用和管理
'''
class Person:
    def sleep(self,time):
            print(f'我要睡{time}小时')
    @staticmethod
    def run():
        print('人类会跑')
    
Person.run()    #1、通过类名调用
person=Person()     #2、定义对象，通过对象调用
person.run()

Person.sleep(person,10)
person.sleep(20)

'''
类方法：主要用于对类属性进行操作，对比实例方法，类方法可以直接调用修改类属性，而不需要通过实例对象来调用
'''
class Person:
     @classmethod
     def sleep(cls):
          print("会碎觉")

Person.sleep()   #直接通过类调用
person=Person()
person.sleep()

class Student1:
     number=10
     @classmethod
     def num1(cls):
          print(f'有{cls.number}个学生')
     @classmethod     
     def add1(cls):
          cls.number=cls.number+1
          print(f'类对象中的number: {Student1.number}')  

class Student2:
     number=10
     def num2(self):
          print(f'有{self.number}个学生')
     def add2(self):
          self.number=self.number+1
          self.__class__.number +=1     #需要通过实例对象向上找到类对象，再对类属性进行修改，较麻烦
          print(f'实例对象中的number: {self.number}')
          print(f'类对象中的number: {Student2.number}')

Student1.num1()

student2=Student2()
Student2.num2(student2)
student2.num2()                 #读取类属性时可以不需要进行实例化

Student1.add1()
Student2.add2(student2)         #修改类属性更加方便



