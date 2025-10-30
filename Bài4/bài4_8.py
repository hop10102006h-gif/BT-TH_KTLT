# Dương Phúc Hợp msv: 245752021610047
p = input('nhập danh sách: ').split()
maxlen = max(len(w) for w in p)
for w in p:
    if len(w) == maxlen:
        print('Từ dài nhất là: ', w)