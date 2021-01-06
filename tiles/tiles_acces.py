def check_indice(plateau, indice):
	"""
	Retourne True si l'indice mis en paramètre correspond à un indice valide du tableau
	(Entre 0 et n - 1)
	"""
	return 0 <= indice <= plateau['n'] - 1

def check_room(plateau, lig, col):
	"""
	Retourne True si (lig, col) sont des indices du tableau
	"""
	return check_indice(plateau, lig) and check_indice(plateau, col)

def get_value(plateau, lig, col):
	"""
	Retourne la valeur d'un plateau à la position lig, col
	"""
	if check_room(plateau, lig, col):
		return plateau['tiles'][lig * plateau['n'] + col]
	return 'Erreur !'

def set_value(plateau, lig, col, val):
	"""
	Affecte une valeur dans le plateau à la position lig, col
	"""
	if check_room(plateau, lig, col) and val >= 0:
		plateau['tiles'][lig * plateau['n'] + col] = val
		plateau['nombre_cases_libres'] -= 1	
	else:
		return 'Erreur !'

def is_room_empty(plateau, lig, col):
	"""
	Affiche True si la case du plateau est vide (= 0), sinon, affiche False
	"""
	if check_room(plateau, lig, col):
		return get_value(plateau, lig, col) == 0
	return 'Erreur !'
