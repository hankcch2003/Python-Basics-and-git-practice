# 遍歷串列元素
fruits = ['蘋果', '香蕉', '橘子', '鳳梨'] # 定義水果清單
for i in fruits: # 遍歷讀取清單中的每個元素
    print(f'我喜歡吃 {i}') # 輸出喜愛的水果
print()

# 遍歷字串：依序印出字元
for s in "python is simple": # 遍歷讀取字串中的每個字母
    print(s) # 輸出單個字元
print()

# 遍歷從 0 到結束值前一位
for i in range(10): # 遍歷 0 到 9 的數列
    print(f'i = {i}') # 輸出當前的 i 值
print()

# 遍歷設定起始值與結束值
for i in range(1, 7): # 遍歷 1 到 6 的數列
    print(f'i = {i}') # 輸出當前的 i 值
print()

# 遍歷設定間隔值
for i in range(1, 10, 2): # 遍歷 1, 3, 5, 7, 9 的奇數數列
    print(f'i = {i}') # 輸出當前的 i 值
print()

# 遍歷遞減數列
for i in range(10, 0, -1): # 遍歷 10 到 1 的遞減數列
    print(f'i = {i}') # 輸出當前的 i 值
print()

# 利用迴圈遍歷計算 1 + 2 + 3 + ... + 10 的總和
sum_value = 0 # 初始化累加變數為 0
for i in range(1, 11): # 遍歷產生 1 到 10 的數列
    sum_value += i # 將目前的數字累加到總和中

    # 輸出累加過程
    print(f'目前加到 {i}，累計總和為 {sum_value}')

# 輸出最終結果
print(f'1 加到 10 的最終總和為 {sum_value}')
print()

# 計算 1 到 100 的總和
sum_total = 0 # 初始化總和變數為 0
for x in range(1, 101): # 遍歷 1 到 100 的數列
    sum_total += x # 累加每個數字

# 輸出結果
print(f'1 加到 100 的總和為 {sum_total}')