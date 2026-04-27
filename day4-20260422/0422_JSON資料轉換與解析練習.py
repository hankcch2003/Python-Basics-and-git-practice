import json

student = {
    'name': '小明',
    'age': 18,
    'scores': [85, 89, 95]
}

# 使用 json.dumps() 將 python 物件轉成 json 字串
# ensure_ascii = False 確保中文不被轉碼，indent = 2 進行縮排美化
json_string = json.dumps(student, ensure_ascii = False, indent = 2)

# 輸出轉換後的 json 字串
print(json_string)
print()

# 使用 json.loads() 將 json 字串轉回 python 物件
# 將剛才產生的字串還原為字典格式
data = json.loads(json_string)

# 輸出還原後的物件內容
print('還原後的字典資料：')
print(data)
print()

# 存取還原後字典中的特定欄位
print(f"學生姓名：{data['name']}")

# 取得學生的姓名與第一筆成績
print(f"第一門學科成績：{data['scores'][0]}")