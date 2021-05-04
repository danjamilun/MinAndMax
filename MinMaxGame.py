from random import choice


class Game:
    def __init__(self):
        self.sticks = 11 
        self.player = "player1" 

    def __str__(self):
        return str(self.sticks) + "  " +self.player 

    def action(self, act):
        self.sticks = self.sticks-act 

    def undo_action(self, act):
        self.sticks = self.sticks+act

    def all_actions(self):
        actionList = [1, 2]
        return actionList

    def check(self): 
        if self.sticks == 0:
            return True

        elif self.sticks == 1:
            return False

        elif self.sticks < 0:
            return False

        return 2

    def changePlayer(self):
        if self.player == "player2":
            self.player = "player1"
        else:
            self.player = "player2"


def miniMax(game, d):
    result = game.check()
    gameplayer = game.player
    if result != 2:
        if result == True:
            return(-100+d, None)
        elif result == False:
            return(100-d, None)
    if gameplayer == "player1":
        maxv, best_act = -1000, None
        for a in game.all_actions():
            game.action(a)
            game.changePlayer()
            v, _ = miniMax(game, d+1)
            game.undo_action(a)
            if v > maxv:
                maxv = v
                best_act = a
        return (maxv, best_act)
    else:
        minv, best_act = 1000, None
        for a in game.all_actions():
            game.action(a)
            game.changePlayer()
            v, _ = miniMax(game, d+1)
            game.undo_action(a)
            if v < minv:
                minv = v
                best_act = a
        return (minv, best_act)

def Playing(game):
    while True:
        print(game)
        stick = int(input("Odaberite 1 ili 2 štapića sa poda  "))
        game.action(stick)
        if game.check() == True:
            print(game.player+" pobjednik")
            break
        elif game.check() == False:
            print(game.player+" gubitnik")
            break
        game.changePlayer()
        print(game)
        print("\n")
        value, stickKomp = miniMax(game, 0)
        game.action(stickKomp)
        print("Racunalo igra {0}".format(stickKomp))
        if game.check() == True:
            print(game.player+" pobjednik")
            break
        elif game.check() == False:
            print(game.player+" gubitnik")
            break
        game.changePlayer()
        print(game)
        print("\n")
if __name__ == '__main__':
    game = Game()
    Playing(game)
    