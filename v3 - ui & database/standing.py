from database import db
from models.driver import Driver, ChampionDriver

class Standing:
    def __init__(self):
        db.init_db()

    def tambah_driver(self, driver):
        if isinstance(driver, ChampionDriver):
            db.insert_driver(driver.nama, driver.tim, driver.negara, driver.point, driver.jumlah_juara)
        else:
            db.insert_driver(driver.nama, driver.tim, driver.negara, driver.point)
        print(f"Pembalap {driver.nama} berhasil ditambahkan ke database.")

    def tampilkan_semua_driver(self):
        data = db.fetch_all_drivers()
        if not data:
            print("Belum ada pembalap.")
            return

        print("\n=== Daftar Pembalap ===")
        for i, d in enumerate(data, 1):
            nama, tim, negara, point, juara = d
            if juara > 0:
                driver = ChampionDriver(nama, tim, negara, point, juara)
            else:
                driver = Driver(nama, tim, negara, point)
            print(f"{i}. ", end="")
            driver.tampil_info()

    def tambah_poin_ke_driver(self, nama, tambahan):
        db.update_point(nama, tambahan)
        print(f"Poin untuk {nama} ditambahkan sebanyak {tambahan}.")
