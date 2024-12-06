def devinette_player_vs_player(pJoueur1: str, pJoueur2 :str):
    """
    fonction jeu devinette joueur contre joueur
    pas de paramètre d'entrée
    sortie: pseudo du joueur et son score
    """

    # importation des modules
    import os

    # affichage des règles
    print("REGLES DU JEU")
    print('\r')
    print("Le joueur 2 fixe un intervalle entre 1 et une limite a decider")
    print("")
    print("Le joueur 1 choisit un nombre entre 1 et cette limite")
    print("")
    print("le joueur 2 doit deviner le nombre choisi par le joueur 1 sans depasser 5 tentatives")
    print("")
    print("A chaque hypothese emise par le joueur 2, le joueur 1 doit emettre une reponse parmi les 3 suivantes :")
    print("")
    print("")
    print("+       -       =")
    print("")
    print("")
    print("+ Si le nombre du joueur 2 est trop petit")
    print("")
    print("- Si le nombre du joueur 2 est trop grand")
    print("")
    print("= Si le joueur 2 a trouve le nombre du joueur 1")
    print("")
    print("")
    print("Si le joueur 2 trouve le nombre auquel pense le joueur 1 sans depasser 5 hypotheses, alors celui-ci gagne")
    print("")
    print("Sinon, c'est le joueur 1 qui gagne")

    # type des variables
    rslt : list[str]
    rslt = []
    joueur_2 : str
    boundary_max : int
    number_player1 : int
    limit : int
    ntry : int
    interval : list
    hypothesis : int
    response : str

    # attribution des valeurs de la constante limit et de la variable ntry
    limit = 5
    ntry = 0

    # choix des pseudo et attribution des roles
    joueur_1 = pJoueur1
    joueur_2 = pJoueur2

    # choix de la taille de l'intervalle et controle 
    boundary_max = int(input("Le joueur 2 doit entrer la taille de l'intervalle : "))
    while boundary_max < 1 or boundary_max % 1 != 0:
        boundary_max = int(input(" Le joueur 2 doit entrer la taille de l'intervalle")) 
    
    # le joueur 1 pense a un nombre
    number_player1 = int(input("Le joueur 1 doit choisir un nombre dans l'intervalle : "))
    while number_player1 < 1 or number_player1 > boundary_max or number_player1 % 1 != 0:
        number_player1 = int(input("Le joueur 1 doit choisir un nombre dans l'intervalle : "))
    os.system("cls")
   




    





    # création de l'intervalle
    interval : list[int]
    interval = []
    for i in range(1, boundary_max + 1):
        interval.append(i)
    print("\x1b[38;5;200m")
    print(interval)
    print("\x1b[38;5;7m")

    # instauration du nombre d'essai max du joueur 2
    while ntry != limit:
        ntry = ntry + 1

        # emmission de l'hypothèse par le joueur 2 et controle
        hypothesis = int(input("Le joueur 2 doit emettre une hypothese : "))
        while hypothesis < interval[0] or hypothesis > interval[0] + len (interval) - 1 or hypothesis % 1 != 0:
            hypothesis = int(input("Le joueur 2 doit emettre une hypothese : "))
        
        # réponse du joueur 1 et contrôle
        if hypothesis > number_player1:
            response = input("Le joueur 1 doit emettre une réponse : ")
            while response != "-":
                response = input("Le joueur 1 doit dire la vérité : ")
            print ("C'est moins !")

            # affichage du nouvel intervalle 
            for loop in range (len(interval) + interval[0] - 1 - hypothesis + 1):
                del interval[hypothesis - interval[0]]
            print("\x1b[38;5;200m")
            print(interval)
            print("\x1b[38;5;7m")

        # équivalent des deux dernières parties commentées mais dans le cas contraire
        elif hypothesis < number_player1:
            response = input("Le joueur 1 doit emettre une réponse : ")
            while response != "+":
                response = input("Le joueur 1 doit dire la vérité : ")
            print ("C'est plus !")
            i = 0
            while interval[i] != hypothesis:
                i = i + 1
            for loop in range (i+1):
                del interval[0]
            print("\x1b[38;5;200m")
            print(interval)
            print("\x1b[38;5;7m")

        # on sort de la boucle si le joueur 2 trouve le nombre    
        else:
            break

    








    # Détermination du gagnant    
    if ntry != limit :
        response = input("Le joueur 1 doit emettre une réponse : ")
        while response != "=":
            response = input("Le joueur 1 doit dire la vérité : ")
        print (joueur_2," a gagne ! ",joueur_2," a trouve ",hypothesis," en ",(ntry)," essai(s)")
        rslt.append(pJoueur2)
        rslt.append(str(1))
        return rslt
    elif ntry == limit and hypothesis == number_player1:
        response = input("Le joueur 1 doit emettre une réponse : ")
        while response != "=":
            response = input("Le joueur 1 doit dire la vérité : ")
        print (joueur_2," a gagne ! ",joueur_2," a trouve ",hypothesis," en ",(ntry)," essai(s)")
        rslt.append(pJoueur2)
        rslt.append(str(1))
        return rslt
    elif ntry == limit and hypothesis != number_player1:
        print (joueur_2," a dépassé les 5 tentatives autorisées. Le nombre était ",number_player1)
        print (joueur_1," a gagne !")
        rslt.append(pJoueur1)
        rslt.append(str(1))
        return rslt