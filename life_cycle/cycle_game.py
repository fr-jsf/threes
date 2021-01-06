import copy

def is_game_over(plateau):
	"""
	Retourne True si la partie est fini, sinon, affiche False
	"""
	from tiles.tiles_moves import get_nb_empty_rooms, columns_move, lines_move
	check = copy.deepcopy(plateau)
	columns_move(check, 0), columns_move(check, 1), lines_move(check, 0), lines_move(check, 1)
	return get_nb_empty_rooms(plateau) == 0 and get_nb_empty_rooms(check) == 0 and check == plateau

def get_score(plateau):
	"""
	Fait la somme de l'ensemble des tuiles du plateau
	"""
	somme = 0
	for i in range(0, len(plateau['tiles'])):
		somme += plateau['tiles'][i]
	return somme
