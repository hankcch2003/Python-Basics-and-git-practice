students = [
    {'name': '小明', 'score': 85},
    {'name': '小華', 'score': 92},
    {'name': '小美', 'score': 78}
]

# 遍歷學生清單並輸出姓名與分數
for student in students:
    # 輸出單一學生的姓名與分數
    print(f"{student['name']}：{student['score']} 分")

# 初始化總分變數為 0
total = 0
for student in students:
    # 遍歷清單並累加每位學生的分數
    total += student['score']

# 計算平均值
average = total / len(students)
print(f'班級平均分數：{average:.1f} 分')
print()

student = {
    'name': '小明',
    'subject': ['國文', '英文', '數學'],
    'score': [88, 85, 66]
}

# 輸出特定學生的成績標題
print(f"{student['name']}的各科成績：")

# 使用 range 遍歷索引值以對應學科與分數
for i in range(len(student['subject'])):

    # 取得當前遍歷到的學科名稱與分數
    subject = student['subject'][i]
    score = student['score'][i]

    # 格式化輸出各科成績
    print(f'{subject}：{score} 分')
print()

# 使用 zip 同時遍歷多個清單
for x, y in zip(student['subject'], student['score']):
    # 遍歷並輸出學科名稱與對應的分數
    print(f'{x}：{y} 分')