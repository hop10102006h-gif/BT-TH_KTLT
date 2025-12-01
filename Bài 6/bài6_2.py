# Dương Phúc Hợp msv: 245752021610047
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong 
    def dientich(self):
        return self.chieu_dai * self.chieu_rong
hcn = Hinhchunhat(4, 6)
print("Diện tích hình chữ nhật là:", hcn.dientich())
