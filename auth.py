"""Khung lớp AuthManager; chưa triển khai đăng nhập/phân quyền."""


class AuthManager:
    def __init__(self, file_handler=None):
        self.tai_khoan = {}
        self.hien_tai = None
        self.thong_bao = ""
        self._file = file_handler

    def doc(self): pass
    def luu(self): pass
    def dang_ky(self, ten, mat_khau, nhap_lai, vai_tro="user"): pass
    def dang_nhap(self, ten, mat_khau): pass
    def dang_xuat(self): pass
    def doi_mat_khau(self, cu, moi, nhap_lai): pass
    def dat_lai_mat_khau(self, ten, moi): pass
    def xoa_tai_khoan(self, ten): pass
    def co_quyen(self, quyen): pass
    def yeu_cau_quyen(self, quyen): pass
    def ten_hien_tai(self): pass
    def danh_sach(self): pass
