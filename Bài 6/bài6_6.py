# Dương Phúc Hợp msv: 245752021610047
class XuLyChuoi:
    def __init__(self):  # Khởi tạo biến thành viên là string 
        self.string = ""   # Ban đầu gán giá trị rỗng cho nó để lưu trữ dữ liệu của chuỗi
    def get_String(self):
        self.string = input("Nhập chuỗi: ")     # Lấy chuỗi từ người dùng
    def print_String(self):  # In ra chuỗi người dùng đã nhập
        print(self.string.upper())  # Chuyển chuỗi từ chữ thường thành chữ hoa
obj = XuLyChuoi()  # tạo đối tượng có tên là obj từ lớp XuLyChuoi
obj.get_String()
obj.print_String()
