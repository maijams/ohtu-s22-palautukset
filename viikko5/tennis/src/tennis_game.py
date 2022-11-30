class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1

    def deuce(self):
        return self.player1_points == self.player2_points
        
    def points_over_four(self):
        return self.player1_points >= 4 or self.player2_points >= 4
        
    def get_score(self):
        score = ""
        score_terms = {
            0: "Love", 
            1: "Fifteen", 
            2: "Thirty", 
            3: "Forty"
            }
        
        if self.deuce():
            if self.player1_points in range(0, 4):
                score = score_terms[self.player1_points] + "-All"
            else:
                score = "Deuce"
        elif self.points_over_four():
            difference = self.player1_points - self.player2_points
            
            if difference == 1:
                score = "Advantage player1"
            elif difference == -1:
                score = "Advantage player2"
            elif difference >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = score_terms[self.player1_points] + "-" + score_terms[self.player2_points]

        return score
