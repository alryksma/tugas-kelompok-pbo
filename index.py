class Animal:
    def __init__(self, nama, sifat , ukuran, jumlahKaki):
        self.nama = nama
        self.sifat = sifat
        self._ukuran = ukuran
        self._jumlahKaki = jumlahKaki

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaJalan, jenisMamalia):
        super().__init__(nama, sifat, ukuran, jumlahKaki)
        self.bisaJalan = bisaJalan
        self.__jenisMamalia = jenisMamalia


class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves):
        super().__init__(nama, sifat, ukuran, jumlahKaki)
        self.bisaTerbang = bisaTerbang
        self.__jenisAves = jenisAves

        
class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves, jenisAyam, bisaDiadu):
        super().__init__(nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves)
        self.jenisAyam = jenisAyam
        self.__bisaDiadu = bisaDiadu

class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves):
        super().__init__(nama, sifat, ukuran, jumlahKaki, bisaTerbang, jenisAves)

