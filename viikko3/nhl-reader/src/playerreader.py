import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []
    
    def get_players(self):
        for player_dict in self.response:
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['penalties'], player_dict['team'], player_dict['games']
            )
            
            self.players.append(player)
        return self.players