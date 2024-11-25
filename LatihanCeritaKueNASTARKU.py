import random
import os

class CeritaTokoNastarku:
    def _init_(self):
        self.kue_kering = ["Nastar", "Kastengel", "Rentak_Keju"]
        self.kue_basah = ["Masubah", "Bolu_Gulung"]
        self.cemilan = ["Donut", "Risol", "Jus_KacangIjo"]

    def buat_cerita(self):
        random_kue_kering = random.choice(self.kue_kering)
        random_kue_basah = random.choice(self.kue_basah)
        random_cemilan = random.choice(self.cemilan)

        os.system("cls" if os.name == "nt" else "clear")

        print(
            f"Saya membeli makanan. di toko nastarku "
            f"Saya memilih makanan terenak yaitu {random_cemilan} dan membeli kue basah terenak yaitu {random_kue_basah}. "
            f"Saya juga membeli kue kering yaitu kue {random_kue_kering}. yang saya jual lagi untuk mendapatkan keuntungan pribadi."
        )

def main():
    cerita = CeritaTokoNastarku()
    cerita.buat_cerita()

if __name__ == "_main_":
    main()