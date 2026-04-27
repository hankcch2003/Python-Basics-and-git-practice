student = {
    'name': '小明',
    'age': 25,
    'grade': 'A',
    'is_active': True
}

# 用鍵值取值
print(student['name']) # 取得鍵 name 的值
print(student['age']) # 取得鍵 age 的值

# 取得鍵 grade 的值
print(student['grade'])

# 修改值
student['age'] = 50 # 修改年齡為 50
print(student['age'])

# 將 is_active 值改為 False
student['is_active'] = False
print(student['is_active'])

# 新增鍵值對（電子郵件）
student['email'] = 'james@gmail.com'
print(student)

# 新增鍵（tel 值：0912345678）
student['tel'] = '0912345678'
print(student)