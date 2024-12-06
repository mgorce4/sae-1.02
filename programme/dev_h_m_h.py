# importation des modules
import os
import time

def devinette_player_vs_machine_hardcore(pJoueur1):
    """
    fonction jeu devinette joueur contre machine niveau hardcore
    pas de paramètre d'entrée
    sortie: pseudo du joueur et son score
    """
    # type des variables
    rslt : list[str]
    rslt = []
    n_essai_max_machine : int
    n_essai_machine : int
    born_min : int
    born_max : int
    joueur_1 : str
    joueur_2 : str
    nombre_mystere : int
    tableau : list[int]
    i : int
    c : int
    moy : int
    reaction : str
    boolean : int

    # attribution des valeurs aux variables 
    n_essai_max_machine = 7
    born_min = 1
    born_max = 20
    boolean = 0
    n_essai_machine = 0

    # affichage des règle
    print("règles du jeu")
    print('\r')
    print("Le joueur 1 (humain) choisit un nombre entre ",born_min," et ",born_max,".")
    print("le joueur 2 (machine) doit deviner le nombre choisi par le joueur 1 sans dépasser ",n_essai_max_machine," essai(s).")
    print("À chaque essai du joueur 2, le joueur 1 doit émettre une réponse parmi les 3 suivantes :")
    print("")
    print("+       -       =")
    print("")
    print("+ Si la réponse du joueur 2 est trop petit.")
    print("- Si la réponse du joueur 2 est trop grand.")
    print("= Si le joueur 2 a trouvé le nombre du joueur 1.")
    print("")
    print("Si le joueur 2 trouve le nombre auquel pense le joueur 1 sans dépasser 5 hypothèses, alors celui-ci gagne.")
    print("Sinon, c'est le joueur 1 qui gagne.")   

    # atribution des roles
    joueur_1 = pJoueur1
    time.sleep(1)
    joueur_2 = "Bot"
    print ("pseudo du joueur 2 : Bot")
    time.sleep(1)

    # joueur 1 humain désigne le nombre mystère
    print (joueur_1)
    print("Choisissez un nombre entre ",born_min," et ",born_max," : ")
    nombre_mystere = int(input("Votre choix : "))
    while nombre_mystere < born_min or nombre_mystere > born_max:
        nombre_mystere = int(input("Choisissez un nombre entre ",born_min," et ",born_max," : "))
    os.system("cls")

    # création de l'intervalle initial
    time.sleep(1)
    tableau = []
    for i in range(born_min, born_max + 1):
        tableau.append(i)
    print("\x1b[38;5;200m")
    print(tableau)
    print("\x1b[38;5;7m")

    # tant que le nombre d'essais de la machine n'a pas atteint la limite
    while n_essai_machine != n_essai_max_machine:
        n_essai_machine = n_essai_machine + 1
        # la mlachine choisit la valeur moyenne de l'intervalle
        moy = int((tableau[0] + tableau[0] + len(tableau) - 1) / 2)
        time.sleep(1)
        print ("choix de ",joueur_2," : ",moy)
        time.sleep(1)
        if nombre_mystere < moy:
            if n_essai_machine == n_essai_max_machine:
                break
            else:
                # réponse du joueur 1
                print (joueur_1)
                reaction =  input("votre réponse : ")
                while reaction != "-":
                    reaction =  input("votre réponse : ")
                for loop in range (len(tableau) + tableau[0] - moy):
                    del tableau[moy - tableau[0]]
                print("\x1b[38;5;200m")
                print(tableau)
                print("\x1b[38;5;7m")            
        elif nombre_mystere > moy:
            if n_essai_machine == n_essai_max_machine:
                break
            else:
                # réponse du joueur 1
                print (joueur_1)
                reaction =  input("votre réponse : ")
                while reaction != "+":
                    reaction =  input("votre réponse : ")
                c = 0
                while tableau[c] != moy:
                    c = c + 1
                for loop in range (c + 1):
                    del tableau[0]
                print("\x1b[38;5;200m")
                print(tableau)
                print("\x1b[38;5;7m") 
        else:
            # victoire de joueur 2
            boolean = 1
            print(joueur_1)
            reaction = input("Votre réponse : ")
            while reaction != "=":
                reaction = input("Votre réponse : ")
            print (joueur_2," a gagné en ",n_essai_machine," essai(s).")
            print (joueur_1," a perdu.")
            rslt.append(pJoueur1)
            rslt.append(str(0))
            return rslt
    if boolean == 0:
        # victoire de joueur 1
        print(joueur_1," a gagné.")
        print(joueur_2," a perdu en ",n_essai_machine," essai(s).")
        rslt.append(pJoueur1)
        rslt.append(str(1))
        return rslt