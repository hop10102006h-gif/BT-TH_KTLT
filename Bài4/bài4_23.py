# Dương Phúc Hợp msv: 245752021610047
chuoi = input('nhập số chuỗi: ')
chu_cai = 0
chu_so = 0
for cn in chuoi:
    if cn.isalpha():
        chu_cai +=1
    elif cn.isdigit():
        chu_so +=1
print('Số chữ cái là: ', chu_cai)
print('Số chữ số là: ', chu_so)