# from Personnage.Ennemi.ennemi import Ennemi

# class LoupSauvage(Ennemi):
#     def __init__(self,nom):
#         super().__init__(nom=nom,pv=100,attaque=15,defense=20,vitesse=10,agilite=10,endurance=10)

#     def attaqueMultiple(self):
#         pass

from Personnage.Ennemi.ennemi import Ennemi

class LoupSauvage(Ennemi):
    def __init__(self, nom: str = "Loup sauvage"):
        super().__init__(
            nom=nom,
            pv=80,
            attaque=18,
            defense=5,
            vitesse=15,
            agilite=12,
            endurance=8,
            intelligence=0,
            niveau=1,
        )

    def attaques_multiples(self, cible):
        degats_total = 0
        for _ in range(2):
            degats_total += self.attaquer(cible)
        return degats_total

    def choisir_action(self, cible):
        return super().choisir_action(cible)
