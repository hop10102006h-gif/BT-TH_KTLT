# Dương Phúc Hợp msv: 245752021610047
# Bài 5. Chương trình Python để nối văn bản vào tệp và hiển thị văn bản.
def file_read(fname):
    # 1. Ghi nội dung vào file (chế độ "w")
    # Chế độ "w" (write) sẽ TẠO MỚI file hoặc XÓA SẠCH nội dung cũ nếu file đã tồn tại.
    with open(fname, "w") as myfile:  # mở file ở chế dộ ghi, nếu file chr tồn tại thì tạo file, nếu file đã tồn tại thì xoá toàn bộ nội dung cũ để ghi lại
        myfile.write("Python Exercises\n")  # Ghi chuỗi bao gồm ký tự xuống dòng
        myfile.write("Java Exercises")    # Ghi thêm ký tự dòng hai
    # 2. Đọc nội dung file
    txt = open(fname, 'r') # Thêm chế độ 'r' để làm rõ
    # 3. Hiển thị nội dung
    print(txt.read())
    # Đảm bảo file đọc được đóng
    txt.close()
# Gọi hàm để thực thi chương trình
print(" Nội dung của tệp sau khi được ghi và đọc")
file_read('abc.txt')