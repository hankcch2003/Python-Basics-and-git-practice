fruits = ['蘋果', '香蕉', '橘子']
numbers = list(range(10))  # 產生 0 到 9 的整數列表
mixed = ['hello', 42, 3.14, True]

# 輸出變數名稱與內容，這在 Python 3.8 之後是非常方便的除錯寫法
print(f'{fruits = }')
print(f'{numbers = }')
print(f'{mixed = }')

# 輸出利用 len 函式取得的列表元素總個數
print(f'numbers 的長度為 {len(numbers)}')

# 輸出透過索引 1 抓取的第二個元素（電腦計數從 0 開始）
print(f'fruits 第二個元素為{fruits[1]}')

# 輸出透過索引 0 抓取的清單最開端資料
print(f'numbers 第一個元素為 {numbers[0]}')

# 輸出最後一個元素：方法一（利用總長度減 1）
print(f'mixed 最後一個元素為 {mixed[len(mixed) - 1]}')

# 輸出最後一個元素：方法二（利用負索引 -1 直接指向結尾）
print(f'mixed 最後一個元素為 {mixed[-1]}')

# 輸出從索引 2 開始切到最後的所有元素內容
print(f'numbers 從索引為 2 到最後的元素為 {numbers[2:]}')

# 輸出從索引 2 到 5 的切片（包頭不包尾，結尾需設為 6）
print(f'numbers 從索引為 2 到 5 的結果為 {numbers[2:6]}')

# 輸出利用切片語法 [::-1] 產生的反轉副本（原本的列表不變）
print(f'numbers 反轉的結果為 {numbers[::-1]}')

# 輸出利用 reversed 函式產生的反轉內容（需轉為 list 格式）
print(f'numbers 反轉用 reversed 函式的結果為 {list(reversed(numbers))}')

# 輸出利用 reverse 方法原地修改 (inplace) 後的列表內容
numbers.reverse() 
print(f'numbers 反轉用 reverse 方法的結果為 {numbers}')