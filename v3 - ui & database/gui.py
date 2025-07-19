from tkinter import *
from tkinter import messagebox, Toplevel, StringVar, OptionMenu
from standing import Standing
from models.driver import Driver, ChampionDriver

standing = Standing()

def menu_tambah_biasa():
    top = Toplevel(root)
    top.title("Tambah Pembalap Biasa")

    Label(top, text="Nama").pack()
    entry_nama = Entry(top)
    entry_nama.pack()

    Label(top, text="Tim").pack()
    entry_tim = Entry(top)
    entry_tim.pack()

    Label(top, text="Negara").pack()
    entry_negara = Entry(top)
    entry_negara.pack()

    def simpan():
        nama = entry_nama.get()
        tim = entry_tim.get()
        negara = entry_negara.get()
        if not nama or not tim or not negara:
            messagebox.showwarning("Lengkapi semua data", parent=top)
            return
        standing.tambah_driver(Driver(nama, tim, negara))
        messagebox.showinfo("Sukses", f"{nama} ditambahkan", parent=top)
        top.destroy()

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

def menu_tambah_juara():
    top = Toplevel(root)
    top.title("Tambah Juara Dunia")

    Label(top, text="Nama").pack()
    entry_nama = Entry(top)
    entry_nama.pack()

    Label(top, text="Tim").pack()
    entry_tim = Entry(top)
    entry_tim.pack()

    Label(top, text="Negara").pack()
    entry_negara = Entry(top)
    entry_negara.pack()

    Label(top, text="Jumlah Juara Dunia").pack()
    entry_juara = Entry(top)
    entry_juara.pack()

    def simpan():
        try:
            nama = entry_nama.get()
            tim = entry_tim.get()
            negara = entry_negara.get()
            juara = int(entry_juara.get())
            if not nama or not tim or not negara:
                raise ValueError
            driver = ChampionDriver(nama, tim, negara, jumlah_juara=juara)
            standing.tambah_driver(driver)
            messagebox.showinfo("Sukses", f"{nama} (Juara {juara}x) ditambahkan", parent=top)
            top.destroy()
        except:
            messagebox.showerror("Gagal", "Isi data dengan benar", parent=top)

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

def menu_tampilkan_semua():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada pembalap.")
        return

    top = Toplevel(root)
    top.title("Daftar Pembalap")

    for i, d in enumerate(daftar, 1):
        text = f"{i}. {d.nama} | {d.tim} | ({d.negara}) | Poin: {d.point}"
        if isinstance(d, ChampionDriver):
            text += f" | Juara: {d.jumlah_juara}"
        Label(top, text=text).pack(anchor="w")

def menu_tampilkan_klasemen():
    daftar = standing.get_klasemen()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data.")
        return

    top = Toplevel(root)
    top.title("Klasemen Pembalap")

    for i, d in enumerate(daftar, 1):
        text = f"{i}. {d.nama} | {d.tim} | ({d.negara}) | Poin: {d.point}"
        Label(top, text=text).pack(anchor="w")

def menu_tambah_poin():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data.")
        return

    top = Toplevel(root)
    top.title("Tambah Poin")

    pilihan = StringVar(top)
    pilihan.set(daftar[0].nama)
    nama_to_driver = {d.nama: d for d in daftar}

    Label(top, text="Pilih Pembalap").pack()
    OptionMenu(top, pilihan, *nama_to_driver.keys()).pack()

    Label(top, text="Tambahan Poin").pack()
    entry_poin = Entry(top)
    entry_poin.pack()

    def simpan():
        try:
            tambahan = int(entry_poin.get())
            driver_obj = nama_to_driver[pilihan.get()]
            standing.tambah_poin_ke_driver(driver_obj.nama, tambahan)
            messagebox.showinfo("Sukses", f"{driver_obj.nama} mendapat {tambahan} poin", parent=top)
            top.destroy()
        except:
            messagebox.showerror("Error", "Masukkan angka yang valid", parent=top)

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

root = Tk()
root.title("F1 Driver Standings")
root.geometry("350x350")

Label(root, text="MENU UTAMA", font=("Helvetica", 14, "bold")).pack(pady=10)

Button(root, text="Menu Tambah Pembalap", command=menu_tambah_biasa).pack(fill="x", padx=30, pady=3)
Button(root, text="Menu Tambah Juara Dunia", command=menu_tambah_juara).pack(fill="x", padx=30, pady=3)
Button(root, text="Menu Tampilkan Pembalap", command=menu_tampilkan_semua).pack(fill="x", padx=30, pady=3)
Button(root, text="Menu Tampilkan Klasemen", command=menu_tampilkan_klasemen).pack(fill="x", padx=30, pady=3)
Button(root, text="Menu Tambah Poin", command=menu_tambah_poin).pack(fill="x", padx=30, pady=3)

Button(root, text="Keluar", command=root.quit).pack(fill="x", padx=30, pady=10)

root.mainloop()