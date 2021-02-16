class Game():
    def __init__(self, gamenumber) -> int:
        self.gamenumber = int(gamenumber)

    def start(self):
        print(f"start {self.gamenumber}")


game = Game(25)
game.start()
