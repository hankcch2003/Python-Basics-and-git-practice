print("Hello, Python!")

a, b, c = 11, 55, 99
print(a, b, c)
print(a, b, c, sep = ',') # 設定輸出物件間的分隔字元

print("first line")
print("second line")
print("third line")

print("first line", end = ' ') # 設定結尾字元，可用於串接輸出
print("second line", end = ' ')
print("third line")

with open('ok.txt', 'w', encoding = 'utf-8') as f:
    print("今天天氣很好, 終端機")
    print("今天天氣很好, 輸出到檔案", file = f)

import math
print()
print(math.pi) 
print(math.ceil(math.pi)) # 無條件進位至最接近整數
print(math.floor(math.pi)) # 無條件捨去至最接近整數

from math import pi, ceil, floor
print()
print(pi)
print(ceil(pi)) # 無條件進位至最接近整數
print(floor(pi)) # 無條件捨去至最接近整數

print()
# 採用「銀行家捨入法」：小數點後為 .5 時，捨入到最近的「偶數」
print(round(3.12)) 
print(round(3.52)) 
print(round(3.62)) 
print(round(4.12)) 
print(round(4.5))  # 輸出 4（向最近的偶數 4 捨入）
print(round(3.5))  # 輸出 4（向最近的偶數 4 捨入）
print(round(4.62)) 
print("=" * 50) 

import random
print()
print(list(range(1, 6))) # 產生一個從 1 到 5 的整數串列
lotto = random.sample(range(1, 50), 6) # 從範圍內隨機取出「不重複」樣本
lotto.sort() # 原地排序(由小到大)，並會直接修改原串列順序
print(lotto)

print()
name = "Hank"
age = 23
height = 164.3
print('name', type(name)) # 查詢物件的資料型別
print('age', type(age))
print('height', type(height))
print('name', name.__class__) # 查詢物件所屬的類別（底層屬性）
print('age', age.__class__)
print('height', height.__class__)

import keyword
print()
print("所有保留字:", keyword.kwlist) # 輸出所有系統保留字
print("=" * 100)
print(keyword.iskeyword('if')) # 檢查字串是否為系統保留字
print(keyword.iskeyword('If'))

print()
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) # 整除運算（只取商數）
print(10 % 3)  # 取餘數運算
print(10 ** 3) # 次方運算
print('10' + '3')
print('10' + str(3)) # 不同型別相加須先轉型
print('10' * 3)
print('周杰倫' * 100) # 字串重複運算
print(2 ** 3 + 1)
print(2 ** (3 + 1))

print()
score = 100
score = score + 50 
print("score = ", score)
print("score = ", score, sep = '')
print(f'{score = }') # 自動輸出「變數名 = 值」
score += 50 
print(f'{score = }')

print()
total_minutes = int(input("請輸入停車的總分鐘數: "))
money_per_hour = 30
max_fee = 200
hours = total_minutes // 60
minutes = total_minutes % 60

# 判斷式邏輯：超過 30 分鐘進位一小時
if minutes > 30:
    hourstotal = hours + 1
else:
    hourstotal = hours

total = hourstotal * money_per_hour

# 判斷式邏輯：檢查是否超過最高費用
if total > max_fee:
    total = max_fee

print(f'停車時間: {hours} 小時 {minutes} 分鐘')
print(f'計費時數為 {hourstotal} 小時')
print(f'應繳金額為 {total} 元')