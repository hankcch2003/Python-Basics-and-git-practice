# 顯示目前的 __name__ 變數內容
print(f'這個檔案的 __name__ 是：{__name__}')

# 定義招呼語函數
def greet(name):
    # 輸出歡迎訊息
    print(f'您好，{name}！')

# 判斷檔案是否為直接執行（非作為模組匯入）
if __name__ == '__main__':
    # 檔案直接執行時才會輸出的內容
    print('這個檔案被直接執行')

    # 呼叫 greet 函數
    greet('小明')