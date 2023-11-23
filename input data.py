def buat_file(nama_file, nama, nim, tahun_angkatan):
    try:
        with open(nama_file, "w") as file:
            file.write(f"Nama: {nama}\n")
            file.write(f"NIM: {nim}\n")
            file.write(f"Tahun Angkatan: {tahun_angkatan}\n")
        print(f"File {nama_file} berhasil dibuat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def baca_file(nama_file):
    try:
        with open(nama_file, "r") as file:
            isi_file = file.read()
            print(f"Isi {nama_file}:\n{isi_file}")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def tambah_teks(nama_file, teks):
    try:
        with open(nama_file, "a") as file:
            file.write(f"{teks}\n")
        print(f"Teks berhasil ditambahkan ke dalam {nama_file}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

while True:
    print("\nMenu:")
    print("1. Buat File")
    print("2. Baca File")
    print("3. Tambah Teks ke File")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        nama_file = input("Masukkan nama file (dengan ekstensi .txt): ")
        nama = input("Masukkan nama anda: ")
        nim = input("Masukkan NIM anda: ")
        tahun_angkatan = input("Masukkan tahun anda: ")
        buat_file(nama_file, nama, nim, tahun_angkatan)
    elif pilihan == "2":
        nama_file = input("Masukkan nama file (dengan ekstensi .txt): ")
        baca_file(nama_file)
    elif pilihan == "3":
        nama_file = input("Masukkan nama file (dengan ekstensi .txt): ")
        teks = input("Masukkan teks yang ingin ditambahkan: ")
        tambah_teks(nama_file, teks)
    elif pilihan == "4":
        print("Program ditutup.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, atau 4.")
