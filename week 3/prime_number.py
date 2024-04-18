n=input("숫자를 입력해 주세요.")
for i in range(2, int(n)):
    if int(n)% i != 0:
        print("소수입니다.")
        break
    elif int(n)% i == 0:
        print("소수가 아닙니다.")
        break
#1과 2도 포함하고 싶다면 어떻게 하나요?
