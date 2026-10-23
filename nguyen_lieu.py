"""Khung lớp NguyenLieu; chưa triển khai kiểm tra/nghiệp vụ."""


class NguyenLieu:
    def __init__(self, ma_nguyen_lieu, ten_nguyen_lieu, so_luong, don_vi,
                 gia_nhap, han_su_dung, ma_ncc="", muc_toi_thieu=0):
        self.ma_nguyen_lieu = ma_nguyen_lieu
        self.ten_nguyen_lieu = ten_nguyen_lieu
        self.so_luong = so_luong
        self.don_vi = don_vi
        self.gia_nhap = gia_nhap
        self.han_su_dung = han_su_dung
        self.ma_ncc = ma_ncc
        self.muc_toi_thieu = muc_toi_thieu

    def gia_tri(self): pass
    def so_ngay_con_lai(self, ngay=None): pass
    def kiem_tra_so_luong(self, muc=None): pass
    def kiem_tra_han_su_dung(self, so_ngay=0): pass
    def trang_thai(self, so_ngay): pass
    def hien_thi_thong_tin(self): pass
    def to_dict(self): pass
    @classmethod
    def from_dict(cls, data): pass
