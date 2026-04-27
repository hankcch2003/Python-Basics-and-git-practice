numbers = list(range(10))
print(f'{numbers = }')

# 輸出 5 是否存在於列表中（若存在回傳 True，否則回傳 False）
print(f'5 有沒有在列表中？ {5 in numbers}')

# 輸出 15 是否存在於列表中（若存在回傳 True，否則回傳 False）
print(f'15 有沒有在列表中？ {15 in numbers}')

# append: 將單一元素（數字 10）加到列表的最末端
numbers.append(10)
print(f'{numbers = }')

n2 = [99, 100, 101]

# append 新增列表時，會將其視為「單一個元素」而不拆開內容
numbers.append(n2)
print(f'{numbers = }')

# 輸出目前列表的長度（計算元素總個數）
print(f'長度為 {len(numbers)}')

# pop: 依照「索引值」移除元素（此處移除索引 3 的位置）
numbers.pop(3) 

# pop 括號內不填則預設移除「最後一個」元素
numbers.pop() 
print(f'{numbers = }')

# extend: 將另一個列表的內容「拆解」後，逐一新增至末端
numbers.extend(n2)
print(f'{numbers = }')

# 輸出經 extend 合併後的列表新長度
print(f'長度為 {len(numbers)}')

# remove: 依照「元素名稱」進行刪除，若有重複則刪除第一個遇到的
numbers.remove(100)
print(f'{numbers = }')

# insert: 在指定的索引位置「插入」特定元素
numbers.insert(3, 3)
print(f'{numbers = }')

# index: 查詢特定元素在列表中第一次出現的索引位置
print(f'10 的索引值為 {numbers.index(10)}')

# count: 統計特定元素在列表中出現的總次數
print(f'10 有 {numbers.count(10)} 個')

import random

# random.sample: 從 1-49 範圍內隨機取出 6 個不重複的數字組成列表
lotto1 = random.sample(range(1, 50), 6)
print(f'樂透開獎號碼為 {lotto1}')

# sort: 對原列表進行由小到大的排序，會直接改寫記憶體 (inplace)
lotto1.sort()
print(f'從小到大排序為 {lotto1}')

# sort(reverse = True): 進行由大到小的反向排序
lotto1.sort(reverse = True)
print(f'從大到小排序為 {lotto1}')

lotto2 = random.sample(range(1, 50), 6)
print(f'{lotto2 = }')

# sorted: 產生一個「排序後的新列表」，原本的列表順序不變
print('從小到大為', sorted(lotto2))

# sorted 搭配反向排序參數
print('從大到小為', sorted(lotto2, reverse = True))

# reversed: 反轉列表順序，並將其結果轉換回 list 格式輸出
print(f'反轉結果為 {list(reversed(lotto2))}')

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 列表合併：使用 + 號進行接龍，產生新列表
combined = list_a + list_b
print(f'{combined = }')

# 輸出將列表內容重複複製 5 次後的結果
print(f'重複 5 次的結果為 {list_a * 5}')

# 使用 sum 函式輸出列表內所有數值的加總
print(f'列表總和為 {sum(list_a)}')

# 使用 max 函式輸出列表中的最大數值
print(f'最大值為 {max(list_a)}')

# 使用 min 函式輸出列表中的最小數值
print(f'最小值為 {min(list_a)}')

# dir: 輸出系統環境中所有內建屬性與函式的名稱清單
print(f'系統內建屬性清單為 {dir(__builtins__)}')

func_list = []

# 利用 for 迴圈遍歷所有內建名稱
for x in dir(__builtins__):
    # 邏輯篩選：僅保留名稱為「全小寫」且「非底線開頭」的函式
    if x.islower() and not x.startswith('_'):
        # 將符合條件的名稱加入新列表
        func_list.append(x)

# 輸出最終篩選過後的常用內建函式清單
print(f'篩選後的小寫函式清單為 {func_list}')