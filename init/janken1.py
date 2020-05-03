import random

print('ジャンケンを始めます。最初はグー！ジャンケンぽん！\n数字を入力してください：1:グー/2:チョキ,/3:パー')
number = [1, 2, 3]
print("あなたの手は：")
yourChoise = int(input())
roboChoise = (random.choice(number))
print(roboChoise)

if yourChoise == roboChoise:
    print("あいこです。")

elif yourChoise == 1 and roboChoise == 2 or yourChoise == 2 and roboChoise == 3 or yourChoise == 3 and roboChoise == 1:
    print("あなたの勝ちです。")

else:
    print("あなたの負けです。")