# Dương Phúc Hợp Msv: 245752021610047
import math

x1 = int(input('Nhập x1 từ bàn phím:  '))
x2= int(input('Nhập x2từ bàn phím:  '))

y1= int(input('Nhập y2từ bàn phím:  '))
y2 = int(input('nhập y2 từ bàn phím: '))

d1 = (x2 - x1) * ( x2 - x1)
d2 = (y2-y1)  * (y2-y1)

res = math.sqrt(d1+d2)
print('khoảng cách của d1 và d2 là:  ' , res)