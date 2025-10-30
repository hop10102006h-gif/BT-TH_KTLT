# Dương Phúc Hợp msv: 245752021610047
import numpy as np
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
dtype = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]
# Tạo mảng NumPy có cấu trúc
students = np.array(data, dtype=dtype)
# Sắp xếp theo lớp (class) và sau đó theo chiều cao (height)
sorted_students = np.sort(students, order=['class', 'height'])
# In kết quả
print(sorted_students)
