# 1~ 100 차례차례 입력됨 2~5배수 카운팅 출력

num2 = 0
num3 = 0
num4 = 0
num5 = 0



for number in range(1, 101):

    if number % 2 == 0:
        num2 = num2 + 1
    if number % 3 == 0:
        num3 = num3 + 1
    if number % 4 == 0:
        num4 = num4 + 1
    if number % 5 == 0:
        num5 = num5 + 1

print("2의 배수 개수: ", num2)
print("3의 배수 개수: ", num3)
print("4의 배수 개수: ", num4)
print("5의 배수 개수: ", num5)
