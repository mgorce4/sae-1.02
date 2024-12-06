def allumettes_player_vs_player(pJoueur1 : str, pJoueur2 : str):
    """
    fonction jeu allumettes joueur contre joueur
    pas de paramètre d'entrée
    sortie : pseudo du joueur et son score
    """
    # regles

    print("regles")
    print("")
    print("On dispose d'un tas de 20 allumettes.")
    print("Chaque joueur à tour de rôle peut en prélever 1, 2 ou 3.")
    print("Le perdant est celui qui prend la dernière allumette.")
    print("Le joueur 1 commence.")
    print("")
    print("")
    print("")



    # type des variables
    rslt : list[str]
    rslt =[]
    m_taken : int

    turn : int

    response : int

    joueur_1 : str

    joueur_2 : str



    # attribution aux variables de leurs valeurs

    m_taken = 0

    turn = 0

    joueur_1 = pJoueur1

    joueur_2 = pJoueur2



    # representation du paquet d'allumettes original

    for i in range (20 - m_taken):

        print("\x1b[38;5;196m.")

        print("\x1b[38;5;190m|")

        print("\x1b[38;5;7m")

    print ((20 - m_taken), " allumette(s) restante(s)")



    # tant que les 20 allumettes n'ont pas été piochées

    while m_taken != 20:



        # tour du joueur 1

        if turn % 2 == 0:

            print (joueur_1)

            response = int(input("votre choix : "))

            # controle de la réponse du joueur 1

            while (m_taken + response > 20) or (response < 1) or (response > 3):

                response = int(input("votre choix : "))

            m_taken = m_taken + response

            # representation du paquet d'allumettes après le passage du joueur 1
            
            for i in range (20 - m_taken):

                print("\x1b[38;5;196m.")

                print("\x1b[38;5;190m|")

                print("\x1b[38;5;7m")

            print ((20 - m_taken), " allumette(s) restante(s)")

            if m_taken == 20:

                print(joueur_1, " a perdu")
                rslt.append(pJoueur2)
                rslt.append(str(1))
                return rslt

        # tour du joueur 2

        else:

            print (joueur_2)

            response = int(input("votre choix : "))

            # controle de la réponse du joueur 2

            while (m_taken + response > 20) or (response < 1) or (response > 3):

                response = int(input("votre choix : "))

            m_taken = m_taken + response



            # representation du paquet d'allumettes après le passage du joueur 2

            for i in range (20 - m_taken):

                print("\x1b[38;5;196m.")

                print("\x1b[38;5;190m|")

                print("\x1b[38;5;7m")

            print ((20 - m_taken), " allumette(s) restante(s)")

            if m_taken == 20:

                print(joueur_2, " a perdu")
                rslt.append(pJoueur1)
                rslt.append(str(1))
                return rslt         



        # Le tour est désormais à l'autre joueur

        turn = turn + 1