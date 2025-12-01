# Dương Phúc Hợp msv: 245752021610047
class RomanToInteger:
    def __init__(self):
        # Bảng giá trị các ký tự La Mã
        self.values = {     # Đây là một từ điển dùng để lưu trữ các giá trị số Lamã
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    def convert(self, roman):
        total = 0
        prev_value = 0
        # Duyệt từ phải qua trái
        for char in reversed(roman):   # hàm reversed để duyệt từ phải sang trái
            value = self.values[char]     # Lấy giá trị nguyên của giá trị hiện tại
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
converter = RomanToInteger()
print(converter.convert("IX"))     # 9
print(converter.convert("LVIII"))  # 58
print(converter.convert("MCMXCIV")) # 1994
