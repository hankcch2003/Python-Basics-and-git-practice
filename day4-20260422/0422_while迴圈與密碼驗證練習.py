count = 1 # 設定計數器初始值為 1
while count <= 5: # 當計數器小於或等於 5 時持續執行
    print(f'目前數到 {count}') # 輸出當前的數字
    count += 1 # 每次迴圈將計數器加 1
print('數完了！') # 迴圈結束後輸出提示
print()

# 第一種寫法：標準迴圈
print("第一種寫法(標準迴圈)：")
password = "" # 初始化密碼變數
while password != "python": # 當密碼不等於 python 時持續執行
    password = input('請輸入密碼：') # 讀取使用者輸入的密碼
    if password != 'python': # 判斷輸入是否錯誤
        print('密碼錯誤，請再試一次') # 輸出錯誤提示
print('密碼正確，歡迎登入！') # 密碼正確後輸出歡迎字樣
print()

# 第二種寫法：海象運算子
print("第二種寫法(海象運算子)：")
# 使用 := 同時進行輸入賦值與條件判斷
while (password := input('請輸入密碼：')) != "python":
    # 密碼錯誤時執行
    print('密碼錯誤，請再試一次')
print('密碼正確，歡迎登入！') # 條件不成立跳出迴圈，輸出歡迎字樣