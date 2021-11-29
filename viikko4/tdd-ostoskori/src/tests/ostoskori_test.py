import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_ostoskorin_tuotteiden_maara_on_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("juusto", 4))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)       
