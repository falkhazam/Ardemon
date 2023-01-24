from player import *
from creatures import *
from display import *
from game import *

ardtoise = Ardtoise(3)
ardtoise.available_xp = 100

pikachu = Pikardchu(3)
ardusaur = Ardusaur(2)
ardizard = Ardizard(2)

player1 = Player("COM9", [Ardtoise(3), Pikardchu(3), Ardizard(2)])
player2 = Player("COM5", [Ardizard(2), Pikardchu(3), Ardusaur(2)])

# dummy = Ardusaur(5)

# display1 = Display(player1)

# # player1.change_attack()
# # player1.change_attack()

# # att = player1.active_ardemon.attack(dummy, player1.active_ardemon.active_attack)
# display1.select_attack(False)

Battle(player1, player2)() # C++ esque



