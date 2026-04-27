import time

# 讓使用者輸入秒數並將字串轉換為整數型別
seconds = int(input('請輸入秒數：'))

# 開啟迴圈，只要秒數大於或等於 0 就會持續輸出倒數進度
while seconds >= 0:
    
    # 利用整除運算子 // 換算出總秒數包含的「整數分鐘」
    minutes = seconds // 60

    # 利用取餘數運算子 % 換算出扣除分鐘後「剩下的秒數」
    remaining_seconds = seconds % 60
    
    # 輸出技巧：\r 使游標回到行首，搭配 end = '' 讓下一次輸出覆蓋舊內容，達成原地更新
    # :02d 格式化確保數值恆為二位數，不足時自動在前面補 0
    print(f'\r倒數計時: {minutes:02d} 分 {remaining_seconds:02d} 秒', end = '')
    
    # 每次迴圈執行結束前將總秒數遞減 1，作為控制時間流逝的機制
    seconds -= 1
    
    # 調用時間模組的 sleep 函式，讓程式強制暫停 1 秒，精確對齊現實時間
    time.sleep(1)

# 當秒數扣至負數跳出迴圈後，輸出最終的結束提示
print('\n時間到！')