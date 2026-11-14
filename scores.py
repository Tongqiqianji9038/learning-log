def average(scores):
    return sum(scores) / len(scores)

def highest(scores):
    return max(scores)

def lowest(scores):
    return min(scores)

scores = []
while True:
    text = input("请输入你的成绩（end 结束）: ")
    if text == "end":
        break
    scores.append(float(text))
if len(scores) == 0:
    print("没有成绩喵")
else:
    print(f"共 {len(scores)} 个成绩")
    print(f"平均分:{average(scores):.2f}")
    print(f"最高分:{highest(scores)}")
    print(f"最低分:{lowest(scores)}")