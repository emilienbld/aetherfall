from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from Personnage.Inventaire.inventaire import Inventaire
    from Combat.statut import Statut  # A CRÉER

class Personnage:
    def __init__(
        self,
        nom: str,
        pv: int,
        attaque: int,
        defense: int,
        vitesse: int = 0,
        agilite: int = 0,
        endurance: int = 0,
        intelligence: int = 0,
        inventaire: Optional["Inventaire"] = None,
    ):
        self.nom = nom
        self.pv_max = pv
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.agilite = agilite
        self.endurance = endurance
        self.intelligence = intelligence

        self.inventaire: Optional["Inventaire"] = inventaire
        self.statuts: List["Statut"] = []

    def est_vivant(self) -> bool:
        return self.pv > 0

    def recevoir_degats(self, degats: int) -> None:
        self.pv = max(0, self.pv - degats)

    def soigner(self, montant: int) -> None:
        self.pv = min(self.pv_max, self.pv + montant)

    def attaquer(self, cible: "Personnage") -> int:
        degats = max(1, self.attaque - cible.defense)
        cible.recevoir_degats(degats)
        return degats

    def defendre(self) -> None:
        # A FAIRE
        pass
