from Personnage.Heros.guerrier import Guerrier
from Personnage.Heros.mage import Mage
from Personnage.Heros.voleur import Voleur
from Personnage.Heros.heros import Heros

class HerosFactory:
    def creer_heros(self, classe: str, nom: str) -> Heros:
        classe = classe.lower()
        if classe == "guerrier":
            return Guerrier(nom)
        if classe == "mage":
            return Mage(nom)
        if classe == "voleur":
            return Voleur(nom)
        raise ValueError(f"Héros inconnu : {classe}")
