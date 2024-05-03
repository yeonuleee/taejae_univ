import random

def roll_dice():
    return random.randint(1, 6)

player_number = int(input("플레이어 수를 입력해 주세요."))

player_list = []
for i in range(1, player_number+1):
    player = input("플레이어 이름을 입력해 주세요.")
    player_list.append(player)

print("주사위를 굴려 봅시다!")

players_numbers = []
for i in range(0, player_number):
    player_numbers = roll_dice()
    players_numbers.append(player_numbers)
    print(f"{player_list[i]}의 주사위 결과는 " + f"{players_numbers[i]}입니다.")


print("가장 높은 수가 나온 플레이어는 " + f"로, " + str(max(players_numbers)) + "이/가 나왔습니다.")
#가장 높은 점수가 나온 플레이어를 어떻게 구하나요?
answer = input("게임을 계속 하시겠 습니까?")
if answer == "y":
   print("게임 다시 하세요.") #재시작 어떻게 하나요......?
else:
    print("게임을 종료 합니다.")
