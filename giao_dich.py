"""Khung giao dịch kho: lớp trừu tượng và hai lớp con."""
from abc import ABC, abstractmethod


class GiaoDichKho(ABC):
    def __init__(self, ma_giao_dich, ngay_giao_dich, nguoi_thuc_hien):
        self.ma_giao_dich = ma_giao_dich
        self.ngay_giao_dich = ngay_giao_dich
        self.nguoi_thuc_hien = nguoi_thuc_hien

    @abstractmethod
    def thuc_hien_giao_dich(self, kho): pass
    @abstractmethod
    def danh_sach_dong(self): pass
    @abstractmethod
    def ghi_chu(self): pass
    @abstractmethod
    def to_dict(self): pass


class PhieuNhap(GiaoDichKho):
    def __init__(self, ma_giao_dich, ngay_giao_dich, nguoi_thuc_hien,
                 danh_sach_nhap=None, nha_cung_cap=""):
        super().__init__(ma_giao_dich, ngay_giao_dich, nguoi_thuc_hien)
        self.danh_sach_nhap = danh_sach_nhap or []
        self.nha_cung_cap = nha_cung_cap

    def thuc_hien_giao_dich(self, kho): pass
    def danh_sach_dong(self): pass
    def ghi_chu(self): pass
    def to_dict(self): pass


class PhieuXuat(GiaoDichKho):
    def __init__(self, ma_giao_dich, ngay_giao_dich, nguoi_thuc_hien,
                 danh_sach_xuat=None, ly_do=""):
        super().__init__(ma_giao_dich, ngay_giao_dich, nguoi_thuc_hien)
        self.danh_sach_xuat = danh_sach_xuat or []
        self.ly_do = ly_do

    def thuc_hien_giao_dich(self, kho): pass
    def danh_sach_dong(self): pass
    def ghi_chu(self): pass
    def to_dict(self): pass
