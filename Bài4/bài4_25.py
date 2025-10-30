# Dương Phúc Hợp msv: 245752021610047
chuoi = input('nhập các số cách nhau bằng dấu phẩy: ')
ds = [int(x) for x in chuoi.split(',')]
so_le = [x for x in ds if x % 2 != 0]
print('Các số lẻ là: ', so_le)