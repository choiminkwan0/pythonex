# def 함수를 만들 때 사용하는 예약어
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)

def add(a, b):
    return a + b
print(add(3, 4))

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add": # 매개변수 choice에 "add"를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": # 매개변수 choice에 "mul"를 입력받았을 때
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 매개변수 앞에 별 2개(**)를 붙임
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 매개변수에 초깃값을 미리 설정
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")
