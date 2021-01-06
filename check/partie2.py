from os import path
import sys
sys.path.append("../")
from tiles.tiles_moves import *

def test_get_next_alea_tiles() : 
    """
    Test de la fonction get_next_alea_tiles
    """
    plateau = {
        'n' : 4,
		'nombre_cases_libres' : 16,
		'tiles' : [1,0,2,1,2,1,2,1,2,1,2,1,1,2,1,2]
	}
    mode = 'init'
    assert get_next_alea_tiles(plateau, mode) == 'Erreur !'
    plateau["tiles"] = [1,0,2,1,2,1,2,1,2,1,2,0,1,2,1,2]
    tableau = get_next_alea_tiles(plateau, mode)
    assert tableau == {'mode' : 'init', 'check' : True, '0' : {'val': 1, 'lig' : 0, 'col' : 1},'1' : {'val': 2, 'lig' : 2, 'col' : 3}} or tableau == {'mode' : 'init', 'check' : True, '0' : {'val': 1, 'lig' : 2, 'col' : 3}, '1' : {'val': 2, 'lig' : 0, 'col' : 1}}
    mode = 'encours'
    plateau["tiles"] = [1,2,2,1,2,1,2,1,2,1,2,2,1,2,1,2]
    assert get_next_alea_tiles(plateau, mode) == 'Erreur !'
    plateau["tiles"] = [1,1,2,1,2,1,2,1,2,1,2,0,1,2,1,2]
    tableau = get_next_alea_tiles(plateau, mode)
    assert tableau == {'mode' : 'encours', 'check' : True, '0' : {'val': 1, 'lig' : 2, 'col' : 3}} or tableau == {'mode' : 'encours', 'check' : True, '0' : {'val': 2, 'lig' : 2, 'col' : 3}} or tableau == {'mode' : 'encours', 'check' : True, '0' : {'val': 3, 'lig' : 2, 'col' : 3}}
    print('Test de la fonction get_next_alea_tiles : OK')
	
def test_put_next_tiles() : 
	"""
	Test de la fonction put_next_tiles
	"""
	plateau = {
        'n' : 4,
		'nombre_cases_libres' : 16,
		'tiles' : [1,0,2,1,2,1,2,1,2,1,2,1,1,2,1,2]
	}
	tableau = {'mode' : 'encours', 'check' : True, '0' : {'val': 1, 'lig' : 0, 'col' : 1}}
	put_next_tiles(plateau, tableau)
	assert plateau["tiles"] == [1,1,2,1,2,1,2,1,2,1,2,1,1,2,1,2]
	plateau["tiles"] = [0,1,2,1,2,0,2,1,2,1,2,1,1,2,0,2]
	tableau = {'mode' : 'encours', 'check' : True, '0' : {'val': 3, 'lig' : 2, 'col' : 2}}
	put_next_tiles(plateau, tableau)
	assert plateau["tiles"] == [0,1,2,1,2,0,2,1,2,1,3,1,1,2,0,2]
	plateau["tiles"] = [1,0,2,1,2,1,2,1,2,1,2,0,1,2,1,2]
	tableau = {'mode' : 'init', 'check' : True, '0' : {'val': 1, 'lig' : 0, 'col' : 1},'1' : {'val': 2, 'lig' : 2, 'col' : 3}}
	put_next_tiles(plateau, tableau)
	assert plateau["tiles"] == [1,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2] 
	print('Test de la fonction put_next_tiles : OK') 

