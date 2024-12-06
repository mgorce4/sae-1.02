#jeu du morpion

import random

def jeu_du_morpion_humain_humain(pJoueur1 : str , pJoueur2 : str) : #-> list[str] 
    """
    fonction du jeu du morpion le joueur sera définit par 1 ou 2 et changera entre chaque tour de manière
    entrée: pseudos des joueurs
    sortie: nom du gagnant et le nombre de points à lui ajouter
    """
    rslt : list[str]
    rslt =[]
    #regles
    print("\nRègles du jeu:\nPour jouer une partie de Morpion, chaque joueur à tour de rôle,\nplace un rond ou une croix dans une des cases de la grille.\n\nLe but du jeu est d'aligner trois croix ou ronds sur une même ligne.\n")

    joueur=1#on commence avec le joueur 1(initialisation de la partie )
    print("Le joueur 1 jouera les X(croix) et le joueur 2 jouera les O(ronds)")
    grille=[" "," "," "," "," "," "," "," "," "]#notre liste étant la grille du morpion
    afficher_la_grille(grille)

    gagne=0 #on initialise gagne à 0
    while gagne==0:
        tour_joueur_joueur(grille,joueur)
        if gagnant(grille): #si la partie est remportée faire
            print("Le joueur "+str(joueur)+" remporte la partie")
            gagne=1

            if joueur == 1: #si le gagnant est le premier joueur, lui ajouter un point
                rslt.append(pJoueur1)
                rslt.append(str(1))
            else :
                if joueur == 2: #si le gagnant est le deuxième joueur, lui ajouter un point
                    rslt.append(pJoueur2)
                    rslt.append(str(1))

            return rslt#retour au menu pour tableau des points
        else:
            if match_nul(grille): #si il y a match nul
                print("Plus de place ! Match nul !")
                gagne=1

                rslt.append(pJoueur1)
                rslt.append(str(0))
                return rslt #retour au menu pour tableau des points
            
        #changement de joueurs    
        if joueur==1:
            joueur=2
        else:
            joueur=1

def jeu_du_morpion_humain_machine_easy(pJoueur1: str):
    """
    fonction du jeu de morpion entre un humain et une "machine" le joueur sera définit par joueur 1 et la machine par joueur 2 ce mode de jeu sera compté comme facile la machine posera ses pions au hasard 
    entrée: pseudo du joueur
    sortie: pseudo du joeur et s'il a gagné ou non sa partie 
    """
    rslt : list[str]
    rslt =[]
    #regles
    print("\nRègles du jeu:\nPour jouer une partie de Morpion, chaque joueur à tour de rôle,\nplace un rond ou une croix dans une des cases de la grille.\n\nLe but du jeu est d'aligner trois croix ou ronds sur une même ligne.\n")

    joueur=1#on commence avec le joueur 1(initialisation de la partie )
    print("Le joueur 1 jouera les X(croix) et le joueur 2 jouera les O(ronds)")
    grille=[" "," "," "," "," "," "," "," "," "]#notre liste étant la grille du morpion
    afficher_la_grille(grille)

    gagne=0 #on initialise gagne à 0
    while gagne==0:
        tour_joueur_bot_easy(grille,joueur)
        if gagnant(grille):
            print("Le joueur "+str(joueur)+" remporte la partie")
            gagne=1

            if joueur == 1: #si le gagnant est le premier joueur, lui ajouter un point
                rslt.append(pJoueur1)
                rslt.append(str(1))
            else :
                if joueur == 2: #si le gagnant est le deuxième joueur, lui ajouter un point
                    rslt.append(pJoueur1)
                    rslt.append(str(0))

            return rslt#retour au menu pour tableau des points
        else:
            if match_nul(grille): #si il y a match nul
                print("Plus de place ! Match nul !")
                gagne=1

                rslt.append(pJoueur1)
                rslt.append(str(0))
                return rslt #retour au menu pour tableau des points
            
        #changement de joueurs    
        if joueur==1:
            joueur=2
        else:
            joueur=1


