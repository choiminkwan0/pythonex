a = [1, 2, 3]
print(a)
print(a[0] + a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print([-1][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))

a = [1, 2, 3]
a[2] = 4
print(a)

a = [1, 2, 3]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

a = [1, 2, 3]
a.pop()
print(a)

a = [1, 2, 3]
a.pop(1)
print(a)

a = [1, 2, 3, 1]
a.count(1)