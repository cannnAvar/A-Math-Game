import time
import os


class Game():
    def __init__(self, playername, defgamenumber, gamenumber=0) -> int:
        self.playername = str(playername)
        self.defgamenumber = int(defgamenumber)
        self.gamenumber = int(gamenumber)
        self.loop = False

    def rules(self):
        print(
            f"{self.defgamenumber} minus 1 or 2 and")
        time.sleep(2)
        print("If you say 0 you loose")
        time.sleep(2)
        print("you loose")
        time.sleep(2)

    def minus_player(self, player):
        self.gamenumber -= int(player)
        print(f"{self.playername}||{self.gamenumber}||" + f"{player}")

    def ai(self):
        if self.gamenumber in [24, 21, 18, 15, 12, 9, 6, 3]:
            numb = 2
        elif self.gamenumber in [23, 20, 17, 14, 11, 8, 5, 2]:
            numb = 1

        self.gamenumber -= int(numb)
        print(f"AI||{self.gamenumber}||" + f"{numb}")

    def start(self):
        self.loop = True
        while self.loop:
            if self.gamenumber <= 0:
                self.loop = False
                self.finish()
            player = str(input("minus 1 or minus2:   "))
            if player == "1":
                self.minus_player(player=player)
                self.ai()

            elif player == "2":
                self.minus_player(player=player)
                self.ai()

            else:
                print("you play wrong")

    def start_dev(self):
        self.gamenumber = self.defgamenumber
        self.start()

    def start_with_rules(self):
        self.gamenumber = self.defgamenumber
        os.system("cls")
        self.rules()
        self.start()

    def finish(self):
        print("you lose")


player = str(input("your name:    "))
game = Game(playername=player, defgamenumber=25)
game.start_with_rules()
