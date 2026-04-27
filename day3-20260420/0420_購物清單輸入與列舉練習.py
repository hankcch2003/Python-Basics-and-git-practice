# 初始化一個空的購物清單列表
shopping_list = []

# 讓使用者輸入想要購買的總數量並轉換為整數
no = int(input('請輸入數量：'))

# 使用 range(no) 建立迴圈，根據指定的次數重複執行
for x in range(no):

    # 讓使用者輸入商品名稱，並利用 f-string 顯示目前是第幾項
    item = input(f'請輸入第 {x + 1} 項名稱：')

    # 將輸入的商品名稱新增至 shopping_list 列表的最末端
    shopping_list.append(item)

# 輸出提示文字
print('以下為您要購買的所有項目:')

# 使用 enumerate 同時取得索引值 (i) 與商品內容 (x)
# 因為索引從 0 開始，所以輸出時使用 i + 1 顯示為第 1 項、第 2 項
for i, x in enumerate(shopping_list):
    # 輸出最終的購物清單明細
    print(f'第 {i + 1} 項: {x}')