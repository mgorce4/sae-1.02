# importation des modules
from random import *
import random 
import time

def allumettes_player_vs_machine_medium(pJoueur1 : str):
    """
    fonction jeu allumettes joueur contre machine difficulté moyen
    pas de paramètre d'entrée
    sortie : pseudo du joueur et son score 
    """
    # type des variables
    rslt: list[str]
    rslt = []
    turn : int
    machine_player : str
    human_player : str
    choix : str
    joueur_1 : str
    joueur_2 : str
    m_taken : int
    p : float
    response : int

    # attribution des valeurs aux variables
    machine_player = "Bot"
    turn = 0
    m_taken = 0

    # REGLES
    print("règles")
    print("")
    print("On dispose d'un tas de 20 allumettes.")
    print("Chaque joueur à tour de rôle peut en prélever 1, 2 ou 3.")
    print("Le perdant est celui qui prend la dernière allumette.")
    print("Le joueur 1 commence.")
    print("")
    print("")
    print("")

    # qui sera le joueur 1
    human_player = pJoueur1
    print ("Choisir le joueur 1 ")
    print (human_player," -> a")
    print (machine_player," -> b")
    choix = input("votre choix : ")

    # vérification dénomination du joueur 1
    while (choix != "a") and (choix != "b"):
        choix = input("-> votre choix : ")

    # attribution des rôles
    if choix == "a":
        joueur_1 = human_player
        joueur_2 = machine_player
    else:
        joueur_1 = machine_player
        joueur_2 = human_player

    # representation du paquet d'allumettes original
    for i in range (20 - m_taken):
        print("\x1b[38;5;196m.")
        print("\x1b[38;5;190m|")
        print("\x1b[38;5;7m")
    print ((20 - m_taken), " allumette(s) restante(s)")

    # tant que toutes les allumettes n'ont pas été prises
    while m_taken != 20:
        # tour du joueur 1 (mais lequel ?)
        if turn % 2 == 0:
            # joueur 1 humain
            if choix == "a":
                print (joueur_1)
                response = int(input("votre choix : "))
                # controle réponse joueur 1 humain
                while (m_taken + response > 20) or (response < 1) or (response > 3):
                    response = int(input("votre choix : "))

                # representation du paquet d'allumettes après le passage du joueur 1 humain
                m_taken = m_taken + response                
                for i in range (20 - m_taken):
                    print("\x1b[38;5;196m.")
                    print("\x1b[38;5;190m|")
                    print("\x1b[38;5;7m")
                print ((20 - m_taken), " allumette(s) restante(s)")

                # condition de défaite du joueur 1 humain
                if m_taken == 20:
                    print(joueur_1, " a perdu")
                    rslt.append(pJoueur1)
                    rslt.append(str(0))
                    return rslt
            else:
                # tour du joueur 1 machine 
                time.sleep(1)
                print(joueur_1," est en train de jouer")
                time.sleep(1)
                p = random.random()
                if p < 0.66:
                    if (20 - m_taken) % 4 == 0:
                        response = 3
                    elif (20 - m_taken) % 4 == 1:
                        if (20 - m_taken) == 1:
                            response = 1
                        else:
                            liste = [1,2,3]
                            response = choice(liste)
                    elif (20 - m_taken) % 4 == 2:
                        response = 1
                    else:
                        response = 2
                else:
                    if (20 - m_taken) % 4 == 0:
                        liste = [1,2]
                        response = choice(liste)
                    elif (20 - m_taken) % 4 == 1:
                        if (20 - m_taken) == 1:
                            response = 1
                        else:
                            liste = [1,2,3]
                            response = choice(liste)
                    elif (20 - m_taken) % 4 == 2:
                        if (20 - m_taken) == 2:
                            response = 2
                        else:
                            liste = [2,3]
                            response = choice(liste)
                    else:
                        liste = [1,3]
                        response = choice(liste)
                print("choix de ",joueur_1," : ",response)

                # representation du paquet d'allumettes après le passage du joueur 1 machine
                m_taken = m_taken + response                
                for i in range (20 - m_taken):
                    print("\x1b[38;5;196m.")
                    print("\x1b[38;5;190m|")
                    print("\x1b[38;5;7m")
                print ((20 - m_taken), " allumette(s) restante(s)")

                # condition de défaite du joueur 1 machine
                if m_taken == 20:
                    print(joueur_1, " a perdu")
                    rslt.append(pJoueur1)
                    rslt.append(str(1))
                    return rslt

        # tour du joueur 2 (mais lequel ?)        
        else:
            # joueur 2 machine
            if choix == "a":
                time.sleep(1)
                print(joueur_2," est en train de jouer")
                time.sleep(1)
                p = random.random()
                if p < 0.66:
                    if (20 - m_taken) % 4 == 0:
                        response = 3
                    elif (20 - m_taken) % 4 == 1:
                        if (20 - m_taken) == 1:
                            response = 1
                        else:
                            liste = [1,2,3]
                            response = choice(liste)
                    elif (20 - m_taken) % 4 == 2:
                        response = 1
                    else:
                        response = 2
                else:
                    if (20 - m_taken) % 4 == 0:
                        liste = [1,2]
                        response = choice(liste)
                    elif (20 - m_taken) % 4 == 1:
                        if (20 - m_taken) == 1:
                            response = 1
                        else:
                            liste = [1,2,3]
                            response = choice(liste)
                    elif (20 - m_taken) % 4 == 2:
                        if (20 - m_taken) == 2:
                            response = 2
                        else:
                            liste = [2,3]
                            response = choice(liste)
                    else:
                        liste = [1,3]
                        response = choice(liste)
                print("choix de ",joueur_2," : ",response)

                # representation du paquet d'allumettes après le passage du joueur 2 machine
                m_taken = m_taken + response
                for i in range (20 - m_taken):
                    print("\x1b[38;5;196m.")
                    print("\x1b[38;5;190m|")
                    print("\x1b[38;5;7m")
                print ((20 - m_taken), " allumette(s) restante(s)")

                # condition de défaite du joueur 2 machine
                if m_taken == 20:
                    print(joueur_2, " a perdu")
                    rslt.append(pJoueur1)
                    rslt.append(1)
                    return rslt
            else:
                # joueur 2 humain
                print (joueur_2)
                response = int(input("votre choix : "))
                # controle réponse joueur 2 humain
                while (m_taken + response > 20) or (response < 1) or (response > 3):
                    response = int(input("votre choix : "))

                # representation du paquet d'allumettes après le passage du joueur 2 humain
                m_taken = m_taken + response
                for i in range (20 - m_taken):
                    print("\x1b[38;5;196m.")
                    print("\x1b[38;5;190m|")
                    print("\x1b[38;5;7m")
                print ((20 - m_taken), " allumette(s) restante(s)")
                if m_taken == 20:
                    print(joueur_2, " a perdu")
                    rslt.append(pJoueur1)
                    rslt.append(str(0))
        # le tour est désormais à l'autre joueur
        turn = turn + 1