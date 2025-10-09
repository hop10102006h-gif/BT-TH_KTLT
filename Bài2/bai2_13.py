# Dương Phúc Hợp Msv: 245752021610047
import math
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhập c: '))
if a != 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print('pt vô nghiệm')
    elif delta == 0:
        x = -b/(2*a)
        print('pt có nghiệm kép x1=x2=', x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print('pt có 2 nghiệm pb x1={0}, x2={1}'. format(x1, x2))
else:
    print('không phải là pt căn bậc hai')