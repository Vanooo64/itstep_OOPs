class IteratorTeam:

    def __init__(self):
        self.team = Team()
        self.i = 0

    def __next__(self):
        if self.i < len(self.team.junior):
            x = self.i
            self.i += 1
            return self.team.junior[x]
        else:
            raise StopIteration

class Team:
    def __init__(self):
        self.junior = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer 4", "JPlayer 5"]
        self.seniors = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

    def __iter__(self):
        return IteratorTeam()

for x in Team():
    print(x)