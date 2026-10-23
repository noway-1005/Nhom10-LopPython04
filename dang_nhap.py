"""Khung giao diện đăng nhập và hộp thoại tài khoản."""
import tkinter as tk
from tkinter import ttk


class FrameDangNhap(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def xu_ly_dang_nhap(self): pass


class HopThoaiDangKy(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def xu_ly_dang_ky(self): pass


class HopThoaiDoiMatKhau(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def xu_ly_doi_mat_khau(self): pass
