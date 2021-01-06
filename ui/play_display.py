from termcolor import colored

def full_display(plateau):
    """
    Affiche le plateau en couleurs
    """
    couleurs = {
        0 : {0 : ["white", "on_white"], 1 : ["white", "on_blue"], 2 : ["white", "on_red"]},
        1 : ["grey", "on_white"],
        "ligne" : [colored, " ", "grey", "on_grey"]
    }
    trait = couleurs["ligne"][0](couleurs["ligne"][1],couleurs["ligne"][2],couleurs["ligne"][3])
    for i in range(0,16,4):
        wspace = ""
        ligne = ""
        for j in range(i, i + 4):
            if couleurs[plateau["tiles"][j] >= 3] == couleurs[1]:
                wspace += str(trait + couleurs["ligne"][0](" ".center(7), couleurs[1][0], couleurs[1][1]) + trait)
                ligne += str(trait + couleurs["ligne"][0](str(plateau["tiles"][j]).center(7), couleurs[1][0], couleurs[1][1])+ trait)
            else:
                wspace += str(trait + couleurs["ligne"][0](" ".center(7), couleurs[0][plateau["tiles"][j]][0], couleurs[0][plateau["tiles"][j]][1]) + trait)
                ligne += str(trait + couleurs["ligne"][0](str(plateau["tiles"][j]).center(7), couleurs[0][plateau["tiles"][j]][0], couleurs[0][plateau["tiles"][j]][1])+ trait)

        print(trait * 36 + '\n' + wspace +'\n' + wspace + '\n' + ligne + '\n' + wspace)
    print(trait * 36)
