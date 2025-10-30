# Dương Phúc Hợp msv: 245752021610047
def sort_list(lst):
    # hàm sắp xếp dãy tăng dần
    return sorted(lst)
def find_max(lst):
    # hàm tìm phần tử lớn nhất
    return max(lst)
def find_min(lst):
    # hàm tìm phần tử bé nhât
    return min(lst)
# Chương trình chính
n = int(input('nhập số lượng phần tử: '))
lst = []
for i in range(n):
    value = float(input(f'nhập phần tử thứ i+1: '))
    lst.append(value)
sorted_lst = sort_list(lst)
max_value = find_max(lst)
min_value = find_min(lst)
print('\nDanh sách ban đầu: ', lst)
print('Danh sách sau khi sắp xếp: ', sorted_lst)
print('Phần tử lớn nhất: ', max_value)
print('Phần tử bé nhât: ', min_value)