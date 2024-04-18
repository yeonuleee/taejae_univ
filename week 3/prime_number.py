n = input("숫자를 입력해 주세요.")
for i in range(2, int(n)): #1과 2도 포함하고 싶다면 어떻게 하나요?
    if int(n)% i != 0:
        continue
    else:
        print(n+"은/는 소수가 아닙니다.")
        break 
else:
    print(n+"은/는 소수입니다.")
