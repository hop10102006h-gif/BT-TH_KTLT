# Dương Phúc Hợp msv: 245752021610047
# Bài 4. Chương trình Python để đọc n dòng đầu tiên của tệp
from itertools import islice
def file_read_from_head(fname, nlines):
    """"
    Đọc n dòng đầu tiên của file 'fname'.
    :param fname: Tên/đường dẫn của file (string).
    :param nlines: Số dòng muốn đọc (integer).
    """
    # Sử dụng 'with open(...)' để đảm bảo file được đóng tự động
    with open(fname, 'r') as f:
        # islice(f, nlines) sẽ lấy ra nlines phần tử đầu tiên 
        # (tức là nlines dòng đầu tiên) từ file object 'f'
        for line in islice(f, nlines):
            print(line, end='') # Sử dụng end='' để tránh in hai lần ký tự xuống dòng
                                # (vì 'line' đã bao gồm \n từ file)
print(r" Kết quả đọc 2 dòng đầu tiên từ 'c:\Users\HP\Downloads\pia.txt' ")
file_read_from_head(r'c:\Users\HP\Downloads\pia.txt', 2)