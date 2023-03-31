import random

# 生成0-100之间的随机整数
answer = random.randint(0, 100)

# 最多猜10次
for i in range(10):
    guess = int(input("请猜一个0-100之间的数字："))
    if guess == answer:
        print("恭喜你猜对了！")
        break
    elif guess < answer:
        print("你猜的数字太小了。")
    else:
        print("你猜的数字太大了。")

# 如果猜了10次还没猜对，就告诉用户正确答案
if guess != answer:
    print("很遗憾，你没有猜对。正确答案是：", answer)