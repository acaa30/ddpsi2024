class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("Nama \t\t: ", self.nama,
              "\nmakanan \t: ",self.hidup,
              "\nberkembang_biak : ", self.berkembang_biak)
        

object = Animal("buaya", "daging", "amphibi", "bertelur")
object.cetak()

object = Animal("sapi", "rumput", "darat", "melahirkan",)
object.cetak()