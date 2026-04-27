score = [] # 初始化成績清單
for i in range(1, 6): # 遍歷 1 到 5 位同學
    # 讀取使用者輸入的成績並加入清單
    score.append(int(input(f'請輸入第 {i} 位同學的成績：')))

# 計算成績平均值
average = sum(score) / len(score)

# 輸出統計結果
print()
print(f'所有成績：{score}')
print(f'成績平均：{average:.1f}')
print(f'成績最高分：{max(score)}')
print(f'成績最低分：{min(score)}')
print()

import random

# 產生 1 到 100 之間的隨機目標數字
target = random.randint(1, 100)

while True:
    # 讀取使用者猜測的數字
    guess = int(input('請輸入您猜的數字：'))

    # 判斷猜測結果
    if guess > target:
        # 猜測數字太大的提示
        print('太大了，再小一點！')
    elif guess < target:
        # 猜測數字太小的提示
        print('太小了，再大一點！')
    else:
        # 猜對時跳出迴圈
        print('答對了，恭喜您！')
        break