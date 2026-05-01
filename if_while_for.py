money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone']
care = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for(first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

for i in range(2, 10):
    print(f"---{i}단---")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print('')

for i in range(4, 5):
    print(f"---{i}단---")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print('')

number = int(input("출력하고 싶은 단을 입력하세요 "))
print(f"---{number}단---")
for i in range(2, 10):
    result = number * i
    print(f"{number} x {i} = {result}")

number = int(input("출력하고 싶은 단을 입력하세요: "))
i = 2
print(f"---{number}단---")
while i <= 9:
    i += 1
    result = number * i
    print(f"{number} x {i} = {result}")
    if i == 9:
        break