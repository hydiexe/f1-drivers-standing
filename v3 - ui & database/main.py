from models.driver import Driver, ChampionDriver
from standing import Standing

def menu():
    standing = Standing()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah Pembalap Biasa")
        print("2. Tambah Pembalap Juara Dunia")
        print("3. Lihat Daftar Pembalap")
        print("4. Tambah Poin Pembalap")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Nama: ")
            tim = input("Tim: ")
            negara = input("Negara: ")
            try:
                poin = int(input("Poin awal: "))
                driver = Driver(nama, tim, negara, poin)
                standing.tambah_driver(driver)
            except ValueError:
                print("Poin harus angka.")

        elif pilihan == '2':
            nama = input("Nama: ")
            tim = input("Tim: ")
            negara = input("Negara: ")
            try:
                poin = int(input("Poin awal: "))
                juara = int(input("Jumlah juara dunia: "))
                driver = ChampionDriver(nama, tim, negara, poin, juara)
                standing.tambah_driver(driver)
            except ValueError:
                print("Input harus angka.")

        elif pilihan == '3':
            standing.tampilkan_semua_driver()

        elif pilihan == '4':
            nama = input("Nama pembalap: ")
            try:
                tambah = int(input("Tambah poin: "))
                standing.tambah_poin_ke_driver(nama, tambah)
            except ValueError:
                print("Harus angka.")

        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
