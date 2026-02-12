from Personnage.Heros.guerrier import Guerrier
from Personnage.Heros.mage import Mage
from Personnage.Heros.voleur import Voleur


class HerosFactory:
    @staticmethod
    def creer_hero(hero):
        if hero == 'guerrier':
            return Guerrier()
        if hero == 'mage':
            return Mage()
        if hero == 'voleur':
            return Voleur()
        raise ValueError("Héros inconnu")