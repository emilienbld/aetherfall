from __future__ import annotations
from typing import Optional

from Personnage.personnage import Personnage
from Personnage.Inventaire.inventaire import Inventaire

class Heros(Personnage):
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
        or_: int = 0,
        inventaire: Optional[Inventaire] = None,
    ):
        super().__init__(
            nom=nom,
            pv=pv,
            attaque=attaque,
            defense=defense,
            vitesse=vitesse,
            agilite=agilite,
            endurance=endurance,
            intelligence=intelligence,
            inventaire=inventaire or Inventaire(),
        )
        self.or_ = or_
        self.classe = self.__class__.__name__
