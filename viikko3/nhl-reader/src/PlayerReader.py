import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
  
    def get_players_list(self):
        response = requests.get(self.url).json()
        self.players = []

        for player_dict in response:
            if player_dict['nationality'] == 'FIN':
                player = Player(
                    player_dict['name'],
                    player_dict['nationality'],
                    player_dict['team'],
                    player_dict['goals'],
                    player_dict['assists']
                    )
                self.players.append(player)

        return self.players