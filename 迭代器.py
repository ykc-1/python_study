a="123"

it=iter(a)

it1=a.__iter__()

print(it)


print("-------")

print(next(it))
print(next(it))
print(next(it))

print("-------")

print(it1.__next__())
print(it1.__next__())
print(it1.__next__())