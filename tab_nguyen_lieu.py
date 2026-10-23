"""Khung tab quản lý nguyên liệu."""
from tkinter import ttk


class TabNguyenLieu(ttk.Frame):
    def __init__(self, master=None, **kwargs): super().__init__(master, **kwargs)
    def nap_du_lieu(self): pass
    def them_nguyen_lieu(self): pass
    def sua_nguyen_lieu(self): pass
    def xoa_nguyen_lieu(self): pass
    def tim_kiem(self): pass
