
class PlayerStats:
    def __init__(self, PlayerStats):
        self.players = PlayerStats.get_players_list()

    def top_scorers_sorted(self):
        self.players.sort(key = lambda x: x.goals + x.assists, reverse = True)

        return self.players
