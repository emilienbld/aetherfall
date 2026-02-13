from Personnage.Heros.heros import Heros

class Voleur(Heros):
    def __init__(self, nom: str):
        super().__init__(
            nom=nom,
            pv=110,
            attaque=15,
            defense=8,
            vitesse=15,
            agilite=20,
            endurance=10,
            intelligence=0,
        )
        self.endurance_max = 50
        self.endurance_courante = 50

    def attaque_sournoise(self, cible):
        if self.endurance_courante < 10:
            return 0
        self.endurance_courante -= 10
        degats = int(self.attaque * 1.8) - cible.defense
        degats = max(1, degats)
        cible.recevoir_degats(degats)
        return degats

    def esquive_parfaite(self):
        if self.endurance_courante < 8:
            return False
        self.endurance_courante -= 8
        return True
