n = int(input("숫자를 입력해 주세요."))
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(f"{n}번째 피보나치 수는 " + str(fibonacci(n)) +"입니다.")
