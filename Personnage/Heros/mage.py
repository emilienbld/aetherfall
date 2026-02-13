from Personnage.Heros.heros import Heros

class Mage(Heros):
    def __init__(self, nom: str):
        super().__init__(nom,90,5,5,7,5,5)
        self.mana_max = 50
        self.mana = 50
        self.intelligence = 50

    def boule_de_feu(self, cible):
        if self.mana < 10:
            return 0
        self.mana -= 10
        degats = self.intelligence * 2 - cible.defense
        degats = max(1, degats)
        cible.recevoir_degats(degats)
        return degats

    def bouclier_arcanique(self):
        if self.mana < 8:
            return False
        self.mana -= 8
        return True
