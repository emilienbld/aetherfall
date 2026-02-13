from Personnage.Ennemi.ennemi import Ennemi

class ChampionCorrompu(Ennemi):
    def __init__(self, nom):
        super().__init__(
            nom=nom,
            pv=180,
            attaque=22,
            defense=18,
            vitesse=8,
            agilite=10,
            endurance=15,
        )

    def competence_speciale(self, cible):
        pass
