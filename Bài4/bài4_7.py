# Dương Phúc Hợp msv: 245752021610047
chuoi = input('nhập chuỗi: ')
moi = ''
for qt in chuoi:
    if not qt.isalpha():
        moi += qt
print('Chuỗi mới: ', moi)