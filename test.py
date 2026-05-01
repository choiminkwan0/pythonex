a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

print(7 % 3)
print(3 % 7)
print(7 // 4)

a = 123
a = -178
a = 0
a = 1.2
a = -3.45

a = 0o177
a = 0x8ff
a = 0xABC

print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

food = "Python's favorite food is perl"
print(food)
say ='"Python is very easy." he says.'
print(say)

food = 'Python\'s favorite food is perl'
print(food)
say ="\"Python is very easy.\" he says."
print(say)

multiline = "Life is too short\nYouu need python"
print(multiline)

multiline = '''
    Life is too short
    You need python
    '''
print(multiline)

multiline = """
    Life is too short
    You need python
    """
print(multiline)

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a * 2)

a = "Life is too short"
print(len(a))

a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[-1])
print(a[0:4])

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

print("I eat %d apples." %3)

number = 3
print("I eat %d apples." %number)

print("I eat %s apples" %"five")

number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days" %(number, day))

print("I have %s apples" %3)
print("rate is %s" %3.234)

print("%10s" %"hi")
print("%-10sjane." %'hi')
print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)

print("I eat {0} apples".format(3))

number = 3
print("I eat {0} apples".format(number))

print("I eat {0} apples".format("five"))

number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(number, day))

print("I eat {number} apples. so I was sick for {day} days.".format(number = 10, day = 3))
print("I eat {0} apples. so I was sick for {day} days.".format(10, day = 3))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

print("{{ and }}".format())

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
age = 30
print(f'나는 내년이면 {age + 1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# :< 왼쪽 정렬, :> 오른쪽 정렬, :^ 가운데 정렬
# 가운데 정렬후 =로 공백 채우기
print(f'{"hi":=^10}')

# 왼쪽 정렬할고 !로 공백 채우기
print(f'{"hi":!<10}')

# 문자 개수 세기 count
a = "hobby"
print(a.count('b'))

# 문자열 삽입 join
print(",".join('abcd'))

# 위치 알려주기 find 찾는 문자열이 없으면 -1 반환
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

# 소문자를 대문자로 바꾸기 upper
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 lower
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기 lstrip
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 rstrip
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기 strip
a = " hi "
print(a.strip())

# 문자열 바꾸기 replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 split
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))