def jeu_du_morpion_machine_machine():
    """
    procédure du jeu de morpion entre deux machines
    entrée: rien
    sortie: rien
    """
    #regles
    print("\nRègles du jeu:\nPour jouer une partie de Morpion, chaque joueur à tour de rôle,\nplace un rond ou une croix dans une des cases de la grille.\n\nLe but du jeu est d'aligner trois croix ou ronds sur une même ligne.\n")

    joueur=1#on commence avec le joueur 1(initialisation de la partie )
    print("Le joueur 1 jouera les X(croix) et le joueur 2 jouera les O(ronds)")
    grille=[" "," "," "," "," "," "," "," "," "]#notre liste étant la grille du morpion
    afficher_la_grille(grille)

    gagne=0 #on initialise gagne à 0
    while gagne==0:
        tour_bot_bot(grille, joueur)
        if gagnant(grille):
            print("Le bot "+str(joueur)+" remporte la partie")
            gagne=1
            
        else:
            if match_nul(grille): #si il y a match nul
                print("Plus de place ! Match nul !")
                gagne=1
        
        #changement de joueurs    
        if joueur==1:
            joueur=2
        else:
            joueur=1


def afficher_la_grille(grille):
    """
    affichage de la grille de jeu séparée avec ses hauteurs avec les nombres pour les lignes et colonnes allant de 0 à 2
    recois: la liste
    retourne : rien (procédure)
    """
    print("     0/  1/  2")
    print("   _____________") #séparateur
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')#afficher les trois premières listes pour la grille avec un | avant en guise de séparateur
    print(" |")
    print("   _____________")#séparateur
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')#afficher les trois secondes listes pour la grille avec un | avant en guise de séparateur
    print(" |")
    print("   _____________") #séparateur
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')#afficher les trois dernières listes pour la grille avec un | avant en guise de séparateur
    print(" |") #dernier séparateur
    print("   _____________") #séparateur


def tour_joueur_joueur(grille, joueur):
    """
    définition de ce qu'est le tour d'un joueur et son fonctionnement (fonctionnant dans la boucle while)
    entrée : grille et joueur
    sortie : rien(procédure)
    """
    print("C'est le tour du joueur "+str(joueur)) #annoncement du joueur
    colonne=int(input("Entrez le numero de la colonne : ")) #choix de la colonne par le joueur
    while (colonne<0 or colonne>2):#prise en compte de toutes les possibilités
        colonne=int(input("Entrez le numero de la colonne : ")) 
    ligne=int(input("Entrez le numero de la ligne : "))#choix de la ligne par le joueur
    while (ligne<0 or ligne>2):#prise en compte de toutes les possibilités d'input
        ligne=int(input("Entrez le numero de la ligne : "))
    print("\nVous avez joué la case",colonne,ligne) #annonce du jeu fait par le joueur
    while grille[int(colonne)+int(ligne)*3]!=" ": #si la case de la grille est déjà prise 
        afficher_la_grille(grille)#reimprimer la grille
        print("Cette case est deja jouée ! Saisissez une autre case svp !") #annonce du problème
        colonne=int(input("Entrez le numero de la colonne : ")) #le programmme pour rentrer une case est relancé
        if (colonne<0 or colonne>2):
            colonne=int(input("Entrez le numero de la colonne : "))
        ligne=int(input("Entrez le numero de la ligne : "))
        if (ligne<0 or ligne>2):
            ligne=int(input("Entrez le numero de la ligne : "))
        print("Vous avez joué la case","+",colonne,"+","+",ligne,"+")

    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X" #l'input dans le tableau dépend du joueur  
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_la_grille(grille)

