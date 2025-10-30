# Dương Phúc Hợp msv: 245752021610047
# Hàm sắp xếp nổi bọt
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nlist[j] > nlist[j + 1]:
                # Hoán đổi vị trí nếu phần tử sau nhỏ hơn phần tử trước
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
# Chương trình chính
if __name__ == "__main__":
    # Nhập danh sách từ bàn phím, ví dụ: 14,46,43,27,57,41,45,21,70
    nlist = [int(x) for x in input("Nhập các phần tử (cách nhau bởi dấu phẩy): ").split(',')]  
    bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp tăng dần là:")
    print(nlist)
