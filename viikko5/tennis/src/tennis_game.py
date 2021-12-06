class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = {
            0: "Love", 
            1: "Fifteen", 
            2: "Thirty", 
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score >= 4 or self.player2_score >=4:
            return self.check_for_draw()
    
        else:
            return self.game_status()
        
    def deuce(self):
        return f"Deuce"

    def advantage(self):
        if self.player1_score > self.player2_score:
            return f"Advantage {self.player1_name}"
        return f"Advantage {self.player2_name}"

    def winner(self):
        if self.player1_score > self.player2_score:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def game_status(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"

    def check_for_draw(self):
        if self.player1_score == self.player2_score:
                return self.deuce()
        elif abs(self.player1_score - self.player2_score) == 1: 
            return self.advantage()

        return self.winner()


        


