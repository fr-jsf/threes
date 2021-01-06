from os import path
import sys
sys.path.append("../")
from game.play import init_play, create_new_play 
from tiles.tiles_moves import *
from life_cycle.cycle_game import *

def test_init_play(): 
	"""
	Test de la fonction init_play
	"""
	plateau = {
		'n' : 4,
		'nombre_cases_libres' : 16,
		'tiles' : [0 for i in range(16)]
	}
	assert init_play() == plateau
	print("Test de la fonction init_play : OK")

def test_check_indice(): 
	"""
	Test de la fonction check_indice
	"""
	plateau = init_play() 
	assert check_indice(plateau, 0)
	assert check_indice(plateau, 3)
	assert not check_indice(plateau, 4)
	assert not check_indice(plateau, -1)
	print('Test de la fonction check_indice : OK')
	
def test_check_room(): 
	"""
	Test de la fonction check_room
	"""
	plateau = {
		'n' : 4,
		'nombre_cases_libres' : 13,
		'tiles' : [0,2,0,0,0,1,0,0,0,0,0,0,0,2,0,0]
	}
	assert check_room(plateau, 2, 1)
	assert not check_room(plateau, 5, 2)
	assert not check_room(plateau, 2, 5)
	assert not check_room(plateau, -1, 3)
	assert not check_room(plateau, 3, -1)
	assert check_room(plateau, 3, 3)
	print('Test de la fonction check_room : OK')

def test_get_value(): 	
	"""
	Test de la fonction get_value
	"""
	plateau = init_play() 
	assert get_value(plateau, 0, 0) == 0
	assert get_value(plateau, 2, 3) == 0
	assert get_value(plateau, 1, 3) == 0
	assert get_value(plateau, 3, 0) == 0
	assert get_value(plateau, 18, 3) == 'Erreur !'
	print('Test de la fonction get_value : OK')
	
def test_set_value(): 
	"""
	Test de la fonction set_value
	"""
	plateau = init_play() 
	set_value(plateau, 0, 0, 1)
	assert plateau['tiles'][0] == 1 and plateau["nombre_cases_libres"] == 15
	set_value(plateau, 1, 2, 0)
	assert plateau['tiles'][6] == 0 and plateau["nombre_cases_libres"] == 14
	assert set_value(plateau, 18, 3, 1) == 'Erreur !'
	set_value(plateau, 2, 3, 6)
	assert plateau['tiles'][11] == 6 and plateau["nombre_cases_libres"] == 13
	set_value(plateau, 3, 3, 6)
	assert plateau['tiles'][15] == 6 and plateau["nombre_cases_libres"] == 12
	print('Test de la fonction set_value : OK')
	
	
def test_is_room_empty() : 
	"""
	Test la fonction is_room_empty
	"""
	plateau = {
		'n' : 4,
		'nombre_cases_libres' : 13,
		'tiles' : [0,2,0,0,0,1,0,0,0,0,0,0,0,2,0,0]
	}	
	assert not is_room_empty(plateau, 0, 1)
	assert is_room_empty(plateau, 0, 3)
	assert is_room_empty(plateau, 13, 1) == 'Erreur !'
	assert is_room_empty(plateau, 3, 2)
	print("Test de la fonction is_room_empty : OK")

def test_get_nb_empty_rooms():
	"""
	Test la fonction get_nb_empty_rooms
	"""
	plateau = {
		'n' : 4,
		'nombre_cases_libres' : 16,
		'tiles' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	}
	assert get_nb_empty_rooms(plateau) == 16
	plateau['tiles'] = [3,0,0,3,0,0,1,0,0,0,0,4,0,0,0,2]
	assert get_nb_empty_rooms(plateau) == 11 and plateau['nombre_cases_libres'] == 11
	plateau['tiles'] = [3,0,0,3,0,1,1,0,0,0,0,4,0,3,0,2]
	assert get_nb_empty_rooms(plateau) == 9 and plateau['nombre_cases_libres'] == 9
	plateau['tiles'] = [3,1,1,3,1,1,1,1,1,2,3,1,1,3,2,2]
	assert get_nb_empty_rooms(plateau) == 0 and plateau['nombre_cases_libres'] == 0
	print('Test de la fonction get_nb_empty_rooms : OK')

def test_is_game_over() : 
	"""
	Test de la fonction is_game_over
	"""
	plateau = init_play()
	assert not is_game_over(plateau)
	plateau["tiles"] = [1,0,2,1,2,1,2,1,2,1,2,1,1,2,1,2]
	assert not is_game_over(plateau)	
	plateau["tiles"] = [1 for i in range(16)] 
	assert is_game_over(plateau)
	print('Test de la fonction is_game_over : OK')
	
	
def test_get_score() : 
	"""
	Test de la fonction get_score
	"""
	plateau = init_play()
	assert get_score(plateau) == 0
	plateau["tiles"] = [1,0,2,1,2,1,2,1,2,1,2,1,1,2,1,2]
	assert get_score(plateau) == 22
	plateau["tiles"] = [1,0,2,1,2,1,2,-1,2,1,2,1,1,2,1,2]
	assert get_score(plateau) == 20
	print("Test de la fonction get_score : OK")
