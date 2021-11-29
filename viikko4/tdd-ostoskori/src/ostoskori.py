from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if self.ostokset is None:
            return 0
        
        lukumaara = 0
        for ostos in self.ostokset.values():
            lukumaara += ostos.lukumaara()
        return lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if self.ostokset is None:
            return 0

        hinta = 0
        for ostos in self.ostokset.values():
            hinta += ostos.hinta()

        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)

        if lisattava.nimi() not in self.ostokset.keys():
            self.ostokset[lisattava.nimi()] = ostos

        else:
            self.ostokset[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self.ostokset.clear()
        # tyhjentää ostoskorin

    def ostokset(self):

        return list(self.ostokset.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
