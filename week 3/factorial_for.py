n = input("팩토리얼을 구할 숫자를 입력해 주세요.")
result = 1
for i in range(2, int(n)+1, 1):
   result *= i
print(result)
