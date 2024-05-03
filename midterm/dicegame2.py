import random

def roll_dice():
    return random.randint(1, 6)

player_number = int(input("플레이어 수를 입력해 주세요."))

names_numbers = {}
for i in range(player_number):
    name = input("플레이어 이름을 입력해 주세요.")
    number = roll_dice()
    names_numbers[name] = number

print("주사위를 굴려 봅시다!")

print("결과는 " + str(names_numbers))

winner = [name for name, number in names_numbers.items() if max(names_numbers.values()) == number]
print("가장 높은 숫자가 나온 플레이어는 " + str(winner) +"입니다.")
#대괄호 중괄호 빼고 문자만 나오게 하는 방법 없나요?

answer = input("게임을 계속 하시겠 습니까?")
while answer == "y":
   print("게임을 다시 하세요.")#재시작을 어떻게 하나요?
else:
    print("게임을 종료 합니다.")
