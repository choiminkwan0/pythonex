dic = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
a = {1:'hi'} 
a = {'a':[1, 2, 3]}

a = {1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {1:'a', 1:'b'}
print(a)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.keys())
print(list(a.keys()))
print(a.values())
print(a.items())
print(a.clear())

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print('name' in a)
print('email' in a)

# key로 value얻기-get
a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.get('nokey'))
print(a.get('nokey', 'foo'))

# 집합(set) 중복을 허용하지 않음, 순서가 없음
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s1))

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)