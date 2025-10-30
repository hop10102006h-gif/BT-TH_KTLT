# Dương Phúc Hợp msv: 245752021610047
def binary_search(lst, value):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False
# --- Phần chính ---
n = int(input("Nhập số phần tử của danh sách: "))
lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
lst.sort()
value = int(input("Nhập giá trị cần tìm: "))
print(binary_search(lst, value))