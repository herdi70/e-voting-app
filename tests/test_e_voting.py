import unittest
from src.pemilih import Pemilih
from src.kandidat import Kandidat
from src.e_voting import voting, hitung_suara

class TestE_Voting(unittest.TestCase):
    
    def test_voting(self):
        pemilih = Pemilih(1, "Andi")
        kandidat = Kandidat(101, "Budi")
        
        # Pemilih memilih
        hasil = voting(pemilih, kandidat)
        self.assertEqual(hasil, "Andi memilih Budi")
        self.assertTrue(pemilih.sudah_memilih)

        # Cek pemilih yang sama memilih lagi
        hasil_ulang = voting(pemilih, kandidat)
        self.assertEqual(hasil_ulang, "Pemilih sudah memilih.")
        
    def test_hitung_suara(self):
        kandidat = Kandidat(101, "Budi")
        # Cek suara awal
        self.assertEqual(hitung_suara(kandidat), 0)
        
        # Pemilih memberikan suara
        pemilih = Pemilih(1, "Andi")
        voting(pemilih, kandidat)
        
        # Cek suara setelah memilih
        self.assertEqual(hitung_suara(kandidat), 1)
        
    def test_integrasi(self):
        pemilih1 = Pemilih(1, "Andi")
        pemilih2 = Pemilih(2, "Budi")
        kandidat1 = Kandidat(101, "Budi")
        kandidat2 = Kandidat(102, "Susi")

        # Pemilih memberikan suara
        voting(pemilih1, kandidat1)  # Andi memilih Budi
        voting(pemilih2, kandidat2)  # Budi memilih Susi

        # Hitung suara akhir
        self.assertEqual(hitung_suara(kandidat1), 1)
        self.assertEqual(hitung_suara(kandidat2), 1)

if __name__ == '__main__':
    unittest.main()