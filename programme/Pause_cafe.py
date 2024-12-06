import morpion
import pickle
import scores
import devinette
import dev_h_m_e
import dev_h_m_m
import dev_h_m_h
import all_h_m_e
import all_h_m_m
import all_h_m_h
import allumettes

#choix présent sur le menu
menu_options = {
    1: 'devinettes',
    2: 'allumettes',
    3: 'morpion',
    4: 'scores',
    5: 'exit'
}


#imprimer le menu
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def choix_du_mode_de_jeu():
    """
    fonction pour choisir le du mode de jeu (humain contre humain, humain contre machine ou machine contre machine)
    entrée: rien
    sortie: str 
    """
    choix : str
    final_choice : int

    choix = ""
    final_choice = 0
    
    print(r""" __  __  _____  ____  ____    ____  ____     ____  ____  __  __ 
(  \/  )(  _  )(  _ \( ___)  (  _ \( ___)   (_  _)( ___)(  )(  )
 )    (  )(_)(  )(_) ))__)    )(_) ))__)   .-_)(   )__)  )(__)( 
(_/\/\_)(_____)(____/(____)  (____/(____)  \____) (____)(______)""")
    while (choix != '4'):
        print("----------------------------")
        print("|1- Humain vs humain       |")
        print("|2- Humain vs machine      |")
        print("|3- Machine contre machine |")
        print("----------------------------\n")
        choix = input("quel est est votre choix? : ")
        if (choix =="1"):
            final_choice = 1
            return final_choice
        elif (choix =="2"):
            final_choice = 2
            return final_choice
        elif (choix =="3"):
            final_choice = 3
            return final_choice
        else:
            choix = str(input("choix inexistant merci d'entrer un nombre parmi ceux proposés: "))

def choix_du_mode_de_jeu_pas_machine():
    """
    fonction pour choisir le du mode de jeu (humain contre humain, humain contre machine ou machine contre machine)
    entrée: rien
    sortie: str 
    """
    choix : str
    final_choice : int

    choix = ""
    final_choice = 0
    
    print(r""" __  __  _____  ____  ____    ____  ____     ____  ____  __  __ 
(  \/  )(  _  )(  _ \( ___)  (  _ \( ___)   (_  _)( ___)(  )(  )
 )    (  )(_)(  )(_) ))__)    )(_) ))__)   .-_)(   )__)  )(__)( 
(_/\/\_)(_____)(____/(____)  (____/(____)  \____) (____)(______)""")
    while (choix != '3'):
        print("-----------------------")
        print("|1- Humain vs humain  |")
        print("|2- Humain vs machine |")
        print("-----------------------\n")
        choix = input("quel est est votre choix? : ")
        if (choix =="1"):
            final_choice = 1
            return final_choice
        elif (choix =="2"):
            final_choice = 2
            return final_choice
        else:
            choix = str(input("choix inexistant merci d'entrer un nombre parmi ceux proposés: "))

def choixdiff():
    """
    fonction pour choisir la difficulté de la partie
    entrée: rien
    sortie: str 
    """
    so : str
    diffi : int

    so = ""
    diffi = 0

    print(r"""  _____   ____  ______  ______  ____  ______  __   _  ____     __    ______   _____   ______   ____    ____     _____  ____    _____    __    ____  ______  
 |     \ |    ||   ___||   ___||    ||   ___||  | | ||    |  _|  |_ |   ___| |     \ |   ___| |    |  |    \   |     ||    \  |     | _|  |_ |    ||   ___| 
 |      \|    ||   ___||   ___||    ||   |__ |  |_| ||    |_|_    _||   ___| |      \|   ___| |    |_ |     \  |    _||     \ |     \|_    _||    ||   ___| 
 |______/|____||___|   |___|   |____||______||______||______| |__|  |______| |______/|______| |______||__|\__\ |___|  |__|\__\|__|\__\ |__|  |____||______|""")
    while (so != 4):
        print("\n----------------")
        print("|1- Facile      |")
        print("|2- Moyen       |")
        print("|3- Difficile   |")
        print("----------------\n")
        so = input("quel est est votre choix? : ")
        if (so == "1"):
            diffi = 1
            return diffi
        elif (so == "2"):
            diffi = 2
            return diffi
        elif (so == "3"):
            diffi = 3
            return diffi
        else:
            so = str(input("choix inexistant merci d'entrer un nombre parmi ceux proposés: "))

