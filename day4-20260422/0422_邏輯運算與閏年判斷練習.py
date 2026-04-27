# or 只要有一個條件成立即成立
print(10 < 3 or 10 < 3) # 條件皆不成立，輸出 False
print(10 < 3 or 10 > 3) # 右邊條件成立，輸出 True
print(10 > 3 or 10 < 3) # 左邊條件成立，輸出 True
print(10 > 3 or 10 > 3) # 條件皆成立，輸出 True
print()

# and 全部條件皆需成立才成立
print(10 < 3 and 10 < 3) # 條件皆不成立，輸出 False
print(10 < 3 and 10 > 3) # 其中一邊不成立，輸出 False
print(10 > 3 and 10 < 3) # 其中一邊不成立，輸出 False
print(10 > 3 and 10 > 3) # 條件皆成立，輸出 True
print()

# not 顛倒
print(10 > 3) # 原始條件為 True
print(not 10 > 3) # 反轉後輸出 False
print()

# 第一種寫法：巢狀判斷
print("第一種寫法(巢狀判斷)：")
while True:
    # 讀取使用者輸入的年份
    year = int(input('請輸入西元年份(輸入 0 結束)：'))
    
    # 如果輸入為 0 則結束迴圈
    if year == 0:
        break
        
    # 判斷西元年份是否為閏年
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # 能被 400 整除為閏年
                print(year, "是閏年")
            else:
                # 能被 100 整除但不能被 400 整除為平年
                print(year, "不是閏年")
        else:
            # 能被 4 整除但不能被 100 整除為閏年
            print(year, "是閏年")
    else:
        # 不能被 4 整除為平年
        print(year, "不是閏年")
print()

# 第二種寫法：邏輯運算子
print("第二種寫法(邏輯運算子)：")
while True:
    # 讀取使用者輸入的年份
    year = int(input('請輸入西元年份(輸入 0 結束)：'))
    
    # 如果輸入為 0 則結束迴圈
    if year == 0:
        break

    # 使用邏輯運算子簡化判斷
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # 符合條件輸出閏年
        print(year, "是閏年")
    else:
        # 不符合條件輸出不是閏年
        print(year, "不是閏年")