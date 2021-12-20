from kps_pelaa import KPS

class KPSPelaajaVsPelaaja(KPS):        

    def _toisen_siirto(self, ensimmainen_siirto):
        self.tokan_siirto = input("Toisen pelaajan siirto: ")

        return self.tokan_siirto

