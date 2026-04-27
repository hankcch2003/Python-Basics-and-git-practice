import json

students = [
    {'name': '小明', 'age': 18, 'score': 85},
    {'name': '小美', 'age': 20, 'score': 95},
    {'name': '大同', 'age': 25, 'score': 65}
]

# 使用 json.dump() 將資料存入 json 檔
# ensure_ascii = False 確保中文不變亂碼，indent = 2 進行格式美化
with open('students.json', 'w', encoding = 'utf8') as f:
    # 將 python 物件轉換並寫入檔案
    json.dump(students, f, ensure_ascii = False, indent = 2)
print('儲存成功！')
print()

# 用 json.load() 從 JSON 檔案讀取資料
# encoding = 'utf8' 確保中文能正確存取不產生亂碼
with open("students.json", "r", encoding = "utf8") as f:
    # 將檔案內容轉回為 python 物件
    students_data = json.load(f)

# 輸出讀取到的學生總數
print(f"共有 {len(students_data)} 位學生：")
print()

# 遍歷讀取後的學生清單並輸出詳細資訊
for student in students_data:
    # 格式化輸出每位學生的姓名、年齡與成績
    print(f"{student['name']}，{student['age']} 歲，成績 {student['score']} 分")