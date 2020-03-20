class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

l0 = Mahasiswa("luqman", 107, "pojok", 240000)
l1 = Mahasiswa("faris", 113, "dalangan", 230000)
l2 = Mahasiswa("ridwan", 145, "tawangsari", 250000)
l3 = Mahasiswa("dias", 180, "magetan", 235000)
l4 = Mahasiswa("kevin", 104, "magelang", 240000)
l5 = Mahasiswa("edi", 131, "sleman", 250000)
l6 = Mahasiswa("aji", 123, "batang", 245000)
l7 = Mahasiswa("vara", 125, "kudus", 245000)
l8 = Mahasiswa("veni", 213, "pati", 245000)
l9 = Mahasiswa("dwi", 164, "rembang", 270000)
l10 = Mahasiswa("juna", 129, "balikpapan", 265000)
Daftar = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
    return temp

p = cariUangSakuTerkecil(Daftar)
print(p)
