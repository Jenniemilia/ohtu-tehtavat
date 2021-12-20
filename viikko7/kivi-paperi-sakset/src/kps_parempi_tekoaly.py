from tekoaly_parannettu import TekoalyParannettu
from kps_pelaa import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self, tekoaly):
 
        self.tekoaly = TekoalyParannettu(10)

        self.tokan_siirto = self.tekoaly.anna_siirto()

        return self.tokan_siirto



