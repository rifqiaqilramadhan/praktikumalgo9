def tulis_biodata(nama, umur, alamat, email, dosen_wali):
    with open("Biodata.txt", "w") as file:
        file.write(f"Nama          : {nama}\n")
        file.write(f"Umur          : {umur}\n")
        file.write(f"Alamat        : {alamat}\n")
        file.write(f"Email         : {email}\n")
        file.write(f"Dosen Wali    : {dosen_wali}\n")
    print("Biodata berhasil ditulis ke dalam file.")

def baca_biodata():
    try:
        with open("Biodata.txt", "r") as file:
            isi_biodata = file.read()
            print("Isi Biodata:\n", isi_biodata)
    except FileNotFoundError:
        print("File Biodata.txt tidak ditemukan.")

def main():
    print("Masukkan Biodata:")
    nama = input("Nama          : ")
    umur = input("Umur          : ")
    alamat = input("Alamat        : ")
    email = input("Email         : ")
    dosen_wali = input("Dosen Wali    : ")

    tulis_biodata(nama, umur, alamat, email, dosen_wali)
    baca_biodata()

if __name__ == "__main__":
    main()
