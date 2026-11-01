import random
secret = random.randint(1,100)
while True:
    guess = int(input("猜数字游戏开始了喵，请猜取一个数字"))
    if guess == secret:
        print("猜对了喵！")
        break
    elif guess > secret:
        print("猜大了")
    else:
        print("猜小了")