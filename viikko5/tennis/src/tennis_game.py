class TennisGame:
    def __init__(self, p1_name, p2_name):
        self.p1_name, self.p1_points = p1_name, 0
        self.p2_name, self.p2_points = p2_name, 0
        
        self.score_terms = {
            0: "Love", 
            1: "Fifteen", 
            2: "Thirty", 
            3: "Forty"
            }

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_points += 1
        elif player_name == self.p2_name:
            self.p2_points += 1

    def deuce(self):
        if self.p1_points in range(0, 4):
            return self.score_terms[self.p1_points] + "-All"
        else:
            return "Deuce" 
        
    def points_over_four(self):
        difference = self.p1_points - self.p2_points
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def get_score(self):
        if self.p1_points == self.p2_points:
            return self.deuce()
        elif self.p1_points >= 4 or self.p2_points >= 4:
            return self.points_over_four()    
        else:
            return self.score_terms[self.p1_points] + "-" + self.score_terms[self.p2_points]