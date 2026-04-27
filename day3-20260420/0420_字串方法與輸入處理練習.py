url = "httpS://www.pcschool.COM.TW"
email = "amacollege168@gmail.com"

# 輸出將字串全部轉換為大寫的結果
print(f'upper: {url.upper()}')

# 輸出將字串全部轉換為小寫的結果
print(f'lower: {url.lower()}')

# 輸出以 "@" 作為分隔點切割後的字串清單 (List)
print(f'split: {email.split("@")}')

# 輸出先轉小寫後，將所有的 "o" 替換為 "python" 的結果
print(f'replace: {url.lower().replace("o", "python")}')

# 輸出在 email 的每個字元之間插入 "-" 符號後的長字串
print(f'join: {"-".join(email)}')

print("=====================================")
data = ['python', 'is', 'a', 'simple', 'language']

# 輸出將 data 列表中的元素以「空格」連接後的完整句子
sentence = " ".join(data)
print(f'將列表轉字串: {sentence}')

# 輸出尋找子字串 "oo" 出現的索引位置（若找不到則輸出 -1）
print(f'find: {url.find("oo")}')

# 輸出計算 email 中字元 "m" 出現的總次數
print(f'count: {email.count("m")}')

# 輸出判斷網址是否以 "http" 作為開頭的布林值
print(f'startswith: {url.startswith("http")}')

# 輸出判斷網址轉小寫後是否以 "tw" 結尾的布林值
print(f'endswith: {url.lower().endswith("tw")}')

# 透過迴圈與錯誤處理確保使用者輸入正確格式的數字
while True:
    try:
        # 輸出請求並同時將輸入的兩組字串轉為整數存入變數
        no1, no2 = map(int, (input('請輸入二個數字，以空白隔開：').split()))
        break
    except ValueError:
        # 輸出輸入格式錯誤時的提示訊息
        print('錯誤：請確保輸入的是兩個整數數字！')

# 使用三元運算子快速判定並輸出兩數中的較大值
max_val = no1 if no1 > no2 else no2
print(f'二數: {no1, no2} 中, 最大數是: {max_val}')

test = ['www', 'pcsChool', 'cOm', 'tw']
print("=====================================")

# 輸出將列表元素以 "." 號結合後存入 url 變數的結果
url = '.'.join(test)
print(f'結合後的網址為 {url}')

# 輸出將網址轉為小寫後統計字元 "o" 出現次數的結果
print(f'o 共出現的次數為 {url.lower().count("o")} 次')

# 輸出判斷該網址是否由 "www" 開頭的布林值
print(f'是否由 www 開頭: {url.startswith("www")}')

# 輸出判斷該網址是否由 "tw" 結尾的布林值
print(f'是否由 tw 結尾: {url.endswith("tw")}')

# 輸出將網址轉大寫後，統一將 "C" 字元替換為 "X" 的結果
print(f'將 C 以 X 取代的結果為 {url.upper().replace("C", "X")}')