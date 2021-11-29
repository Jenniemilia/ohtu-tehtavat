import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_tavara(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("juusto", 4))
        self.kori.lisaa_tuote(Tuote("leipä", 6))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_oikein(self):
        self.kori.lisaa_tuote(Tuote("juusto", 4))
        self.kori.lisaa_tuote(Tuote("leipä", 6))
        self.assertEqual(self.kori.hinta(), 10)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_oikein(self):
        self.kori.lisaa_tuote(Tuote("juusto", 4))
        self.kori.lisaa_tuote(Tuote("juusto", 4))
        self.assertEqual(self.kori.hinta(), 8)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote, maito)
        self.assertEqual(ostos.hinta(), 3)
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        kahvi = Tuote("kahvi", 6)
        banaani = Tuote("Banaani", 2)

        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(banaani)

        ostokset = self.kori.ostokset

        self.assertEqual(len(ostokset), 2)
