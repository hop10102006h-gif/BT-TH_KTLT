# Dương Phúc Hợp msv: 245752021610047
# Bài 1: Đọc file và in đảo ngược kết quả
input_file = open(r'c:\Users\HP\Downloads\pia.txt', 'r')
for line in input_file:
    line = line.strip()  # loại bỏ ký tự xuống dòng
    l = len(line) # trả về ký tự của chuỗi line. ví dụ line = 'abc', len(line) = 3
    s = ''  # sử dụng chuỗi rỗng để chứa kết quả (chuỗi đã đảo)
    while l > 0:   # lặp từ l xuống 1
        s = s + line[l - 1] # tạo một chuỗi mới bằng cách ghép s và line[l-1]=> tạo thành chuỗi đảo ngược
        l = l - 1  # Giảm biến đếm tiến về 0 khi l về 0 thì vòng lặp kết thúc
    print(s)
input_file.close()