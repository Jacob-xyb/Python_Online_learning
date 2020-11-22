import random

secret = random.randint(1, 10)
print('----------我爱鱼工作室----------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字(1~9)：")
guess = int(temp)
count = 0
while 1:
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        break
    elif guess > secret:
        print("哥，大了大了~~~")
    else:
        print("嘿，小了，小了~~~")
    if count >= 2:
        print("老是猜不中，游戏结束，不玩啦^_^")
        break
    temp = input("猜错啦，继续猜吧：")
    guess = int(temp)
    count += 1
