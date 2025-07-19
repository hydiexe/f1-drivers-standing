from models.interface import DriverBase

# Kelas utama Driver
class Driver(DriverBase):
    def __init__(self, nama, tim, negara, point=0):
        self.nama = nama
        self.tim = tim
        self.negara = negara
        self.point = point

    def tampil_info(self):
        print(f"{self.nama} | {self.tim} | ({self.negara}) | Poin: {self.point}")

    def tambah_point(self, tambahan=1):
        self.point += tambahan

# Kelas turunan ChampionDriver (OVERRIDING)
class ChampionDriver(Driver):
    def __init__(self, nama, tim, negara, point=0, jumlah_juara=0):
        super().__init__(nama, tim, negara, point)
        self.jumlah_juara = jumlah_juara

    def tampil_info(self):  # OVERRIDING
        print(f"{self.nama} | {self.tim} | ({self.negara}) | Poin: {self.point} | Juara Dunia: {self.jumlah_juara}")
