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
            f"{self.defgamenumber} sayısını her tur 1 veya 2 çıkartarak karşıya 0 dedirmeye çalışacagız")
        time.sleep(2)
        print(f"negatif sayı söyleyemesin pass geçemesin ve sayı ekleyemesin")
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
            player = str(input("1 mi yoksa 2 mi çıkaracaksın:   "))
            if player == "1":
                self.minus_player(player=player)
                self.ai()

            elif player == "2":
                self.minus_player(player=player)
                self.ai()

            else:
                print("hatalı oynadın")

    def start_dev(self):
        self.gamenumber = self.defgamenumber
        self.start()

    def start_with_rules(self):
        self.gamenumber = self.defgamenumber
        os.system("cls")
        self.rules()
        self.start()


player = str(input("isminiz:    "))
game = Game(playername=player, defgamenumber=25)
game.start_dev()
