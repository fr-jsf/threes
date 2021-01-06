from os import path
import sys
sys.path.append("../")
from ui.pygetch.getch.getch import *
from life_cycle.play import *

def test_get_user_menu():
    """
    Test de la fonction get_user_menu
    """
    acceptable = [110, 78, 76, 108, 115, 83, 99, 67, 113, 81]
    while True:
        print("Appuyer sur ECHAP pour quitter.")
        char = ord(getch())
        if char == 27:
            break
        elif char in acceptable :
            print('La valeur est valide.')
        else:
            print("La valeur n'est pas valide.")
    print("Test de la fonction get_user_menu : OK")

def test_json() :
    """
    Test de fonction save_game et restore_game
    """
    partie = create_new_play()
    save_game(partie)
    partie2 = restore_game(partie)
    assert partie == partie2
    partie3 = restore_game(partie)
    assert partie3 == create_new_play
    print("Test de la fonction save_game et restore_game : OK")
	
def test_create_new_play(): 
	"""
	Test de la fonction create_new_play
	"""
	partie = create_new_play()
	assert partie["score"] == 3 and partie["plateau"]["tiles"] != [0 for i in range(16)]
	assert get_value(partie['plateau'], partie['next-tile']["0"]["lig"], partie['next-tile']["0"]["col"]) == partie['next-tile']["0"]["val"] and get_value(partie['plateau'], partie['next-tile']["1"]["lig"], partie['next-tile']["1"]["col"]) == partie['next-tile']["1"]["val"]
	print('Test de la fonction create_new_play : OK')

def test_get_user_move():
        """
        Test de la fonction get_user_move
        """
        menu = [77, 109]
        if platform.system() == "Linux":
                fleches = {27 : {91 : {65 : 'h', 66 : 'b', 67 : 'd', 68 : 'g'}}}
                while True:
                        print("Appuyez sur ECHAP pour quiiter")
                        char = ord(getch())
                        if char == 27:
                            break
                        elif char in menu:
                                print("La valeur communiqué est valide.")
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[27]):
                                        char = ord(getch())
                                        if char in list(fleches[27][91]):
                                                print("La valeur communiqué est valide.")
                        else:
                            print("La valeur communiqué n'est pas valide.")
        else:
                fleches = {0 : {72 : 'h', 75 : 'g', 77 : 'd', 80 : 'b'}}
                while True:
                        print("Appuyez sur ECHAP pour quitter")
                        char = ord(getch())
                        if char == 27:
                            break
                        elif char in menu:
                            print("La valeur communiqué est valide.")
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[0]):
                                        print("La valeur communiqué est valide.")
                        else:
                            print("La valeur communiqué n'est pas valide.")
        print("Test de la fonction get_user_move : OK")