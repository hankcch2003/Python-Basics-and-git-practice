# 開啟無限迴圈，直到使用者主動輸入 0 才會停止
while True:
    # 讓使用者輸入成績並轉換為整數
    score = int(input('請輸入成績 (輸入 0 結束)：'))
    
    # 檢查是否觸發結束條件：若輸入為 0 則跳出迴圈
    if score == 0:
        break
    
    # 初始化等級變數，準備存放字母 A-E
    level = ''
    
    # 判斷成績級距
    # 這裡利用 elif 的特性，只要符合前面的條件，後面的就不會執行
    if score >= 90:
        level = 'A'      # 90 分以上等級為 A
    elif score >= 80:
        level = 'B'      # 80 ~ 89 分等級為 B
    elif score >= 70:
        level = 'C'      # 70 ~ 79 分等級為 C
    elif score >= 60:
        level = 'D'      # 60 ~ 69 分等級為 D
    else:
        level = 'E'      # 60 分以下等級為 E
    
    # 輸出最終的成績與等級判斷結果
    print(f'您的成績為 {score} 分，等級為 {level}')