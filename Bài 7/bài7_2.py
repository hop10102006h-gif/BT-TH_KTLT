# Dương Phúc Hợp msv: 245752021610047
# Bài 2: Tính số ký tự, số từ và số dòng trong file
f = open(r'c:\Users\HP\Downloads\pia.txt', 'r')
char = 0   # số ký tự
wc = 0     # số từ
lc = 0     # số dòng
for line in f:   # Lặp qua từng dòng của file
    lc += 1    # Tăng biến đếm số dòng lên 1 đơn vị
    char += len(line)  # Cộng số ký tự lại
    wc += len(line.split())   # Cộng số từ lại
f.close()
print("The number of chars is %d" % char)
print("The number of words is %d" % wc)
print("The number of lines is %d" % lc)