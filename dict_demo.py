scores = {"张三" : 85 , "李四" : 92 , "王五" : 78}

for name in scores:
	print(name, scores[name])

print("---")

for name, score in scores.items():
	print(f"{name}: {score}")