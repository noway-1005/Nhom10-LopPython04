"""Khung tab quản lý nhà cung cấp."""
from tkinter import ttk


class TabNhaCungCap(ttk.Frame):
    def __init__(self, master=None, **kwargs): super().__init__(master, **kwargs)
    def nap_du_lieu(self): pass
    def them_nha_cung_cap(self): pass
    def sua_nha_cung_cap(self): pass
    def xoa_nha_cung_cap(self): pass
    def tim_kiem(self): pass
