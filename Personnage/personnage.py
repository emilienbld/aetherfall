from abc import ABC, abstractmethod

from Personnage.Inventaire.inventaire import Inventaire


class Personnage(ABC):
    def __init__(self,nom,pv,attaque,defense,vitesse,agilite,endurance):
        self.nom = nom
        self.pv = pv
        self.pv_max = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.agilite = agilite
        self.endurance = endurance
        self.endurance_max = endurance
        self.alive = pv > 0
        self.status = []
        self.inventaire = Inventaire()

    @abstractmethod
    def attaquer(self):
        pass

    @abstractmethod
    def subir(self):
        pass

    @abstractmethod
    def esquive(self):
        pass

    def afficher_stats(self):
        return print(f"{self.nom}"
                     f"{self.pv}/{self.pv_max} Pv"
                     f"{self.endurance}/{self.endurance_max} Endurance"
                     f"{self.attaque} Attaque"
                     f"{self.defense} Defense"
                     f"{self.vitesse} Vitesse"
                     f"{self.agilite} Agilité")