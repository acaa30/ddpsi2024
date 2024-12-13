from Animal import * 

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, sirip):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.sirip = sirip
        self.makanan = makanan

    def cetak_Ikan(self):
        super().cetak
        print("nama \t\t:", self.nama,    
              "\nmakanan\t\t:", self.makanan, 
              "\nhidup \t:", self.hidup,
              "\nberkembang_biak \t:", self.berkembang_biak,
              "\nwarna \t\t:", self.warna,
              "\nsirip \t\t:", self.sirip,
              "\n------------------------")
        
nila = Ikan("Nila", "Plankton", "Air", "Bertelur", "Kehitaman", "Sirip Punggung")
nila.cetak_Ikan()

gabus = Ikan("Gabus", "Cacing", "Air", "Bertelur", "Hitam", "Sirip Punggung")
gabus.cetak_Ikan()