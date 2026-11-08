import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_team_returns_players_of_given_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertTrue(all(player.team == "EDM" for player in players))

    def test_team_returns_empty_list(self):
        players = self.stats.team("Nonexistent Team")
        self.assertEqual(len(players), 0)

    def test_top_returns_top_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
        self.assertEqual(top_players[3].name, "Kurri")

    def test_top_returns_empty_list_for_zero(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")
    