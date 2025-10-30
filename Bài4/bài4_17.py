# Dương Phúc Hợp msv: 245752021610047
n = int(input('nhập số nguyên dương: '))
for i in range(1, n):
    tong = sum(j for j in range(1, i) if i % j == 0)
    if tong > i:
        print(tong)