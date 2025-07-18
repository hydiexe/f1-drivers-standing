# models.py

"""
models.py

- Driver              : class utama untuk pembalap f1
- ChampionDriver      : subclass yang mewarisi Driver (inheritance), menambahkan atribut juara, dan override method tampil_info()

"""

# class untuk merepresentasikan pembalap Formula One
class Driver:
    def __init__(d, nama, tim, negara, point=0):
        d.nama = nama
        d.tim = tim
        d.negara = negara
        d.point = point

    # menampilkan informasi pembalap
    def tampil_info(d):
        print(f"{d.nama} | {d.tim} | ({d.negara}) | Poin: {d.point}")

    # method tambah poin dengan default argumen
    def tambah_poin(d, tambahan=1):
        d.point += tambahan


# inheritance ChampionDriver mewarisi class Driver
class ChampionDriver(Driver):
    def __init__(d, nama, tim, negara, point=0, jumlah_juara=0):
        super().__init__(nama, tim, negara, point)
        d.jumlah_juara = jumlah_juara

    # OVERRIDING: menimpa method tampil_info dari superclass
    def tampil_info(d):
        print(f"{d.nama} | {d.tim} | ({d.negara}) | Poin: {d.point} | Juara Dunia: {d.jumlah_juara}")
