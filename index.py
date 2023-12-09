class Animal:
    def __init__(self, nama, sifat , ukuran, jumlahKaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jumlahKaki = jumlahKaki

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaJalan, jenisMamalia):
        super().__init__(nama, sifat, ukuran, jumlahKaki)
        self.bisaJalan = bisaJalan
        self.jenisMamalia = jenisMamalia

    def tampilMamalia(self):
        print(f'Nama hewan: {self.nama}, sifat hewan: {self.sifat}, 
              ukuran: {self.ukuran}, jumlah kaki: {self.jumlahKaki}, 
              bisa jalan: {self.bisaJalan}, jenis mamalia: {self.jenisMamalia}')

class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves):
        super().__init__(nama, sifat, ukuran, jumlahKaki)
        self.bisaTerbang = bisaTerbang
        self.jenisAves = jenisAves

    def tampilAves(self):
        print(f'Nama hewan: {self.nama}, sifat hewan: {self.sifat}, 
              ukuran: {self.ukuran}, jumlah kaki: {self.jumlahKaki}, 
              bisa jalan: {self.bisaTerbang}, jenis mamalia: {self.jenisAves}')
        
class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves, jenisAyam, bisaDiadu):
        super().__init__(nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves)
        self.jenisAyam = jenisAyam
        self.bisaDiadu = bisaDiadu

class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves):
        super().__init__(nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves)

