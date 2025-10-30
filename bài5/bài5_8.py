# Dương Phúc Hợp msv: 245752021610047
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
    return False, -1

# --- phần nhập/xuất ---
n = int(input("Nhập số phần tử của danh sách: "))
dlist = []
for i in range(n):
    dlist.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

item = int(input("Nhập phần tử cần tìm: "))
found, index = Sequential_Search(dlist, item)
print((found, index))
