# Dương Phúc Hợp msv: 245752021610047
# Bài 8. Viết chương trình Python để viết nội dung danh sách vào tệp.
def write_list_to_file(file_name, data_list):
    """
    Viết nội dung của danh sách (list) vào tệp văn bản.
    :param file_name: Tên/đường dẫn của file (string).
    :param data_list: Danh sách chứa các chuỗi muốn ghi vào file (list of strings).
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as f:  # utf-8 đảm bảo ghi đúng định dạng unicode tiếng việt có dấu
            # --- Phương pháp 1: Dùng vòng lặp (Khuyến nghị để kiểm soát định dạng)
            for item in data_list:
                # Ghi từng phần tử vào file và thêm ký tự xuống dòng ('\n') 
                f.write(item + '\n')     
        print(f" Đã ghi thành công {len(data_list)} mục vào tệp '{file_name}'.")
    except Exception as e:
        print(f" Đã xảy ra lỗi khi ghi file: {e}")
#  Ví dụ sử dụng 
file_to_save = 'danh_sach_mua_sam.txt'
shopping_list = [
    "Trứng",
    "Sữa tươi",
    "Bánh mì gối",
    "Rau cải",
    "Thịt bò"
]
write_list_to_file(file_to_save, shopping_list)
print("\n--- Nội dung tệp đã ghi ---")
with open(file_to_save, 'r', encoding='utf-8') as f:
    print(f.read())