from check.partie1 import *
from check.partie2 import *
from check.partie3 import *

def tests_partie1():
    test_init_play()
    test_check_indice()
    test_check_room()
    test_is_room_empty()
    test_set_value()
    test_get_value()
    test_get_nb_empty_rooms()
    test_is_game_over()
    test_get_score()
    print("Fin des tests de la partie 1")

def tests_partie2():
    test_line_move()
    test_line_pack()
    test_lines_move()
    test_column_move()
    test_column_pack()
    test_columns_move()
    test_get_next_alea_tiles()
    test_put_next_tiles()
    test_play_move()
    print("Fin des tests de la partie 2")

def tests_partie3():
    test_create_new_play()
    test_get_user_menu()
    test_get_user_move()
    #test_json()
    print("Fin des tests de la partie 3")


def tests_global():
    import platform
    import os
    affiche = {"Linux" : [os.system, "clear"], "Windows" : [os.system, "cls"]}
    affiche[platform.system()][0](affiche[platform.system()][1])
    tests_partie1()
    tests_partie2()
    tests_partie3()