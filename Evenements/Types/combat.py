from Evenements.abstractEvenement import AbstractEvenement
from Personnage.Heros.heros import Heros


class Combat(AbstractEvenement):
    def __init__(self,ennemi):
        self.ennemi = ennemi
        self.tour = 0
        self.joueur = None

    def executer(self,personnage: Heros):
        self.joueur = personnage
        print(f"Vous avez été repéré par {self.ennemi.nom}")
        self.ennemi.afficher_stats()
        self.joueur.afficher_stats()

        print(f"Voulez vous l'affronter? ")
        choix = input("1. Oui 2. Non")

        match choix:
            case 1:
                while self.joueur.alive and self.ennemi.alive:
                    self.tour += 1
                    print(f"\n{'=' * 50}")
                    print(f"Tour {self.tour}")

                    self.tour_joueur(self.joueur)

                    if self.ennemi.alive:
                        self.tour_ennemi()

                return self.conclure_combat()
            case 2:
                print(f"Vous avez fui le combat")

    def tour_joueur(self,joueur):
        print(f"\n Que voulez vous faire?"
              f"1. Prendre une consommable"
              f"2. Attaquer")

        choix = input()
        match choix:
            case 1:
                pass
            case 2:
                joueur.choisir_action(self.ennemi)

    def tour_ennemi(self,joueur):
        self.ennemi.attaquer()