def menusDesScores():
    """
    procédure pour afficher le tableau des scores et les options diponibles
    entrée: rien
    sortie : rien(procédure)
    """
    choice : str
    cgame : str
    cpseudo : str

    cgame = ""
    choice = ""
    pseudo = ""
    print (r""" ___   ___  _____  ____  ____  ___ 
/ __) / __)(  _  )(  _ \( ___)/ __)
\__ \( (__  )(_)(  )   / )__) \__ \
(___/ \___)(_____)(_)\_)(____)(___/
           """)
    while (choice != '3') :
        print("--------------------------------------")
        print("| 1 - afficher le score d'un joueur  |")
        print("| 2 - afficher le tableau des scores |")
        print("| 3 - Quitter                        |")
        print("--------------------------------------\n")
        choice = input("quel est est votre choix? : ")
        if (choice  == '1') :
            print("------------------")
            print("| 1 - Devinettes |")
            print("| 2 - allumettes |")
            print("| 3 - morpion    |")
            print("| 4 - quitter    |")
            print("------------------")

            cgame = input("choisissez le jeu dont vous voulez voir les scores: ")
            if (cgame == '1'):
                cpseudo = input("entrez le pseudo du joueur dont vous voulez voir le score: ")
                scores.affichescore(cpseudo, score_dev)
            elif (cgame == '2'):
                cpseudo = input("entrez le pseudo du joueur dont vous voulez voir le score: ")
                scores.affichescore(cpseudo, score_all)
            elif (cgame == '3'):
                cpseudo = input("entrez le pseudo du joueur dont vous voulez voir le score: ")
                scores.affichescore(cpseudo,score_mor)
            elif (cgame != '4'):
                print("valeur erronée. Réessayez.")
        elif (choice == '2') : 
            print(r"""
-------------------------
|1 - Devinettes         |
|2 - Jeu des allumettes |
|3 - Morpion            |
------------------------- """)
            cgame = input("choisissez le jeu dont vous voulez voir les scores: ")
            if (cgame == '1' ) :
                scores.afficheTableauScores(score_dev)
            elif (cgame == '2'):
                scores.afficheTableauScores(score_all)
            elif (cgame == '3'):
                scores.afficheTableauScores(score_mor)
            elif (cgame != '4') :
                print("Valeur erronnée. Réessayez")
        print("\rVous avez quitté le menu des scores")
        print("------------------------------------")

#début du programme principal

