from tkinter import *
from tkinter import messagebox, Toplevel, StringVar, OptionMenu
from standing import Standing
from models.driver import Driver, ChampionDriver

# Inisialisasi objek Standing yang otomatis membuat database
standing = Standing()

# Prosedur untuk menambah pembalap biasa
def tambah_biasa():
    nama = entry_nama.get()
    tim = entry_tim.get()
    negara = entry_negara.get()

    if not nama or not tim or not negara:
        messagebox.showwarning("Peringatan", "Semua kolom wajib diisi.")
        return

    driver = Driver(nama, tim, negara)
    standing.tambah_driver(driver)
    messagebox.showinfo("Sukses", f"Pembalap {nama} berhasil ditambahkan.")

# Prosedur untuk menambah pembalap juara dunia (OOP: inheritance)
def tambah_juara():
    nama = entry_nama.get()
    tim = entry_tim.get()
    negara = entry_negara.get()

    try:
        juara = int(entry_juara.get())
    except ValueError:
        messagebox.showerror("Error", "Jumlah juara harus berupa angka.")
        return

    if not nama or not tim or not negara:
        messagebox.showwarning("Peringatan", "Semua kolom wajib diisi.")
        return

    driver = ChampionDriver(nama, tim, negara, jumlah_juara=juara)
    standing.tambah_driver(driver)
    messagebox.showinfo("Sukses", f"Juara dunia {nama} berhasil ditambahkan.")

# Menampilkan semua data pembalap (OOP + database)
def tampilkan_semua():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data pembalap.")
        return

    top = Toplevel(root)
    top.title("Daftar Pembalap")
    for i, d in enumerate(daftar, 1):
        info = f"{i}. {d[1]} | {d[2]} | ({d[3]}) | Poin: {d[4]} | Juara: {d[5]}"
        Label(top, text=info).pack(anchor="w")

# Menampilkan klasemen urut berdasarkan point
def tampilkan_klasemen():
    daftar = standing.get_klasemen()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data pembalap.")
        return

    top = Toplevel(root)
    top.title("Klasemen Pembalap")
    for i, d in enumerate(daftar, 1):
        info = f"{i}. {d[1]} | {d[2]} | ({d[3]}) | Poin: {d[4]}"
        Label(top, text=info).pack(anchor="w")

# Tambah poin ke pembalap tertentu
def tambah_point_gui():
    daftar = standing.get_all_drivers()
    if not daftar:
        messagebox.showinfo("Info", "Belum ada data pembalap.")
        return

    top = Toplevel(root)
    top.title("Tambah Poin Pembalap")

    pilihan = StringVar(top)
    pilihan.set(daftar[0][1])  # default pilih nama pertama

    nama_to_id = {d[1]: d[0] for d in daftar}

    Label(top, text="Pilih Pembalap").pack()
    drop = OptionMenu(top, pilihan, *nama_to_id.keys())
    drop.pack()

    Label(top, text="Jumlah Poin Tambahan").pack()
    entry_poin = Entry(top)
    entry_poin.pack()

    def simpan():
        try:
            tambahan = int(entry_poin.get())
            id_driver = nama_to_id[pilihan.get()]
            standing.tambah_point(id_driver, tambahan)
            messagebox.showinfo("Sukses", "Poin berhasil ditambahkan.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

    Button(top, text="Simpan", command=simpan).pack(pady=5)

# === GUI START ===
root = Tk()
root.title("F1 Driver Standings GUI")
root.geometry("400x400")

Label(root, text="Nama").pack()
entry_nama = Entry(root)
entry_nama.pack()

Label(root, text="Tim").pack()
entry_tim = Entry(root)
entry_tim.pack()

Label(root, text="Negara").pack()
entry_negara = Entry(root)
entry_negara.pack()

Label(root, text="Jumlah Juara Dunia (Opsional)").pack()
entry_juara = Entry(root)
entry_juara.pack()

Button(root, text="Tambah Pembalap Biasa", command=tambah_biasa).pack(pady=4)
Button(root, text="Tambah Juara Dunia", command=tambah_juara).pack(pady=4)
Button(root, text="Tampilkan Semua Pembalap", command=tampilkan_semua).pack(pady=4)
Button(root, text="Tampilkan Klasemen", command=tampilkan_klasemen).pack(pady=4)
Button(root, text="Tambah Poin ke Pembalap", command=tambah_point_gui).pack(pady=4)
Button(root, text="Keluar", command=root.quit).pack(pady=10)

root.mainloop()