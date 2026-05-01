from pemilih import Pemilih
from kandidat import Kandidat

def voting(pemilih, kandidat):
    return pemilih.memilih(kandidat)

def hitung_suara(kandidat):
    return kandidat.hitung_suara()