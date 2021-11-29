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

    
