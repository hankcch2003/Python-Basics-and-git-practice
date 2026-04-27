# 寫入檔案：在指定路徑建立 note.txt 並寫入文字內容
# encoding = 'utf8' 確保中文能正確存取不產生亂碼
with open(r'E:\Python\Python基礎入門\20260422\note.txt', 'w', encoding = 'utf-8') as f1:
    f1.write('這是我的第一個檔案\n')
    f1.write('Python 好好玩\n')
    f1.write('今天天氣很好')
print('檔案寫入完成！')
print()

# 開啟檔案：讀取指定路徑檔案的全部內容
# 讀取時也需指定 encoding = 'utf8' 確保中文能正確存取不產生亂碼
with open(r'E:\Python\Python基礎入門\20260422\note.txt', 'r', encoding = 'utf-8') as f2:
    content = f2.read() # 讀取檔案所有文字
print('檔案的內容：')
print(content)
print()

# 開啟檔案逐行讀取：從指定路徑讀取並加入行號
with open(r'E:\Python\Python基礎入門\20260422\note.txt', 'r', encoding = 'utf-8') as f2:
    # 遍歷檔案內容並自動產生行號
    for line_number, content in enumerate(f2, 1):
        # 輸出第幾行內容並去除多餘換行
        print(f'第 {line_number} 行：{content.strip()}')
print()

# 以二進位模式拷貝 funny.mpg 到 movie.mpg
# 二進位檔案（如影片、圖片）不需要指定 encoding
with open(r'E:\Python\Python基礎入門\20260422\funny.mpg', 'rb') as source:
    with open(r'E:\Python\Python基礎入門\20260422\movie.mpg', 'wb') as destination:
        # 遍歷讀取來源檔案內容並寫入目標檔案
        destination.write(source.read())
print('影片拷貝完成！')