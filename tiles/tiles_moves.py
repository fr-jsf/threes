import sys
from os import path
sys.path.append(path.abspath('../'))
from random import *
from tiles.tiles_acces import *
from life_cycle.cycle_game import is_game_over

def get_nb_empty_rooms(plateau):
    """
    Met à jour le nombre de cases libres du plateau
    """
    somme = 0
    for i in range(0, int(len(plateau['tiles']) / plateau['n'])):
        for j in range (0, int(len(plateau['tiles']) / plateau['n'])):
            if is_room_empty(plateau, i, j):
                somme += 1
    plateau['nombre_cases_libres'] = somme
    return somme

def get_next_alea_tiles(plateau, mode):
    if mode.upper() == "INIT" and get_nb_empty_rooms(plateau) >= 2 or mode.upper() == "ENCOURS" and get_nb_empty_rooms(plateau) >= 1:
        if mode.upper() == "INIT":
            tableau = {'mode' : "init", 'check' :  not is_game_over(plateau), '0' : {'val' : 1, 'lig' : randint(0,3), 'col' : randint(0,3)}, '1' : {'val' : 2, 'lig' : randint(0,3), 'col' : randint(0,3)}}
            while not ( is_room_empty(plateau,tableau["0"]["lig"], tableau["0"]["col"]) and  is_room_empty(plateau, tableau["1"]["lig"], tableau["1"]["col"]) and  not(tableau["0"]["lig"] == tableau["1"]["lig"] and tableau["0"]["col"] == tableau["1"]["col"])):
                tableau["0"] = {'val' : 1, 'lig' : randint(0,3), 'col' : randint(0,3)}
                tableau["1"] = {'val' : 2, 'lig' : randint(0,3), 'col' : randint(0,3)}
        else:
            tableau = {'mode' : 'encours', 'check' : not is_game_over(plateau), '0' : {'val' : randint(1,3), 'lig' : randint(0,3), 'col' : randint(0,3)}}
            while not (is_room_empty(plateau, tableau["0"]["lig"], tableau["0"]["col"])):
                tableau["0"] = {'val' : randint(1,3), 'lig' : randint(0,3), 'col' : randint(0,3)}
        return tableau
    else:
        return 'Erreur !'

def put_next_tiles(plateau, tableau):
    """
    Permet de placer les tuiles générés par la fonction get_next_alea_tiles
    """
    if tableau["mode"] == "init":
        set_value(plateau, tableau["0"]["lig"], tableau["0"]["col"], tableau["0"]["val"])
        set_value(plateau, tableau["1"]["lig"], tableau["1"]["col"], tableau["1"]["val"])
    elif tableau["mode"] == "encours":
        set_value(plateau, tableau["0"]["lig"], tableau["0"]["col"], tableau["0"]["val"])

def line_pack(plateau, num_lig, debut, sens):
    """
    Tasse les tuiles d'une ligne dans un sens donné (1 pour gauche et 0 pour droite).
    """
    if 0 <= debut <= plateau['n'] - 1 and sens in (0,1) and 0 <= num_lig <= plateau['n'] - 1:
        if sens == 0:
            for i in range(num_lig * 4 + debut, num_lig * 4, -1):
                set_value(plateau, num_lig, i % 4, plateau["tiles"][i - 1])
            set_value(plateau, num_lig, 0, 0)
        else:
            for i in range(num_lig * 4 + debut, num_lig * 4 + 3):
                set_value(plateau, num_lig, i % 4, plateau["tiles"][i + 1])
            set_value(plateau, num_lig, plateau['n'] - 1, 0)
    else:
        return "Erreur !"

