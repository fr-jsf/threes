from time import sleep
import os
import platform
import time
from ui.entries import *
from ui.play_display import *
from tiles.tiles_moves import *
from life_cycle.cycle_game import *
from life_cycle.play import *
from game.play import *
from check.tests import *

def threes():
    partie = None
    affiche = {"Linux" : [os.system, "clear"], "Windows" : [os.system, "cls"]}
    while True:
        affiche[platform.system()][0](affiche[platform.system()][1])
        choix = get_user_menu()
        while True:
            if choix == "Q":
                return False
            if choix == "N":
                partie = cycle_play(create_new_play())
                break
            elif choix == "L":
                partie = restore_game(partie)
                break
            elif choix == "S":
                save_game(partie)
                sleep(0.1)
                break
            elif choix == "T":
            	tests_global()
            	break
            elif choix == "C":
                partie = cycle_play(partie)
                sleep(0.1)
                break

threes()
print("Fin du jeu".center(32,"-"))
