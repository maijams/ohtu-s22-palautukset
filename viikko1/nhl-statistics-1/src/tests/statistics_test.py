import unittest
from statistics import Statistics, SortBy
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
        
    def test_constructor_correct(self):
        self.assertEqual(str(self.statistics._players[1]), "Lemieux PIT 45 + 54 = 99")
        
    def test_existing_player_found(self):
        self.assertEqual(str(self.statistics.search("Kurri")), "Kurri EDM 37 + 53 = 90")
        
    def test_non_existing_player_returns_none(self):
        self.assertEqual(self.statistics.search("Koivu"), None)
    
    def test_existing_team_found(self):
        self.assertEqual(str(self.statistics.team("PIT")[0]), "Lemieux PIT 45 + 54 = 99")
        
    def test_non_existing_team_returns_empty_list(self):
        self.assertEqual(self.statistics.team(""), [])
        
    def test_correct_top_players(self):
        self.assertEqual(str(self.statistics.top(1)[0]), "Gretzky EDM 35 + 89 = 124")
    
    def test_correct_top_players_by_goals(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.GOALS)[0]), "Lemieux PIT 45 + 54 = 99")
        
    def test_correct_top_players_by_assists(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.ASSISTS)[0]), "Gretzky EDM 35 + 89 = 124")