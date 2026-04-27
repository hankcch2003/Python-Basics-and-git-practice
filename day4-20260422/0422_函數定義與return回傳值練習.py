# 自定義函數：招呼語練習
def greeting(name):
    # 輸出歡迎訊息
    print(f'您好，{name}！歡迎來到 Python 的世界')

# 呼叫 greeting 函數
greeting('小明')
greeting('小王')
greeting('小美')
print()

# 將加總程式改為呼叫函數（直接輸出型）
def get_sum(n):
    # 初始化總和變數為 0
    total = 0

    # 遍歷從 1 到 n 的數列
    for x in range(1, n + 1):
        # 累加每個數字
        total += x

    # 輸出最終加總結果
    print(f'1 + 2 + 3 + ... + {n} = {total}')

# 呼叫 get_sum 函數進行不同範圍的加總
get_sum(10)
get_sum(50)
get_sum(100)
print()

# 使用 return 回傳值的加總函數
def calc(max_num):
    # 初始化總和變數為 0
    total_sum = 0
    
    # 遍歷從 1 到指定的最大值
    for x in range(max_num + 1):
        # 累加每個數字
        total_sum += x
        
    # 回傳加總後的結果
    return total_sum

# 呼叫 calc 函數並輸出回傳結果
print(f'1 + 2 + 3 + ... + 10 = {calc(10)}')
print(f'1 + 2 + 3 + ... + 50 = {calc(50)}')
print(f'1 + 2 + 3 + ... + 100 = {calc(100)}')