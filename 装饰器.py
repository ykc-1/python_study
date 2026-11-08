
def denglu(fn):
    def inner(*args,**kwargs):
        while True:
            usename=input("请输入用户名:")
            password=input("请输入密码:")
            if usename=="ykc" and password=="123":
                print("登录成功")
                break
            else:
                print("登录失败")
        re=fn(*args,**kwargs)
        return re
    return inner

@denglu
def add():
    a= input("请输入你的姓名:")
    b=input("请输入你的年龄:")
    print("添加信息",a,b)

add()

@denglu
def delete():
    a= input("请输入你的姓名:")
    print("删除信息",a)

delete()