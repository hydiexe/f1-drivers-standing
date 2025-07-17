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