def column_pack(plateau, num_col, debut, sens):
    """
    Tasse les tuiles d'une colonne donné dans un sens donné
    """
    if 0 <= debut <= plateau['n'] - 1 and sens in (0,1) and 0 <= num_col <= plateau['n'] - 1:
        if sens == 0:
            for i in range(num_col + debut * 4, num_col, -4):
                set_value(plateau, i // 4, num_col, plateau["tiles"][i - 4])
            set_value(plateau, 0, num_col, 0)
        else:
            for i in range(num_col + debut * 4, num_col + 12, 4):
                set_value(plateau, i // 4, num_col, plateau["tiles"][i + 4])
            set_value(plateau, plateau['n'] - 1, num_col, 0)
    else:
        return 'Erreur !'

def line_move(plateau, num_lig, sens):
    """
    Déplace les tuiles d'une ligne dans un sens donné
    """
    if 0 <= num_lig <= plateau['n'] - 1 and sens in (0,1):
        if sens == 0:
            for i in range(plateau['n'] - 1, 0, -1):
                tuile1 = get_value(plateau, num_lig, i)
                tuile2 = get_value(plateau, num_lig, i - 1)
                if tuile1 == 0:
                    line_pack(plateau, num_lig, i, sens)
                    break
                elif (tuile1 + tuile2) % 3 == 0 and tuile1 * tuile2 != 0 and (tuile1 == tuile2 or tuile1 in [1,2]):
                    set_value(plateau, num_lig, i - 1, tuile1 + tuile2)
                    line_pack(plateau, num_lig, i, sens)
                    break

        else:
            for i in range(plateau['n'] - 1):
                tuile1 = get_value(plateau, num_lig, i)
                tuile2 = get_value(plateau, num_lig, i + 1)
                if tuile1 == 0:
                    line_pack(plateau, num_lig, i, sens)
                    break
                elif (tuile1 + tuile2) % 3 == 0 and tuile1 * tuile2 != 0 and (tuile1 == tuile2 or tuile1 in [1,2]):
                    set_value(plateau, num_lig, i, tuile1 + tuile2)
                    line_pack(plateau, num_lig, i + 1, sens)
                    break
    else:
        return 'Erreur !'
    
def column_move(plateau, num_col, sens):
    """
    Déplace les tuiles d'une colonne dans un sens donné
    """
    if 0 <= num_col <=  plateau['n'] - 1 and sens in (0,1):
        if sens == 0:
            for i in range(plateau['n'] - 1, 0, -1):
                tuile1 = get_value(plateau, i, num_col)
                tuile2 = get_value(plateau, i - 1, num_col)
                if tuile1 == 0:
                    column_pack(plateau, num_col, i, sens)
                    break
                elif (tuile1 + tuile2) % 3 == 0 and tuile1 * tuile2 != 0 and (tuile1 == tuile2 or tuile1 in [1,2]):
                    set_value(plateau, i, num_col, tuile1 + tuile2)
                    column_pack(plateau, num_col, i - 1, sens)
                    break
        else:
            for i in range(plateau['n'] - 1):
                tuile1 = get_value(plateau, i, num_col)
                tuile2 = get_value(plateau, i + 1, num_col)
                if tuile1 == 0:
                    column_pack(plateau, num_col, i, sens)
                    break
                elif (tuile1 + tuile2) % 3 == 0 and tuile1 * tuile2 != 0 and (tuile1 == tuile2 or tuile1 in [1,2]):
                    set_value(plateau, i + 1, num_col, tuile1 + tuile2)
                    column_pack(plateau, num_col, i, sens)
                    break
    else:
        return 'Erreur !'
    
def lines_move(plateau, sens):
    """
    Déplace les tuiles de toutes lignes du plaateau dans un sens donné
    """
    if 0 <= sens <= 1:
        if sens == 0:
            for i in range(0, plateau['n']):
                 line_move(plateau, i, sens)
        else:
            for i in range(0, plateau['n']):
                line_move(plateau, i, sens)
    else:
        return 'Erreur !'
    
def columns_move(plateau, sens):
    """
    Déplace les tuiles de toutes les colonnes du plateau dans un sens donné
    """
    if 0 <= sens <= 1:
        if sens == 0:
            for i in range(0, plateau['n']):
                column_move(plateau, i, sens)
        else:
            for i in range(0, plateau['n']):
                column_move(plateau, i, sens)
    else:
        return 'Erreur !'
    
def play_move(plateau, sens):
    """
    Déplace les tuiles d'un plateau dans un sens donné
    """
    choix = {
		"h": [columns_move, 1],
		"b": [columns_move, 0],
		"g": [lines_move, 1],
		"d": [lines_move, 0]
    }
    if sens in list(choix):
        choix[sens][0](plateau, choix[sens][1])
    else:
        return 'Erreur !'
