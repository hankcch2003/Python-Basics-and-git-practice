price = 35

# 使用 while 迴圈確保使用者輸入正確的格式
while True:
    try:
        # 讓使用者輸入購買的數量，並轉換為整數
        quantity = int(input('請輸入購買的數量：'))

        # 如果輸入成功，跳出迴圈
        break 
    except:
        # 如果使用者輸入的不是整數，則提示錯誤訊息並繼續要求輸入
        print('請輸入整數！')

# 利用整除運算子 // 算出總數中包含多少組「滿三瓶」，即為免費贈送的數量
free_count = quantity // 3

# 從購買總量中扣除免費的數量，得到使用者真正需要付錢的瓶數
paid_count = quantity - free_count

# 計算在完全沒有任何優惠活動下的原始總金額
original_total = quantity * price

# 以實際需要付錢的數量乘以單價，得出套用優惠後的最終支付金額
actual_total = paid_count * price

# 將原價減去實付金額，計算出這次消費總共節省了多少錢
saved = original_total - actual_total

# 輸出預先設定好的單件商品價格
print(f'單價: {price} 元')

# 輸出使用者輸入的總購買數量
print(f'購買數量: {quantity} 瓶')

# 輸出根據「買二送一」邏輯換算出的免費贈送數量
print(f'免費數量: {free_count} 瓶')

# 輸出若完全沒有優惠時應支付的原始總金額
print(f'原價總計: {original_total} 元')

# 輸出扣除免費瓶數後，實際需要支付的結帳金額
print(f'實付金額: {actual_total} 元')

# 輸出原價與實付金額的差額，即本次消費節省的錢
print(f'省下的金額: {saved} 元')