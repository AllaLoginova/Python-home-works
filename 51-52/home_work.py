from random import randint

class  Player:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins


class Game:
    def __init__(self, player1, player2, num_of_throws_in_round=2):
        self.player1 = player1
        self.player2 = player2
        self.num_of_throws = num_of_throws_in_round

    def throw_cube(self):
        return randint(1, 6)

    def play_round(self):
        score1 = 0
        score2 = 0

        for _ in range(self.num_of_throws):
            score1 += self.throw_cube()

        for _ in range(self.num_of_throws):
            score2 += self.throw_cube()
            
        if score1 > score2:
            self.player1.wins += 1
            res = f"Победил {self.player1.name}"
        elif score2 > score1:
            self.player2.wins += 1
            res = f"Победил {self.player2.name}"
        else:
            res = f"Ничья"


        print(f"{self.player1.name} выбросил {score1}")
        print(f"{self.player2.name} выбросил {score2}")
        print(res)
        print()

    def get_statistics(self):
        print(f"{self.player1.name} - Побед {self.player1.wins}\n{self.player2.name} - Побед {self.player2.wins}")


player1 = Player("Alice")
player2 = Player("Bob")
game = Game(player1, player2)
game.play_round()
game.play_round()
game.get_statistics()
