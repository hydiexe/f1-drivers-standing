from tkinter import *
from tkinter import messagebox, Toplevel, StringVar, OptionMenu
from standing import Standing
from models.driver import Driver, ChampionDriver

standing = Standing()

# ==== WINDOW: Tambah Pembalap Biasa ====
def window_tambah_biasa():
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
            messagebox.showwarning("Wajib isi semua data", parent=top)
            return
        standing.tambah_driver(Driver(nama, tim, negara))
        messagebox.showinfo("Sukses", f"{nama} ditambahkan", parent=top)
        top.destroy()

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

# ==== WINDOW: Tambah Pembalap Juara Dunia ====
def window_tambah_juara():
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
            juara = int(entry_juara.get())
            nama = entry_nama.get()
            tim = entry_tim.get()
            negara = entry_negara.get()
            if not nama or not tim or not negara:
                raise ValueError("Data belum lengkap")
            driver = ChampionDriver(nama, tim, negara, jumlah_juara=juara)
            standing.tambah_driver(driver)
            messagebox.showinfo("Sukses", f"{nama} (Juara {juara}x) ditambahkan", parent=top)
            top.destroy()
        except:
            messagebox.showerror("Input salah", "Isi semua field dengan benar", parent=top)

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

# ==== WINDOW: Tampilkan Semua Pembalap ====
def window_tampilkan_semua():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data pembalap.")
        return

    top = Toplevel(root)
    top.title("Daftar Pembalap")

    for i, d in enumerate(daftar, 1):
        info = f"{i}. {d[1]} | {d[2]} | ({d[3]}) | Poin: {d[4]} | Juara: {d[5]}"
        Label(top, text=info).pack(anchor="w")

# ==== WINDOW: Tampilkan Klasemen ====
def window_tampilkan_klasemen():
    daftar = standing.get_klasemen()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data klasemen.")
        return

    top = Toplevel(root)
    top.title("Klasemen Pembalap")

    for i, d in enumerate(daftar, 1):
        info = f"{i}. {d[1]} | {d[2]} | ({d[3]}) | Poin: {d[4]}"
        Label(top, text=info).pack(anchor="w")

# ==== WINDOW: Tambah Poin ke Pembalap ====
def window_tambah_poin():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data pembalap.")
        return

    top = Toplevel(root)
    top.title("Tambah Poin ke Pembalap")

    pilihan = StringVar(top)
    pilihan.set(daftar[0][1])  # default nama pertama
    id_map = {d[1]: d[0] for d in daftar}

    Label(top, text="Pilih Pembalap").pack()
    OptionMenu(top, pilihan, *id_map.keys()).pack()

    Label(top, text="Tambah Berapa Poin?").pack()
    entry_poin = Entry(top)
    entry_poin.pack()

    def simpan():
        try:
            tambahan = int(entry_poin.get())
            standing.tambah_point(id_map[pilihan.get()], tambahan)
            messagebox.showinfo("Sukses", "Poin ditambahkan", parent=top)
            top.destroy()
        except:
            messagebox.showerror("Error", "Input harus angka", parent=top)

    Button(top, text="Simpan", command=simpan).pack(pady=5)
    Button(top, text="Batal", command=top.destroy).pack()

# ==== ROOT WINDOW: Menu Utama ====
root = Tk()
root.title("F1 Driver Standing - GUI")
root.geometry("350x350")

Label(root, text="=== MENU UTAMA ===", font=("Helvetica", 14)).pack(pady=10)

Button(root, text="Tambah Pembalap Biasa", command=window_tambah_biasa).pack(fill="x", padx=20, pady=3)
Button(root, text="Tambah Juara Dunia", command=window_tambah_juara).pack(fill="x", padx=20, pady=3)
Button(root, text="Tampilkan Semua Pembalap", command=window_tampilkan_semua).pack(fill="x", padx=20, pady=3)
Button(root, text="Tampilkan Klasemen", command=window_tampilkan_klasemen).pack(fill="x", padx=20, pady=3)
Button(root, text="Tambah Poin", command=window_tambah_poin).pack(fill="x", padx=20, pady=3)
Button(root, text="Keluar", command=root.destroy).pack(fill="x", padx=20, pady=10)

root.mainloop()
