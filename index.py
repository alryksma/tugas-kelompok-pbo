class Animal:
    def __init__(self, nama, sifat, ukuran, kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.kaki = kaki


class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia


class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves


class Ayam(Aves):
    def __init__(
        self,
        nama,
        sifat,
        ukuran,
        kaki,
        bisa_terbang,
        jenis_aves,
        jenis_ayam,
        bisa_diadu,
    ):
        super().__init__(nama, sifat, ukuran, kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu


# Contoh penggunaan
ayam_pertama = Ayam(
    "Ayam Putih", "Ramah", "Sedang", 2, True, "Burung", "Ayam Kampung", True
)
print(
    f"{ayam_pertama.nama} adalah sejenis {ayam_pertama.jenis_ayam} dan {'bisa' if ayam_pertama.bisa_diadu else 'tidak bisa'} diadu."
)
