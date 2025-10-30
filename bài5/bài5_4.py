# Dương Phúc Hợp msv: 245752021610047
import numpy as np

mang_goc = np.arange(12, 38)

# In mảng gốc
print("Mảng được tạo:")
print(mang_goc)

# 2. Đảo ngược mảng bằng cách sử dụng slicing (lát cắt) với bước nhảy -1
# Cú pháp [::-1] nghĩa là:
# Bắt đầu từ đầu (trống) : kết thúc ở cuối (trống) : với bước nhảy -1 (đi ngược)
mang_dao_nguoc = mang_goc[::-1]

# In mảng đảo ngược
print("\nMảng đảo ngược:")
print(mang_dao_nguoc)