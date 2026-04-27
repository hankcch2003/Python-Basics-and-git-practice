# 預設參數：為參數設定預設值
def greet(name, greeting = '您好'):
    # 輸出問候語，若未傳入 greeting 則使用預設值
    print(f'{greeting}，{name}！')

# 呼叫函數，僅傳入姓名（使用預設問候語）
greet('小明')

# 呼叫函數，傳入姓名與自訂問候語
greet('小明', 'hello')
greet('小明', 'good morning')
print()

# 回傳多個值：分析成績並回傳統計結果
def analyze_scores(scores):
    # 取得最高分
    highest = max(scores)

    # 取得最低分
    lowest = min(scores)

    # 計算平均分數
    average = sum(scores) / len(scores)
    
    # 同時回傳三個統計值
    return highest, lowest, average

# 定義成績清單
score = [85, 93, 78, 95, 88]

# 接收回傳的多個值
high, low, avg = analyze_scores(score)

# 輸出統計結果
print(f'最高分：{high} 分')
print(f'最低分：{low} 分')
print(f'平均分：{avg:.1f} 分')