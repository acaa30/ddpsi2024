from Animal import * 

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, kantong_udara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
        self.kantong_udara = kantong_udara
        self.makanan = makanan

    def cetak_Burung(self):
        super().cetak
        print("nama \t\t:", self.nama,    
              "\nmakanan\t\t:", self.makanan, 
              "\nhidup \t:", self.hidup,
              "\nberkembang_biak \t:", self.berkembang_biak,
              "\nwarna \t\t:", self.warna_bulu,
              "\nsirip \t\t:", self.kantong_udara,
              "\n------------------------") 
        
    def terbang(self):
        print("{self.nama}, berkembang biak di {self.berkembang_biak}, dan memakan {self.memakan}")

    def berkicau(self):
        print("{self.nama}, berkicau di {self.hidup}, dan memakan {self.memakan}")
        
gagak = Burung("Gagak", "Daging", "Terbang", "Bertelur", "Hitam Mengkilap", "Kantong Udara")
gagak.cetak_Burung()


dara = Burung("Dara", "Jagung", "Berkucau", "Bertelur", "Hitam", "Kantong Udara")
dara.cetak_Burung()

