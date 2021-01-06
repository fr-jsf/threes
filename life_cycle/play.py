from os import path
from life_cycle.cycle_game import *
from ui.play_display import *
from ui.entries import *
from tiles.tiles_moves import *
from game.play import *
import json

def cycle_play(partie):
        """
        Gère une partie de threes/media/11906062/8EA5-D70D/jeu_threes_v3/
        """
        import os
        import platform
        affiche = {"Linux" : [os.system, "clear"], "Windows" : [os.system, "cls"]}
        if partie is None:
            print("Aucune partie en cours".center(32, "-"))
        else:
                while not is_game_over(partie["plateau"]):
                        affiche[platform.system()][0](affiche[platform.system()][1])
                        full_display(partie["plateau"])
                        if get_nb_empty_rooms(partie["plateau"])!= 0:
                                partie["next-tile"] = get_next_alea_tiles(partie["plateau"], "encours")
                        else:
                                partie["next-tile"]["0"]["val"] = "x"
                        print("Score : " + str(partie["score"]) + " ".center(7) + "Prochaine tuile : " + str(partie["next-tile"]["0"]["val"]))
                        choix = get_user_move()
                        if choix == "m":
                                return partie
                        else:
                                if get_nb_empty_rooms(partie["plateau"]) == 0:
                                        play_move(partie["plateau"], choix)
                                        partie["score"] = get_score(partie["plateau"])
                                else:
                                        play_move(partie["plateau"], choix)
                                        tile = get_next_alea_tiles(partie["plateau"], "encours")
                                        tile["0"]["val"] = partie["next-tile"]["0"]["val"]
                                        partie["next-tile"] = tile
                                        put_next_tiles(partie["plateau"], partie["next-tile"])
                                        partie["score"] = get_score(partie["plateau"])

                affiche[platform.system()][0](affiche[platform.system()][1])
                full_display(partie["plateau"])
                print("La partie est terminée".center(35, "-"))
                ord(getch())
                return None

def save_game(partie):
        """
        Sauvegarde une partie de threes
        """
        assert partie is None or type(partie) is dict, "Erreur !"
        if partie is None:
        	print("Rien à sauvegarder".center(32, "-"))
        else:
	        fic = open("saved_game.json", 'w')
        	fic.write(json.dumps(partie))
        	fic.close()
        	print("Partie sauvegardée".center(32,"-"))

def restore_game(partie):
        """
        Restaure une partie de threes sauvegardé
        """
        assert partie is None or type(partie) is dict, "Erreur !"
        with open('saved_game.json') as fic:
                if fic.read() == "null":
                        return cycle_play(create_new_play())
                else:
                        fic.seek(0)
                        return cycle_play(json.load(fic))
