# Dương Phúc Hợp msv: 245752021610047
chuoi = input('nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ')
ds = chuoi.split(',')
ket_qua = []
for b in ds:
    if int(b, 2) % 5 == 0:
        ket_qua.append(b)
print('Các số nhị phân chi hết cho 5 là: ', ','.join(ket_qua))