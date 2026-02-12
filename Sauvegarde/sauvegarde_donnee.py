from dataclasses import dataclass, asdict
from typing import Any, Dict, List

@dataclass
class SauvegardeDonnee:
    # NE PAS OUBLIER DE COMPLETER DEMAIN
    classe_hero: str
    nom_hero: str
    pv_hero: int
    pv_max_hero: int
    attaque_hero: int
    defense_hero: int
    vitesse_hero: int
    agilite_hero: int
    endurance_hero: int
    intelligence_hero: int

    or_hero: int

    zone_actuelle: str
    etat_quete: int

    inventaire: List[Dict[str, Any]]

    arme_equipee: Dict[str, Any] | None
    armure_equipee: Dict[str, Any] | None

    def en_dict(self) -> Dict[str, Any]:
        return asdict(self)