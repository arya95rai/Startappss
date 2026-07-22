from collections import OrderedDict

class LeaderBoard:
    def __init__(self):
        self.players = OrderedDict()

    def update_score(self, name, score):
        self.players[name] = score

    def latest_score(self, name):
        if name in self.players:
            print(f"{name}'s Latest Score: {self.players[name]}")
        else:
            print("Player not found")

    def highest_score(self):
        if not self.players:
            print("No players")
            return

        player = max(self.players, key=self.players.get)
        print(f"Highest Score: {player} -> {self.players[player]}")

    def top_10_players(self):
        print("Top Players")
        top = sorted(self.players.items(),
                     key=lambda x: x[1],
                     reverse=True)[:10]

        for rank, (player, score) in enumerate(top, start=1):
            print(f"{rank}. {player} : {score}")


# ---------------- Driver Code ----------------

lb = LeaderBoard()

lb.update_score("Rahul", 450)
lb.update_score("Aman", 620)
lb.update_score("Priya", 510)
lb.update_score("Arya", 700)
lb.update_score("Rohit", 580)

lb.latest_score("Rahul")
print()

lb.highest_score()
print()

lb.top_10_players()