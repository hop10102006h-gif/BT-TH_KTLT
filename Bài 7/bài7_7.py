# Dương Phúc Hợp msv: 245752021610047
# Bài 7. Viết chương trình Python để đếm số dòng trong tệp văn bản
def count_lines(fname):
    try:   # để xử lý ngoại lệ trường hợp file không tồn tại
        # Mở file ở chế độ đọc ('r')
        with open(fname, 'r') as f:
            # list(f) tạo ra một danh sách (list) chứa tất cả các dòng của file.
            # len(...) sẽ trả về số lượng phần tử (tức là số dòng) trong danh sách đó.
            line_count = len(list(f))
            return line_count     
    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy file '{fname}'"
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"
file_name = r'c:\Users\HP\Downloads\pia.txt'
total_lines = count_lines(file_name)
print(f"File: {file_name}")
print(f"Tổng số dòng: {total_lines}")