from models import Driver, ChampionDriver
from standing import Standing

def menu():
    standing = Standing()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah Pembalap Biasa")
        print("2. Tambah Pembalap Juara Dunia")
        print("3. Tampilkan Daftar Pembalap")
        print("4. Tampilkan Klasemen")
        print("5. Tambah Poin ke Pembalap")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            nama = input("Nama: ")
            tim = input("Tim: ")
            negara = input("Negara: ")
            try:
                point = int(input("Poin awal: "))
                driver = Driver(nama, tim, negara, point)
                standing.tambah_driver(driver)
            except ValueError:
                print("Poin harus berupa angka.")

        elif pilihan == '2':
            nama = input("Nama: ")
            tim = input("Tim: ")
            negara = input("Negara: ")
            try:
                point = int(input("Poin awal: "))
                juara = int(input("Jumlah Juara Dunia: "))
                driver = ChampionDriver(nama, tim, negara, point, juara)
                standing.tambah_driver(driver)
            except ValueError:
                print("Input harus berupa angka.")

        elif pilihan == '3':
            standing.tampilkan_semua_driver()

        elif pilihan == '4':
            standing.tampilkan_klasemen()

        elif pilihan == '5':
            standing.tampilkan_semua_driver()
            try:
                index = int(input("Nomor pembalap yang dipilih: ")) - 1
                tambahan = int(input("Tambah berapa poin?: "))
                standing.tambah_poin_ke_driver(index, tambahan)
            except ValueError:
                print("Input tidak valid.")

        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()