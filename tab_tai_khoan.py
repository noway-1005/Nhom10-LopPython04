"""Khung tab quản lý tài khoản."""
from tkinter import ttk


class TabTaiKhoan(ttk.Frame):
    def __init__(self, master=None, **kwargs): super().__init__(master, **kwargs)
    def nap_danh_sach(self): pass
    def tao_tai_khoan(self): pass
    def dat_lai_mat_khau(self): pass
    def xoa_tai_khoan(self): pass
