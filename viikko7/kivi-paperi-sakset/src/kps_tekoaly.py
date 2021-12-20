from tekoaly import Tekoaly
from kps_pelaa import KPS


class KPSTekoaly(KPS):
    def __init__(self, tekoaly = Tekoaly()):
        self.tekoaly = tekoaly

        
    def tokan_siirto(self, ensimmaisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()



 
 
