from Evenements.abstractEvenement import AbstractEvenement
from Personnage.Heros.heros import Heros


class Combat(AbstractEvenement):
    def __init__(self,ennemi):
        self.ennemi = ennemi
        self.tour = 0
        self.joueur = None

    def executer(self,personnage : Heros):
        self.joueur = personnage
        print(f"Vous avez été repéré par {self.ennemi.nom}")
        self.ennemi.afficher_stats()
        self.joueur.afficher_stats()

        print(f"Voulez vous l'affronter? ")
        choix = input("1. Oui 2. Non")

        if(choix == 1):
            while self.joueur.pv > 0 and self.ennemi.pv > 0:
                self.tour += 1
                print(f"\n{'=' * 50}")
                print(f"TOUR {self.tour}")
                print('=' * 50)

                # Tour du joueur
                self.tour_joueur()

                # Tour ennemi (s'il est vivant)
                if self.ennemi.pv > 0:
                    self.tour_ennemi()

            return self.conclure_combat()