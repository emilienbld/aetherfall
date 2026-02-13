from Personnage.Heros.heros import Heros

class Guerrier(Heros):
    def __init__(self, nom: str):
        super().__init__(nom,150,20,15,5,5,10)

    def coup_puissant(self, cible):
        degats = int(self.attaque * 1.5) - cible.defense
        degats = max(1, degats)
        cible.recevoir_degats(degats)
        return degats

    def charge_heroique(self, cible):
        degats = self.attaque * 2 - cible.defense
        degats = max(1, degats)
        cible.recevoir_degats(degats)
        return degats