if __name__=='__main__':
    choice : str #définition du type de toutes les variables
    player1 : str
    player2 : str
    mode : str
    diff : str
    score_all : list[list[str]]
    score_mor : list[list[str]]
    score_dev : list[list[str]]
    endallum : list[str]
    enddevine : list[str]
    endmorpion : list[str]
    
    

    with open("./sauvegarde/endall.pkl","rb") as fsal : 
        score_all = pickle.load(fsal)
    with open("./sauvegarde/endmor.pkl","rb") as fmorp : 
        score_mor = pickle.load(fmorp)
    with open("./sauvegarde/enddev.pkl","rb") as fdev : 
        score_dev = pickle.load(fdev)
    
    #initialisation des variables
    endallum = []
    enddevine = []
    endmorpion = []


    #imprimerle menu en boucle tant que les joueurs ne choisissent pas de sortir du programme
    while(True):
        mode = ''
        diff = ''
        #titre
        print(r"""                                           
                                   (          
          )   (       (           ))\ )   (   
 `  )  ( /(  ))\ (   ))\    (  ( /(()/(  ))\  
 /(/(  )(_))/((_))\ /((_)   )\ )(_))(_))/((_) 
((_)_\((_)_(_))(((_|_))    ((_|(_)(_) _(_))   
| '_ \) _` | || (_-< -_)  / _|/ _` |  _/ -_)  
| .__/\__,_|\_,_/__|___|  \__|\__,_|_| \___|  
|_|                                          
              """)

        print_menu()
        #Lancement du menu et des procédures correspondantes aux différentes parties du programmes
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check quel choix est entré et s'il correspond à un choix présent
        if option == 1:
            mode = choix_du_mode_de_jeu_pas_machine()
            if (mode == 1):
                player1 = input("entrer le pseudo du joueur 1 :")
                player2 = input("entrer le pseudo du joueur 2 :")
                enddevine = devinette.devinette_player_vs_player(player1,player2)
                scores.addToScore(enddevine[0],enddevine[1],score_dev)
                scores.afficheTableauScores(score_dev)
                scores.triescores(score_dev)
            else:
                if(mode == 2):
                    diff = choixdiff()
                    if (diff == 1):
                        player1 = input("entrer le pseudo du joueur: ")
                        enddevine = dev_h_m_e.devinette_player_vs_machine_easy(player1)
                        scores.addToScore(enddevine[0],enddevine[1],score_dev)
                        scores.afficheTableauScores(score_dev)
                        scores.triescores(score_dev)
                    elif (diff == 2):
                        player1 = input("entrer le pseudo du joueur: ")
                        enddevine = dev_h_m_m.devinette_player_vs_machine_medium(player1)
                        scores.addToScore(enddevine[0],enddevine[1],score_dev)
                        scores.afficheTableauScores(score_dev)
                        scores.triescores(score_dev)
                    elif (diff == 3):
                        player1 = input("entrer le pseudo du joueur: ")
                        enddevine = dev_h_m_h.devinette_player_vs_machine_hardcore(player1)
                        scores.addToScore(enddevine[0],enddevine[1],score_dev)
                        scores.afficheTableauScores(score_dev)
                        scores.triescores(score_dev)

        elif option == 2:
            mode = choix_du_mode_de_jeu_pas_machine()
            if (mode == 1):
                player1 = input("entrer le pseudo du joueur 1 :")
                player2 = input("entrer le pseudo du joueur 2 :")  
                endallum = allumettes.allumettes_player_vs_player(player1,player2)
                scores.addToScore(endallum[0],endallum[1],score_all)
                scores.afficheTableauScores(score_all)
                scores.triescores(score_all)
            elif (mode == 2):
                diff = choixdiff()
                if (diff == 1):
                    player1 = input("entrer le pseudo du joueur: ")
                    endallum = all_h_m_e.allumettes_player_vs_machine_easy(player1)
                    scores.addToScore(endallum[0],endallum[1],score_all)
                    scores.afficheTableauScores(score_all)
                    scores.triescores(score_all)
                elif (diff == 2):
                    player1 = input("entrer le pseudo du joueur: ")
                    endallum = all_h_m_m.allumettes_player_vs_machine_medium(player1)
                    scores.addToScore(endallum[0],endallum[1],score_all)
                    scores.afficheTableauScores(score_all)
                    scores.triescores(score_all)
                elif (diff == 3):
                    player1 = input("entrer le pseudo du joueur: ")
                    endallum= all_h_m_h.allumettes_player_vs_machine_hardcore(player1)
                    scores.addToScore(endallum[0],endallum[1],score_all)
                    scores.afficheTableauScores(score_all)
                    scores.triescores(score_all)

        elif option == 3:
            mode = choix_du_mode_de_jeu()
            if (mode == 1):
                player1 = input("entrer le pseudo du joueur 1 :")
                player2 = input("entrer le pseudo du joueur 2 :")
                endmorpion = morpion.jeu_du_morpion_humain_humain(player1,player2)
                scores.addToScore(endmorpion[0],endmorpion[1],score_mor)
                scores.afficheTableauScores(score_mor)
                scores.triescores(score_mor)
            elif (mode == 2):
                player1 = input("entrer le pseudo du joueur: ")
                endmorpion = morpion.jeu_du_morpion_humain_machine_easy(player1)
                scores.addToScore(endmorpion[0],endmorpion[1],score_mor)
                scores.afficheTableauScores(score_mor)
                scores.triescores(score_mor)
            elif (mode == 3):
                print ("bot vs bot")
                morpion.jeu_du_morpion_machine_machine()

        elif option == 4:
            menusDesScores()

        elif option == 5:
            print("Au revoir")
            break

        else:
            print('choix inexistant merci de rentrer un nombre entre 1 et 5 compris.')

#sauvegarde des scores
    with open("./sauvegarde/scoredev.pkl", "rb") as fsdev :
        pickle.dump(score_dev, fsdev)
    with open("./sauvegarde/scoreal.pkl", "rb") as fsal :
        pickle.dump(score_all, fsal)
    with open("./sauvegarde/scoremmor.pkl", "rb") as fsmor :
        pickle.dump(score_mor, fsmor)