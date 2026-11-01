import random
while True:
    secret = random.randint(1, 100)
    count = 0
    while True:
        guess = int (input("猜一个数字"))
        count +=1
        if guess == secret:
            print(f"你猜对了 使用了 {count} 次")
            break
        elif guess > secret:
            print("猜大了你个扎啤")
        else:
            print("猜小了你个扎啤")
    again = input("你个扎啤要再来一遍吗(y / n)")
    if again != "y":
        break