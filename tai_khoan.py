"""Khung lớp TaiKhoan; chưa triển khai xác thực/mã hóa."""


class TaiKhoan:
    def __init__(self, ten_dang_nhap, mat_khau, vai_tro="user", ho_ten=""):
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.vai_tro = vai_tro
        self.ho_ten = ho_ten

    def to_dict(self): pass
    @classmethod
    def from_dict(cls, data): pass
