# Dương Phúc Hợp msv: 245752021610047
# Bài 9. Viết chương trình Python để sao chép nội dung của tệp này sang tệp khác.
import shutil
def copy_file_shutil(source_file, destination_file):
    """
    Sao chép nội dung từ tệp nguồn sang tệp đích bằng module shutil.
    :param source_file: Tên/đường dẫn của file nguồn.
    :param destination_file: Tên/đường dẫn của file đích.
    """
    try:
        # shutil.copyfile chỉ sao chép nội dung file.
        shutil.copyfile(source_file, destination_file)
        print(f" Sao chép thành công nội dung từ '{source_file}' sang '{destination_file}'.")
    except FileNotFoundError:
        print(f" Lỗi: Không tìm thấy file nguồn '{source_file}'.")
    except Exception as e:
        print(f" Đã xảy ra lỗi khi sao chép: {e}")
source = r'c:\Users\HP\Downloads\pia.txt'
destination = r'c:\Users\HP\Downloads\pia.txt'
copy_file_shutil(source, destination)