"""Khung tab thống kê, cảnh báo và báo cáo."""
from tkinter import ttk


class TabThongKe(ttk.Frame):
    def __init__(self, master=None, **kwargs): super().__init__(master, **kwargs)
    def nap_thong_ke(self): pass
    def hien_thi_canh_bao(self): pass
    def xuat_bao_cao(self): pass
