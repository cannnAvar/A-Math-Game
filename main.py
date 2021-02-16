import time
import os
import math

class Game():
    def __init__(self, defgamenumber, gamenumber=0) -> int:
        self.defgamenumber = int(defgamenumber)
        self.gamenumber = int(gamenumber)
        self.loop = False

    def rules(self):
        print(
            f"{self.defgamenumber} sayısını her tur 1 veya 2 çıkartarak karşıya 0 dedirmeye çalışacagız")
        time.sleep(2)
        print(f"negatif sayı söyleyemesin pass geçemesin ve sayı ekleyemesin")
        time.sleep(2)

    def minus_player(self,player):
        self.gamenumber -= int(player)
        print(f"||{self.gamenumber}||" + f"{player}")

    def ai(self):
        numb = 
        self.gamenumber -= int(numb)
        print(f"||{self.gamenumber}||" + f"{numb}")

    def start(self):
        self.loop = True
        while self.loop:
            player = str(input("1 mi yoksa 2 mi çıkaracaksın:   "))
            if player == "1":
                self.minus_player(player=player)
                
            elif player == "2":
                self.minus_player(player=player)
                
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


game = Game(26)
game.start_dev()
