"""Khung lớp MonAn; chưa triển khai định mức/chế biến."""


class MonAn:
    def __init__(self, ma_mon, ten_mon, dinh_muc_nguyen_lieu=None):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.dinh_muc_nguyen_lieu = dinh_muc_nguyen_lieu or {}

    def cap_nhat_mon_an(self, ten_mon, dinh_muc): pass
    def tinh_nguyen_lieu_can(self, so_luong_mon): pass
    def kiem_tra_kha_nang_che_bien(self, kho, so_luong_mon): pass
    def che_bien(self, kho, so_luong_mon, nguoi_thuc_hien): pass
    def to_dict(self): pass
    @classmethod
    def from_dict(cls, data): pass
