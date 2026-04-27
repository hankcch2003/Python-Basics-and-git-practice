student = {
    'name': '小明',
    'age': 25,
    'grade': 'A',
    'is_active': True,
    'city': '台北'
}

# 使用 get 方法，當鍵不存在時不會報錯
print(student.get('phone', '未提供')) # 取得不存在的鍵 phone

# 利用 get 方法取得 key city 的值
# 若值不存在則顯示「不存在」
print(student.get('city', '不存在'))

# 檢查 key 值是否存在
print('name' in student) # 檢查 name 是否在字典中
print('phone' in student) # 檢查 phone 是否在字典中

# 檢查 city 是否存在
print('city' in student)
print()

# 刪除鍵值對
del student['grade'] # 刪除成績鍵值對
print(student)

# 刪除 age 的鍵值對
del student['age']
print(student)
print()

# keys() 取得所有的 key 值
print(student.keys()) # 輸出字典中所有的鍵

# values() 取得所有的 value 值
print(student.values()) # 輸出字典中所有的值
print()

# items() 取得所有的 key, value
# 透過 for 迴圈遍歷字典的鍵與值
for k, v in student.items():
    print(f'key: {k}, value: {v}')