"""Khung các widget tùy biến Tkinter."""
import tkinter as tk
from tkinter import ttk


class DateEntry(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def get(self): pass
    def set(self, ngay): pass
    def dat_trang_thai(self, trang_thai): pass


class DataTree(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def nap(self, du_lieu): pass
    def chon(self): pass
    def sap_xep(self, cot, tang=True): pass


class BarChart(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
    def ve(self, du_lieu): pass
