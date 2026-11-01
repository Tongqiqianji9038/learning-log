import random
while True:
    secret = random.randint(1,100)
    count = 0
    while True:
        guess = int(input("猜取一个数字喵"))
        count +=1
        if guess == secret:
            print(f"你猜对了，你使用了 {count} 次")
            break
        elif guess > secret:
            print("猜大了喵")
        else:
            print("猜小了喵")
    again = input("要再来一局吗喵 (y/n)")
    if again != "y":
        break