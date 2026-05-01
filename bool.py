a = True
b = False
print(type(a))
print(type(b))

if []:
    print("참")
else:
    print("거짓")

print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(0))
print(bool(3))

# 변수
a = [1, 2, 3]
print(id(a))

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b is a)

a, b = ('python', 'life')
print(a)
print(b)
(a, b) = 'python', 'life'
print(a)
print(b)
[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)