def test_line_pack():
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 1, 
        'tiles': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    }
    #Pour droite
    line_pack(plateau, 1, 1, 0)
    assert plateau['tiles'] == [0, 1, 2, 3, 0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    line_pack(plateau, 2, 3, 0)
    assert plateau['tiles'] == [0,  1, 2, 3, 0,  4, 6, 7, 0,  8, 9, 10, 12, 13, 14, 15]
    #Pour gauche
    line_pack(plateau, 1, 1, 1)
    assert plateau['tiles'] == [0, 1, 2, 3, 0, 6, 7, 0, 0, 8, 9, 10, 12, 13, 14, 15]
    line_pack(plateau, 2, 3, 1)
    assert plateau['tiles'] == [0, 1, 2, 3, 0, 6, 7, 0, 0, 8, 9, 0, 12, 13, 14, 15]
    #Pour les valeurs non cohérantes 
    assert line_pack(plateau, 4, 3, 1) and line_pack(plateau, -4, -3, 0) == "Erreur !"
    assert line_pack(plateau, 0, 0, 4) and line_pack(plateau, 0, 0, -4) == "Erreur !"
    print("Test de la fonction line_pack : OK")

def test_line_move():
    """
    Test de la fonction line_move
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 8, 
        'tiles': [0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0, 13, 0, 15]
    }
    #Pour droite
    line_move(plateau, 1, 0)
    assert plateau['tiles'] == [0, 1, 0, 3, 0, 0, 5, 7, 0, 9, 0, 11, 0, 13, 0, 15]
    line_move(plateau, 3, 0)
    assert plateau['tiles'] == [0, 1, 0, 3, 0, 0, 5, 7, 0, 9, 0, 11, 0, 0, 13, 15]
    #Pour gauche
    line_move(plateau, 1, 1)
    assert plateau['tiles'] == [0, 1, 0, 3, 0, 5, 7, 0, 0, 9, 0, 11, 0, 0, 13, 15]
    line_move(plateau, 3, 1)
    assert plateau['tiles'] == [0, 1, 0, 3, 0, 5, 7, 0, 0, 9, 0, 11, 0, 13, 15, 0]
    #Pour les valeurs non cohérantes 
    assert line_move(plateau, 4, 1) and line_move(plateau, -4, 0) == "Erreur !"
    assert line_move(plateau, 0, 4) and line_move(plateau, 0, -4) == "Erreur !"
    print("Test de la fonction line_move : OK")

def test_column_pack():
    """
    Test de la fonction column_pack
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 1, 
        'tiles': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    }
    #Pour bas
    column_pack(plateau, 1, 1, 0)
    assert plateau['tiles'] == [0, 0, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    column_pack(plateau,2, 3, 0)
    assert plateau['tiles'] == [0, 0, 0, 3, 4, 1, 2, 7, 8, 9, 6, 11, 12, 13, 10, 15]
    #Pour haut
    column_pack(plateau, 1, 1, 1)
    assert plateau['tiles'] == [0, 0, 0, 3, 4, 9, 2, 7, 8, 13, 6, 11, 12, 0, 10, 15]
    column_pack(plateau, 2, 3, 1)
    assert plateau['tiles'] == [0, 0, 0, 3, 4, 9, 2, 7, 8, 13, 6, 11, 12, 0, 0, 15]
    #Pour les valeurs non cohérantes
    assert column_pack(plateau, 4, 3, 1) and column_pack(plateau, -4, -3, 0) == "Erreur !"
    assert column_pack(plateau, 0, 0, 4) and column_pack(plateau, 0, 0, -4) == "Erreur !"
    print("Test de la fonction colum_pack : OK")

def test_column_move():
    """
    Test de la fonction column_move
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 6, 
        'tiles': [0, 1, 0, 3, 4, 0, 3, 2, 9, 0, 0, 11, 0, 13, 2, 15]
    }
    #Pour bas
    column_move(plateau, 1, 0)
    assert plateau['tiles'] == [0, 0, 0, 3, 4, 1, 3, 2, 9, 0, 0, 11, 0, 13, 2, 15]
    column_move(plateau, 2, 0)
    assert plateau['tiles'] == [0, 0, 0, 3, 4, 1, 0, 2, 9, 0, 3, 11, 0, 13, 2, 15]
    #Pour haut
    column_move(plateau, 1, 1)
    assert plateau['tiles'] == [0, 1, 0, 3, 4, 0, 0, 2, 9, 13, 3, 11, 0, 0, 2, 15]
    column_move(plateau, 2, 1)
    assert plateau['tiles'] == [0, 1, 0, 3, 4, 0, 3, 2, 9, 13, 2, 11, 0, 0, 0, 15]
    #Pour les valeurs non cohérantes
    assert column_move(plateau, 4, 1) == 'Erreur !' and column_move(plateau, -4, 0) == "Erreur !"
    assert column_move(plateau, 0, 4) == 'Erreur !' and column_move(plateau, 0, -4) == "Erreur !"
    print("Test de la fonction colum_move : OK")

def test_lines_move():
    """
    Test de la fonction lines_moves
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 8, 
        'tiles': [0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0, 13, 0, 15]}
    #Pour droite
    lines_move(plateau, 0)
    assert plateau['tiles'] == [0, 0, 1, 3, 0, 0, 5, 7, 0, 0, 9, 11, 0, 0, 13, 15]
    #Pour gauche
    lines_move(plateau, 1)
    assert plateau['tiles'] == [0, 1, 3, 0, 0, 5, 7, 0, 0, 9, 11, 0, 0, 13, 15, 0]
    #Pour les valeurs non cohérantes
    assert lines_move(plateau, 4) == "Erreur !" and lines_move(plateau, -4) == "Erreur !"
    print("Test de la fonction lines_move : OK")

def test_columns_move():
    """
    Test de la fonction columns_moves
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 6, 
        'tiles': [0, 1, 0, 3, 4, 0, 3, 2, 9, 0, 0, 11, 0, 13, 2, 15]
    }
    #Pour bas
    columns_move(plateau, 0)
    assert plateau['tiles'] == [0, 0, 0, 3, 0, 1, 0, 2, 4, 0, 3, 11, 9, 13, 2, 15]
    #Pour haut
    columns_move(plateau, 1)
    assert plateau['tiles'] == [0, 1, 0, 3, 4, 0, 3, 2, 9, 13, 2, 11, 0, 0, 0, 15]
    #Pour les valeurs non cohérantes
    assert columns_move(plateau, 4) == "Erreur !" and columns_move(plateau, -4) == "Erreur !"
    print("Test de la fonction columns_move : OK")

def test_play_move():
    """
    Test la fonction play_move
    """
    plateau = {
        'n': 4, 
        'nombre_cases_libres': 12, 
        'tiles': [0, 0, 0, 0, 0, 2, 3, 0, 0, 1, 6, 0, 0, 0, 0, 0]
    }
    play_move(plateau, "b")
    assert plateau['tiles'] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 1, 6, 0]
    play_move(plateau, "g")
    assert plateau['tiles'] == [0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 1, 6, 0, 0]
    play_move(plateau, "h")
    assert plateau['tiles'] == [0, 0, 0, 0, 2, 3, 0, 0, 1, 6, 0, 0, 0, 0, 0, 0]
    play_move(plateau, "d")
    assert plateau['tiles'] == [0, 0, 0, 0, 0, 2, 3, 0, 0, 1, 6, 0, 0, 0, 0, 0]
    #Pour les valeurs incohérentes 
    assert play_move(plateau, "x") == "Erreur !"
    print("Test de la fonction play_move : OK")