# Daftar DVD yang tersedia
dvd_tersedia = ["Rafi si katak", "Billal si penjelajah", "Dika si Starboy"]

# Function untuk menampilkan DVD yang tersedia (Non-return type)
def tampilkan_dvd():
    print("Daftar DVD Tersedia:")
    for dvd in dvd_tersedia:
        print(f"- {dvd}")
    print()  # Spasi kosong untuk memperindah tampilan

# Function untuk menambahkan DVD baru ke dalam daftar (Return type tanpa parameter)
def tambah_dvd():
    dvd_baru = input("Masukkan judul DVD yang ingin ditambahkan: ")
    dvd_tersedia.append(dvd_baru)
    return dvd_baru

# Class untuk sistem rental DVD
class RentalDVD:
    def __init__(self, nama_pelanggan):
        self.nama_pelanggan = nama_pelanggan
        self.dvd_dipinjam = []

    # Method non-return type untuk meminjam DVD
    def pinjam_dvd(self, judul_dvd):
        if judul_dvd in dvd_tersedia:
            dvd_tersedia.remove(judul_dvd)
            self.dvd_dipinjam.append(judul_dvd)
            print(f"{self.nama_pelanggan} telah meminjam DVD '{judul_dvd}'.\n")
        else:
            print(f"Maaf, DVD '{judul_dvd}' tidak tersedia.\n")

    # Method return type dengan parameter untuk mengembalikan DVD
    def kembalikan_dvd(self, judul_dvd):
        if judul_dvd in self.dvd_dipinjam:
            self.dvd_dipinjam.remove(judul_dvd)
            dvd_tersedia.append(judul_dvd)
            return f"DVD '{judul_dvd}' telah dikembalikan oleh {self.nama_pelanggan}.\n"
        else:
            return f"{self.nama_pelanggan} tidak meminjam DVD berjudul '{judul_dvd}'.\n"

# Function untuk menjalankan rental DVD
def jalankan_rental():
    pelanggan = input("Masukkan nama pelanggan: ")
    rental = RentalDVD(pelanggan)

    while True:
        print("=== Menu Rental DVD ===")
        print("1. Tampilkan DVD Tersedia")
        print("2. Tambah DVD")
        print("3. Pinjam DVD")
        print("4. Kembalikan DVD")
        print("5. Keluar")

        pilihan = input("\nPilih opsi (1-5): ")

        if pilihan == '1':
            tampilkan_dvd()
        elif pilihan == '2':
            dvd_baru = tambah_dvd()
            print(f"DVD '{dvd_baru}' telah ditambahkan ke rental.\n")
        elif pilihan == '3':
            judul_dvd = input("Masukkan judul DVD yang ingin dipinjam: ")
            rental.pinjam_dvd(judul_dvd)
        elif pilihan == '4':
            judul_dvd = input("Masukkan judul DVD yang ingin dikembalikan: ")
            pesan = rental.kembalikan_dvd(judul_dvd)
            print(pesan)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan rental DVD.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan program rental DVD
jalankan_rental()
