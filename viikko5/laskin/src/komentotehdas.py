class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus
        self.edellinen = self.sovellus.tulos
        print(self.edellinen)

    def suorita(self):
        return self.sovellus.plus(self.io())
    def palauta(self):
        return self.sovellus.aseta_arvo(self.edellinen)



class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus
        self.edellinen = self.sovellus.tulos
        print(self.edellinen)

    def suorita(self):
        return self.sovellus.miinus(self.io())
    def palauta(self):
        return self.sovellus.aseta_arvo(self.edellinen)

class Nollaus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus

    def suorita(self):
        return self.sovellus.nollaa()




    










