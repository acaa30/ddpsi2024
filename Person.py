class Person:
    nama = ""
    gender = ""
    umur = 0

    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    def cetak(self):
        print("Nama \t\t\t: ", self.nama,
              "\nJenis Kelamin \t\t: ", self.gender,
              "\nUmur \t\t\t:", self.umur)
