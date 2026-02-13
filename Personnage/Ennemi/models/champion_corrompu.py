# from Personnage.Ennemi.ennemi import Ennemi

# class ChampionCorrompu(Ennemi):
#     def __init__(self, nom):
#         super().__init__(nom=nom, pv=100, attaque=15, defense=20, vitesse=10, agilite=10, endurance=10)


from Personnage.Ennemi.ennemi import Ennemi

class ChampionCorrompu(Ennemi):
    def __init__(self, nom: str = "Champion corrompu"):
        super().__init__(
            nom=nom,
            pv=180,
            attaque=22,
            defense=18,
            vitesse=8,
            agilite=10,
            endurance=15,
            intelligence=0,
            niveau=2,
        )

    def competence_speciale(self, cible):
# A FAIRE 
        pass
