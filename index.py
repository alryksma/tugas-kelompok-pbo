# Definisi kelas induk Animal
class Animal:
    def __init__(self, nama, sifat, ukuran, kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.kaki = kaki

    def tampil(self):
        print(f"{self.nama} adalah seekor {self.sifat} dengan ukuran {self.ukuran} dan {self.kaki} kaki.")

# Kelas turunan Mamalia dari kelas Animal
class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def tampil(self):
        super().tampil()
        print(f"{self.nama} adalah seekor mamalia {self.jenis_mamalia} dan {'bisa' if self.bisa_jalan else 'tidak bisa'} jalan.")

# Kelas turunan Aves dari kelas Animal
class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def tampil(self):
        super().tampil()
        print(f"{self.nama} adalah seekor burung {self.jenis_aves} dan {'bisa' if self.bisa_terbang else 'tidak bisa'} terbang.")

# Kelas turunan Ayam dari kelas Aves
class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def tampil(self):
        super().tampil()
        print(f"{self.nama} adalah seekor ayam {self.jenis_ayam} dan {'bisa' if self.bisa_diadu else 'tidak bisa'} diadu.")

# Kelas turunan Burung Merpati dari kelas Aves
class BurungMerpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)

# Membuat objek dan memanggil metode
singa = Mamalia("Singa", "buas", "besar", 4, True, "karnivora")
kuda = Mamalia("Kuda", "jinak", "sedang", 4, True, "herbivora")
gajah = Mamalia("Gajah", "lambat", "besar", 4, True, "herbivora")

merpati = BurungMerpati("Merpati", "ramah", "kecil", 2, True, "herbivora")
camar = Aves("Camar", "cerdik", "sedang", 2, True, "karnivora")

ayam = Ayam("Ayam", "berisik", "sedang", 2, True, "karnivora", "kokokan", True)

# Memanggil metode display_info untuk menampilkan informasi
singa.tampil()
kuda.tampil()
gajah.tampil()
merpati.tampil()
camar.tampil()
ayam.tampil()