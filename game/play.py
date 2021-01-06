import sys
from os import path
sys.path.append(path.abspath('../'))
from life_cycle.cycle_game import *
from tiles.tiles_moves import *

def init_play():
	"""
	Retourne un plateau correspondant à une nouvelle partie
	Une nouvelle partie est un dictionnaire avec les clefs et valeurs suivantes :
		- 'n' ; vaut 4
		- 'nb_cases_libres' : au départ, vaut n*n donc 16
		- 'tiles' : tableau de taille n*n cases initialisées à 0
	"""
	plateau = {
		'n' : 4,
		'nombre_cases_libres' : 16,
		'tiles' : [0 for i in range(16)]
	}
	return plateau

def create_new_play():
    """
    Créer et retourne une nouvelle partie
    """
    partie = {}
    partie['plateau'] = init_play()
    partie['next-tile'] = get_next_alea_tiles(partie["plateau"], "init")
    put_next_tiles(partie["plateau"], partie["next-tile"])
    partie['score'] = get_score(partie["plateau"])
    return partie
