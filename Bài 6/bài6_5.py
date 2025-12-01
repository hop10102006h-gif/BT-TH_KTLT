# Dương Phúc Hợp msv: 245752021610047
class ReverseWords:   # Khởi tạo lớp có chức năng đảo ngược từ
    def reverse(self, sentence):
        words = sentence.split()   # Tách chuỗi thành danh sách từ
        words.reverse()            # Đảo ngược danh sách
        return " ".join(words)     # Ghép lại thành chuỗi mới
rw = ReverseWords()
input_data = "hello .py"
output_data = rw.reverse(input_data)
print(output_data)  # Kết quả: ".py hello"
