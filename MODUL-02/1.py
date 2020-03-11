class Pesan(object):

    #a
    def __init__(self, kata):
        self.kata = kata

    def apakahTerkandung(self, bo):
        if bo in self.kata:
            return True
        else:
            return False

    #b
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for i in self.kata:
            if i in vokal:
                v+=1
        kf = len(self.kata) - v
        return kf

    #c 
    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for i in self.kata:
            if i in vokal:
                v+=1
        return v
