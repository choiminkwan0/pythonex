# 파일에 내용을 쓸 때 사용 'w'
# 쓰기 모드로 열면 내용이 모두 사라짐
f = open("C:/pythonex/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 파일을 읽기만 함 'r'
# f.readline 파일의 첫 번째 줄을 읽어 출력
f = open("C:/pythonex/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# while문을 이용해 무한 루프로 계속 할 줄씩 읽음
f = open("C:/pythonex/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# f.readlines() 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
f = open("C:/pythonex/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# f.read() 파일의 내용 전체를 문자열로 리턴
f = open("C:/pythonex/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일 객체를 for문과 함께 사용 줄단위로 읽을 수 있음
f = open("C:/pythonex/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가하기 'a'
f = open("C:/pythonex/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# with 문은 파일을 열고 닫는 것을 자동으로 처리해줌
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")