def tour_joueur_bot_easy(grille, joueur):
    """
    procédure définissant les tours joueur vs bot en mode facile et son fonctionnement
    entrée: grille et joueur
    rien:(procédure)
    """
    print("C'est le tour du joueur "+str(joueur))
    if (joueur==1):
        colonne=int(input("Entrez le numero de la colonne : ")) #choix de la colonne par le joueur
        while (colonne<0 or colonne>2):#prise en compte de toutes les possibilités
            colonne=int(input("Entrez le numero de la colonne : ")) 
        ligne=int(input("Entrez le numero de la ligne : "))#choix de la ligne par le joueur
        while (ligne<0 or ligne>2):#prise en compte de toutes les possibilités d'input
            ligne=int(input("Entrez le numero de la ligne : "))
        print("\nVous avez joué la case","+",colonne,"+",ligne,"+") #annonce du jeu fait par le joueur
        while grille[int(colonne)+int(ligne)*3]!=" ": #si la case de la grille est déjà prise 
            afficher_la_grille(grille)#reimprimer la grille
            print("Cette case est deja jouée ! Saisissez une autre case svp !") #annonce du problème
            colonne=int(input("Entrez le numero de la colonne : ")) #le programmme pour rentrer une case est relancé
            if (colonne<0 or colonne>2):
                colonne=int(input("Entrez le numero de la colonne : "))
            ligne=int(input("Entrez le numero de la ligne : "))
            if (ligne<0 or ligne>2):
                ligne=int(input("Entrez le numero de la ligne : "))
            print("Vous avez joué la case","+",colonne,"+","+",ligne,"+")
        
        grille[int(colonne)+int(ligne)*3]="X"
        afficher_la_grille(grille)

    if (joueur ==2):
        colonne = int(random.randint(0,2)) #le bot choisi un nombre pour la colonne au hasard entre 0 et 2 compris
        ligne = int(random.randint(0,2)) #le bot choisi un nombre pour la ligne au hasard entre 0 et 2 compris
        while grille[int(colonne)+int(ligne)*3]!=" ": #si la case est déjà prise il en choisi une nouvelle
            colonne = int(random.randint(0,2))
            ligne = int(random.randint(0,2))
        grille[int(colonne)+int(ligne)*3]="O" #la case choisie est remplie avec un O
        afficher_la_grille(grille) 
        print ("bot a joué la case","+",colonne,"+","+",ligne,"+")

def tour_bot_bot(grille, joueur):
    """
    procédure définissant les tours joueur vs bot en mode facile et son fonctionnement
    entrée: grille et joueur
    rien:(procédure)
    """
    print("C'est le tour du joueur "+str(joueur))
    if (joueur==1):
        colonne = int(random.randint(0,2)) #le bot choisi un nombre pour la colonne au hasard entre 0 et 2 compris
        ligne = int(random.randint(0,2)) #le bot choisi un nombre pour la ligne au hasard entre 0 et 2 compris
        while grille[int(colonne)+int(ligne)*3]!=" ":
            colonne = int(random.randint(0,2))
            ligne = int(random.randint(0,2))
        grille[int(colonne)+int(ligne)*3]="X" #la case choisie est remplie avec un X
        afficher_la_grille(grille)
        print ("bot 1 a joué la case","+",colonne,"+","+",ligne,"+")

    if (joueur ==2):
        colonne = int(random.randint(0,2)) #le bot choisi un nombre pour la colonne au hasard entre 0 et 2 compris
        ligne = int(random.randint(0,2)) #le bot choisi un nombre pour la ligne au hasard entre 0 et 2 compris
        while grille[int(colonne)+int(ligne)*3]!=" ": #si la case est déjà prise il en choisi une nouvelle
            colonne = int(random.randint(0,2))
            ligne = int(random.randint(0,2))
        grille[int(colonne)+int(ligne)*3]="O" #la case choisie est remplie avec un O
        afficher_la_grille(grille)
        print ("bot 2 a joué la case","+",colonne,"+","+",ligne,"+")

def gagnant(grille):
    """
    fonction pour déterminer les résultats gagnants avec chaque possibilité 
    entrée : grille
    sortie : 1 pour indiquer la fin de partie
    """
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1 #retourne 1 pour la fin de partie
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1

def match_nul(grille):
    """
    fonction déterminant un match nul pour fermer la boucle du programme du morpion
    entrée: grille(pour l'analyser)
    sortie: 1 pour indiquer la fin de partie
    """
    for i in range(9):
        if grille[i]==" ": # bien vérifier que la dernière case est pleine comme ça pas de problème
            return 0
    return 1