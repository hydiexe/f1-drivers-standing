"""
version     = "v1"
Description = Program ini mencatat data pembalap formula one, mengitung total point, 
            dan mengurutkan klasemen berdasarkan point.
"""

# array
drivers = []

# ini prosedur untuk menambahkan data pembalap
def tambah_driver():
    nama = input("Masukkan nama pembalap: ")
    team = input("Masukkan nama tim: ")
    negara = input("Masukkan nama negara: ")

    try:
        point = int(input("Masukkan total point: ")) # validate, the input must be an int
    except ValueError:
        print("Input tidak valid, masukkan angka untuk point.")
        return # end of the function if input is invalid
    
    # add the driver to the list
    drivers.append({
        "nama": nama,
        "team": team,
        "negara": negara,
        "point": point
    })
    print(f"Pembalap {nama} berhasil ditambahkan.")

# ini prosedur untuk menampilkan data pembalap
def tampilkan_driver():
    if not drivers:
        print("Data pembalap belum ditambahkan.")
        return
    
    print("\n=== Daftar Pembalap ===")
    for i, driver in enumerate(drivers, start=1):
        print(f"{i}. {driver['nama']} | {driver['team']} | ({driver['negara']}) | Point: {driver['point']}")

# ini prosedur untuk mengurutkan pembalap berdasarkan point
def tampilkan_klasemen():
    if not drivers:
        print("Data pembalap belum ditambahkan.")
        return
    
    # sort the drivers by point in descending order
    sorted_drivers = sorted(drivers, key=lambda x: x['point'], reverse=True)
    
    print("\n=== Klasemen Pembalap ===")
    for i, driver in enumerate(sorted_drivers, start=1):
        print(f"{i}. {driver['nama']} | {driver['team']} | ({driver['negara']}) | Point: {driver['point']}")

# fungsi untuk tambah point
# mengembalikan total nilai point baru
def tambah_point(driver, tambahan_point):
    return driver["point"] + tambahan_point

# ini prosedur untuk select and update point pembalap
def update_point():
    if not drivers:
        print("Belum ada data pembalap")
        return
    
    tampilkan_driver()
    
    print("\n=== PILIH PEMBALAP UNTUK DITAMBAH POIN ===")
    for i, d in enumerate(drivers, 1):
        print(f"{i}. {d['nama']} ({d['team']}) - {d['point']} poin")

    try:
        pilihan = int(input("Masukkan nomor pembalap: "))
        tambahan = int(input("Tambah berapa poin?: "))
    except ValueError:
        print("Input tidak valid.")
        return

    if 1 <= pilihan <= len(drivers):
        pembalap = drivers[pilihan - 1]
        poin_baru = tambah_point(pembalap, tambahan)  # pakai fungsi
        pembalap["point"] = poin_baru  # update poin
        print(f"Poin {pembalap['nama']} sekarang: {poin_baru}")
    else:
        print("Nomor tidak valid.")

# main
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Pembalap")
        print("2. Tampilkan Daftar Pembalap")
        print("3. Tampilkan Klasemen Pembalap")
        print("4. Tambah Poin Pembalap")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_driver()
        elif pilihan == '2':
            tampilkan_driver()
        elif pilihan == '3':
            tampilkan_klasemen()
        elif pilihan == '4':
            update_point()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()