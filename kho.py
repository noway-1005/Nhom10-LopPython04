"""Khung lớp Kho; chưa triển khai CRUD/giao dịch/thống kê."""


class Kho:
    def __init__(self, tu_dong_luu=True, file_handler=None):
        self.danh_sach_nguyen_lieu = []
        self.danh_sach_nha_cung_cap = []
        self.danh_sach_mon_an = []
        self.lich_su_giao_dich = []
        self.tu_dong_luu = tu_dong_luu
        self.canh_bao_doc = []
        self._file = file_handler

    def tim_nguyen_lieu_theo_ma(self, ma): pass
    def lay_nguyen_lieu(self, ma): pass
    def tim_ncc_theo_ma(self, ma): pass
    def lay_nha_cung_cap(self, ma): pass
    def lay_mon_an(self, ma): pass
    def sinh_ma(self, tien_to): pass
    def them_nguyen_lieu(self, nguyen_lieu): pass
    def cap_nhat_nguyen_lieu(self, nguyen_lieu): pass
    def xoa_nguyen_lieu(self, ma): pass
    def tim_kiem_nguyen_lieu(self, tu_khoa="", **bo_loc): pass
    def them_nha_cung_cap(self, nha_cung_cap): pass
    def cap_nhat_nha_cung_cap(self, nha_cung_cap): pass
    def xoa_nha_cung_cap(self, ma): pass
    def tim_kiem_nha_cung_cap(self, tu_khoa=""): pass
    def them_mon_an(self, mon_an): pass
    def cap_nhat_mon_an(self, mon_an): pass
    def xoa_mon_an(self, ma): pass
    def tim_kiem_mon_an(self, tu_khoa=""): pass
    def ghi_nhan_giao_dich(self, giao_dich): pass
    def loc_giao_dich(self, loai=None, tu_ngay=None, den_ngay=None): pass
    def canh_bao_sap_het_hang(self, muc_toi_thieu=None): pass
    def canh_bao_sap_het_han(self, so_ngay=0): pass
    def tinh_tong_gia_tri_kho(self): pass
    def thong_ke_gia_tri_theo_nguyen_lieu(self): pass
    def thong_ke_tieu_thu(self): pass
    def thong_ke_nhap_xuat(self): pass
    def luu_du_lieu_json(self): pass
    def doc_du_lieu_json(self): pass
    def sao_luu(self): pass
    def danh_sach_sao_luu(self): pass
    def khoi_phuc_tu_sao_luu(self, duong_dan): pass
    def trong(self): pass
    def xoa_toan_bo(self): pass
