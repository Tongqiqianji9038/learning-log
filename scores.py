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
    print(f"平均分:{sum(scores) / len(scores):.2f}")
    print(f"最高分:{max(scores)}")
    print(f"最低分:{min(scores)}")