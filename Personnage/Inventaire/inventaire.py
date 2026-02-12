from collections import deque

from Personnage.Inventaire.arme import Arme
from Personnage.Inventaire.armure import Armure


class Inventaire():
    def __init__(self):
        self.arme = None
        self.armure = None
        self.items = deque(maxlen=10)

    def ajout_item(self, item):
        if len(self.items) < 10:
            self.items.append(item)
            return True
        print("Inventaire plein!")
        return False

    def equiper_arme(self, item):
        if isinstance(item, Arme):
            self.arme = item
            if item in self.items:
                self.items.remove(item)
            return True
        return False

    def equiper_armure(self, item):
        if isinstance(item, Armure):
            self.armure = item
            if item in self.items:
                self.items.remove(item)
            return True
        return False

    def afficher(self):
        print("\n=== INVENTAIRE ===")
        print(f"Arme équipée: {self.arme.nom if self.arme else 'Aucune'}")
        print(f"Armure équipée: {self.armure.nom if self.armure else 'Aucune'}")
        print(f"Objets ({len(self.items)}/10):")
        for i, item in enumerate(self.items, 1):
            print(f"  {i}. {item.nom}")