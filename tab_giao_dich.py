"""Khung tab giao dịch nhập/xuất kho."""
from tkinter import ttk


class TabGiaoDich(ttk.Frame):
    def __init__(self, master=None, **kwargs): super().__init__(master, **kwargs)
    def tao_phieu_nhap(self): pass
    def tao_phieu_xuat(self): pass
    def nap_lich_su(self): pass
