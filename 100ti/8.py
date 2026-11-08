'''
输出 9*9 乘法口诀表
'''

for i in range(1,10):
    for j in range(i,10):
        a=i*j
        print(f"{i}*{j}={a}",end=" ")
    print("\n")