class Mahasiswa(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

l0 = Mahasiswa("luqman", 107, "pojok", 289000)
l1 = Mahasiswa("faris", 113, "serengan", 230000)
l2 = Mahasiswa("ridwan", 145, "tawangsari", 250000)
l3 = Mahasiswa("dias", 180, "magetan", 265000)
l4 = Mahasiswa("kevin", 104, "magelang", 2000000)
l5 = Mahasiswa("edi", 131, "sleman", 250000)
l6 = Mahasiswa("aji", 123, "batang", 245000)
l7 = Mahasiswa("vara", 125, "kudus", 290000)
l8 = Mahasiswa("veni", 213, "pati", 267000)
l9 = Mahasiswa("dwi", 164, "rembang", 2420000)
l10 = Mahasiswa("juna", 129, "balikpapan", 265000)

Daftar = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
def cariTerkecil (self):
    terkecil = self[0].uangSaku
    c = []
    for i in self:
        if i.uangSaku < terkecil :
            c.append ((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
    return c
print(cariTerkecil(Daftar))   
