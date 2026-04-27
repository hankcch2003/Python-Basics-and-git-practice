# BMI 計算公式：體重(kg) / 身高(m) 的平方
height_cm = float(input('請輸入身高(公分)：'))
weight = float(input('請輸入體重(公斤)：'))

# 將公分單位轉換為公尺，以符合 BMI 公式標準
height_m = height_cm / 100

# 使用 ** 運算子進行平方運算，求出 BMI 值
bmi = weight / (height_m ** 2)

# :.1f -> 格式化輸出至小數點後第一位（自動四捨五入）
print(f'您的 BMI 是: {bmi:.1f}')