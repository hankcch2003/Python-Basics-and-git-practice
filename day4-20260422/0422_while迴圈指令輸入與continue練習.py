# 第一種寫法：標準迴圈
print("第一種寫法(標準迴圈)：")
while True:
    # 讀取使用者輸入的指令
    string = input('請輸入指令(輸入 q 離開)：')
    
    # 判斷是否輸入 q 以中斷迴圈
    if string.lower() == 'q':
        # 輸出結束提示
        print('謝謝光臨，再見！')
        break
        
    # 輸出使用者輸入的內容
    print(f'您輸入的字串為 {string}')
print()

# 第二種寫法：海象運算子
print("第二種寫法(海象運算子)：")

# 使用 := 同時進行輸入與條件判斷
while (string := input('請輸入指令(輸入 q 離開)：')).lower() != 'q':
    # 輸出使用者輸入的內容
    print(f'您輸入的字串為 {string}')

# 判斷為 q 跳出迴圈後輸出
print('謝謝光臨，再見！')
print()

# 輸出 1-100 間不能被 3 整除的所有數
count = 0 # 初始化計數器為 0
while count < 100: # 當計數器小於 100 時持續執行
    count += 1 # 每次迴圈將計數器加 1
    
    # 判斷是否能被 3 整除
    if count % 3 == 0:
        # 如果是 3 的倍數則跳過本次迴圈
        continue
        
    # 輸出符合條件的數字
    print(count)