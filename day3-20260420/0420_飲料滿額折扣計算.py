drink_name = input('請輸入飲料名稱：')
price = int(input('請輸入單價(元)：'))
quantity = int(input('請輸入數量：'))

# 計算原始總額，作為後續折扣判定的基準
total = price * quantity

# 定義四捨五入計算工具，確保金額計算符合一般商業邏輯 
# 解決 Python 內建 round() 在處理 .5 時會趨向偶數的特性 (Banker's Rounding)
def round(n):
    return int(n + 0.5)

# 執行消費門檻判定：滿 100 元即享有 9 折優惠
if total >= 100:
    # 套用折扣公式並進行四捨五入取整
    discount_total = round(total * 0.9) 
    
    # 計算原價與折扣價的差額
    saved = total - discount_total
    
    # 輸出原始總金額
    print(f'原價為 {total} 元')

    # 輸出折扣後的最終支付金額
    print(f'滿百打 9 折，實付 {discount_total} 元')

    # 輸出本次消費省下的錢
    print(f'現省 {saved} 元')

# 處理未達優惠門檻的情況，並提供行銷提示
else:
    # 輸出原始總金額
    print(f'總金額為 {total} 元')

    # 輸出尚未達標的優惠提醒
    print(f'滿 100 元，可享 9 折優惠喔！')