"""Khung lớp JsonFile; chưa triển khai đọc/ghi JSON."""


class JsonFile:
    def __init__(self, duong_dan, thu_muc_sao_luu="data/backup"):
        self.duong_dan = duong_dan
        self.thu_muc_sao_luu = thu_muc_sao_luu
        self.thong_bao = ""

    def doc(self, mac_dinh=None): pass
    def luu(self, du_lieu): pass
    def cap_nhat(self, du_lieu): pass
    def sao_luu(self): pass
    def danh_sach_sao_luu(self): pass
    def khoi_phuc(self, duong_dan_sao_luu): pass
