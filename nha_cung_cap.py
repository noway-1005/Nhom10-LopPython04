"""Khung lớp NhaCungCap; chưa triển khai kiểm tra dữ liệu."""


class NhaCungCap:
    def __init__(self, ma_ncc, ten_ncc, so_dien_thoai="", email="", dia_chi=""):
        self.ma_ncc = ma_ncc
        self.ten_ncc = ten_ncc
        self.so_dien_thoai = so_dien_thoai
        self.email = email
        self.dia_chi = dia_chi

    def to_dict(self): pass
    @classmethod
    def from_dict(cls, data): pass
    def hien_thi_thong_tin(self): pass
