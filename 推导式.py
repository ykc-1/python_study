'''
有列表推导式、集合推导式、字典推导式，没有元组推导式
'''

lt=[]
for i in range(10):
    lt.append(i)
print(lt)
#等于
lt1=[i for i in range(10)] 
print(lt1)

lt2=[i for i in range(10) if i%2==0]
print(lt2)


