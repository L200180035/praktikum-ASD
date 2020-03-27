class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    def katakanPy(self):
        print('Python is cool.')
        
listan = [MhsTIF ('Luqman',35,'Sukoharjo', 129000),
MhsTIF('Doni',36,'Surabaya', 890000),
MhsTIF('Dono',29,'Klaten', 123000),
MhsTIF('Chandra',37,'Surakarta', 230000),
MhsTIF('Sony',30,'Sleman', 22000),
MhsTIF('Yoga',31,'Magelang', 980000),
MhsTIF('Agus',34,'Semarang', 267000),
MhsTIF('Tita',28,'Surakarta', 212000),
MhsTIF('Subagyo',25,'Wonogiri', 975000),
MhsTIF('Tono',27,'Bekasi', 21000),
MhsTIF('Justin',226,'Rembang', 125000)]

#1
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def checknimdong (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp
