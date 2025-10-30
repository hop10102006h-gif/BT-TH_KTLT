# Dương Phúc Hợp msv: 245752021610047
n = input('nhập vào chuỗi: ')
chu_thuong = 0
chu_hoa = 0
for k in n:
    if k.islower():
        chu_thuong +=1
    elif k.isupper():
        chu_hoa += 1
print('Chu hoa: ', chu_hoa)
print('Chu thuong', chu_thuong)
    