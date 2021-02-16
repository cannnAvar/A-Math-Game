import time
import os


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

    def start(self):
        self.loop = True
        while self.loop:
            player = str(input("1 mi yoksa 2 mi çıkaracaksın:   "))
            if player == "1":
                pass
            elif player == "2":
                pass
            else:
                print("hatalı oynadın")

    def start_dev(self):
        self.start()

    def start_with_rules(self):
        os.system("cls")
        self.rules()
        self.start()


game = Game(25)
game.start_dev()
