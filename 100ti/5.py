'''
输入三个整数x,y,z，请把这三个数由小到大输出
'''
print("请输入3个整数")
z=[]
for i in range(3):
    a=int(input(f"输入第{i+1}个整数"))
    z.append(a)
z.sort()

print(z)