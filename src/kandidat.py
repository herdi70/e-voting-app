class Kandidat:
    def __init__(self, id_kandidat, nama):
        self.id_kandidat = id_kandidat
        self.nama = nama
        self.suara = 0

    def tambah_suara(self):
        self.suara += 1

    def hitung_suara(self):
        return self.suara