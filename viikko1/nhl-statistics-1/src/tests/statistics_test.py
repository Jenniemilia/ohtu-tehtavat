import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_if_name_found(self):
        found = self.statistics.search("Semenko")
        self.assertEqual(found.name, "Semenko")

    def test_search_if_name_not_found(self):
        found = self.statistics.search("Nylund")
        self.assertEqual(found, None)

    def test_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_top_scores(self):
        found = self.statistics.top_scorers(2)
        self.assertEqual(len(found), 3)