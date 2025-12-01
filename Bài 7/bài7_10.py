# Dương Phúc Hợp msv: 245752021610047
# Bài 10.Viết chương trình python để tìm những từ dài nhất trong văn bản
# Đường dẫn tới tệp văn bản
file_path = r"c:\Users\HP\Downloads\pia.txt"
# Mở tệp và đọc nội dung
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()
# Tách văn bản thành các từ
words = text.split()  # split theo khoảng trắng
# Tìm chiều dài từ dài nhất
max_length = max(len(word) for word in words)
# Lấy tất cả từ có chiều dài bằng max_length
longest_words = [word for word in words if len(word) == max_length]
# Hiển thị kết quả
print("Độ dài từ dài nhất:", max_length)
print("Các từ dài nhất:", longest_words)
