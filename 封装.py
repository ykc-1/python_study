'''
_属性、_方法  只是程序员约定的提示建议不要修改或调用

__属性、__方法  python自动改名为_类__属性(方法)

__方法__    魔法方法、python内置
'''
class Person:
    def __tuoyifu(self):
        print('先脱衣服')

    def swim(self):
        Person.__tuoyifu(self)  #可以在类内进行调用（通常不用这个写法）
        self.__tuoyifu()    #可以在类内进行调用
        print('会游泳')

person=Person()
person.swim()
person._Person__tuoyifu()   #可以通过_类__属性(方法)进行调用
