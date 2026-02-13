# from Personnage.Ennemi.ennemi import Ennemi

# class Bandit(Ennemi):
#     def __init__(self,nom):
#         super().__init__(nom=nom,pv=100,attaque=15,defense=20,vitesse=10,agilite=10,endurance=10)

#     def vol(self):
#         pass

from Personnage.Ennemi.ennemi import Ennemi

class Bandit(Ennemi):
    def __init__(self, nom: str = "Bandit"):
        super().__init__(
            nom=nom,
            pv=100,
            attaque=15,
            defense=10,
            vitesse=10,
            agilite=10,
            endurance=10,
            intelligence=0,
            niveau=1,
        )

    def vol(self, cible):
# A FAIRE
        pass

    def choisir_action(self, cible):
        return super().choisir_action(cible)
