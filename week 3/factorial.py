#for 이용해서 구하기
n = input("팩토리얼을 구할 숫자를 입력해 주세요.")
result = 1
for i in range(2, int(n)+1, 1):
   result *= i
print(result)
#while 이용해서 구하기
n = input("팩토리얼을 구할 숫자를 입력해 주세요.")
multiply_n = 1
result = 1
while multiply_n < int(n):
    multiply_n = multiply_n + 1
    result = result * multiply_n
print(result)
