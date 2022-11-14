class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        result = []
        for player in sorted(self.players, key=lambda x: x.points, reverse=True):
            if player.nationality == nationality:
                result.append(player)
        return result