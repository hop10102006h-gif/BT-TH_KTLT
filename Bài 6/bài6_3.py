# Dương Phúc Hợp msv: 245752021610047
class Nguoi:
    def getGender(self):
        pass
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
nguoi_nam = Nam()   # tạo đối tượng Nam
nguoi_nu = Nu()     # tạo đối tượng nữ
print(nguoi_nam.getGender())  # Kết quả: Nam
print(nguoi_nu.getGender())   # Kết quả: Nữ
