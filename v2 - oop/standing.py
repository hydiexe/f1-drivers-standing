# standing.py

"""
standing.py

- Standing: class untuk mengelola daftar pembalap f1 (objek Driver dan ChampionDriver dari models.py)

"""

from models import Driver, ChampionDriver
class Standing:
    def __init__(self):
        self.daftar_driver = []

    def tambah_driver(self, driver):
        self.daftar_driver.append(driver)
        print(f"Pembalap {driver.nama} berhasil ditambahkan.")

    def tampilkan_semua_driver(self):
        if not self.daftar_driver:
            print("Belum ada pembalap.")
            return

        print("\n=== Daftar Pembalap ===")
        for i, driver in enumerate(self.daftar_driver, 1):
            print(f"{i}. ", end="")
            driver.tampil_info()

    def tampilkan_klasemen(self):
        if not self.daftar_driver:
            print("Belum ada pembalap.")
            return

        print("\n=== Klasemen Pembalap ===")
        for i, driver in enumerate(sorted(self.daftar_driver, key=lambda d: d.point, reverse=True), 1):
            print(f"{i}. ", end="")
            driver.tampil_info()

    def tambah_poin_ke_driver(self, index, tambahan=1):
        if 0 <= index < len(self.daftar_driver):
            self.daftar_driver[index].tambah_poin(tambahan)
            print(f"{self.daftar_driver[index].nama} mendapat tambahan {tambahan} poin.")
        else:
            print("Nomor pembalap tidak valid.")