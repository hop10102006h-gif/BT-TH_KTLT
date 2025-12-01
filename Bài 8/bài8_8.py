# Dương Phúc Hợp msv: 245752021610047
"""8. Viết chương trình graphic sử dụng thư viện Tkinter thực hiện:
a) Xây dựng form hiển thị thôn tin cá nhân (họ tên, ngày tháng năm sinh, MSSV,
ngành học)
b) Xây dựng form có nội dung như hình ở dưới, khi bấm vào nút “Click Me”
thông tin nút radio button đang lựa chọn sẽ được chỉ ra (tương ứng với các số 1,
2, 3)"""
import tkinter as tk

def create_personal_info_form():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Thông Tin Cá Nhân")
    root.geometry("400x200")

    # Dữ liệu mẫu
    info = {
        "Họ tên": "Nguyễn Văn A",
        "Ngày sinh": "01/01/2000",
        "MSSV": "12345678",
        "Ngành học": "Khoa học Máy tính"
    }

    # Hiển thị thông tin
    for label_text, value_text in info.items():
        tk.Label(root, text=f"{label_text}: {value_text}", font=('Arial', 12)).pack(anchor='w',padx=10, pady=5)

    # Chạy ứng dụng
    root.mainloop()

create_personal_info_form()
