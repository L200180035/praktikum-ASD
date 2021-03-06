class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = NIS
        self.umur = umur
        self.us = us
        
    def __str__(self):
        mns = 'nama '+ self.nama +', NIS '+str(self.nis)\
            +'. umur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap minggunya.'
        return mns
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nis
    def ambilumur(self):
        return self.umur
    def ambiluangsaku(self):
        return self.us

   
