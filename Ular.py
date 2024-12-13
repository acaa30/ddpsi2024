from Animal import * 

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak
        print("design \t:", self.design,
              "\n racun \t:", self.racun)
        
cobra = Ular("cobra", "daging", "darat", "bertelur", "batik", "berbisa")
cobra.cetak_ular()


boa = Ular("boa", "burung", "daratan", "vivipar", "coklat", "tidak berbisa")
boa.cetak_ular() 