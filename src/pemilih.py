class Pemilih:
    def __init__(self, id_pemilih, nama):
        self.id_pemilih = id_pemilih
        self.nama = nama
        self.sudah_memilih = False

    def memilih(self, kandidat):
        if self.sudah_memilih:
            return "Pemilih sudah memilih."
        self.sudah_memilih = True
        kandidat.tambah_suara()
        return f"{self.nama} memilih {kandidat.nama}"