particle=("이/가") #끝나는 숫자에 따라 붙는 조사가 다른 건 어떻게 구현하나요?
number1, number2, number3= input("숫자 3개를 입력해 주세요.").split()
if int(number1)>= int(number2):
   if int(number1)>= int(number3):
       print(str(number1)+str(particle)+ " 가장 큰 숫자 입니다.")
   elif int(number1)<int(number3):
       print(str(number3)+str(particle)+" 가장 큰 숫자 입니다.")
elif int(number1)< int(number2):
    if int(number2)>= int(number3):
        print(str(number2)+str(particle)+" 가장 큰 숫자 입니다.")
    elif int(number2)< int(number3):
        print(str(number3)+str(particle)+" 가장 큰 숫자 입니다.")
