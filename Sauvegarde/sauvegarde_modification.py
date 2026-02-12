import json
from pathlib import Path
from typing import Any
from .sauvegarde_donnee import SauvegardeDonnee
from Personnage.Heros.heros_factory import HerosFactory
from Zone.zone_factory import ZoneFactory
from Personnage.Inventaire.inventaire import Inventaire
from Personnage.Inventaire.arme import Arme
from Personnage.Inventaire.armure import Armure
from Personnage.Inventaire.consommable import Consommable

class SauvegardeModification:
    def __init__(self, chemin_dossier: str = "sauvegarder"):
        self.dossier = Path(chemin_dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.heros_factory = HerosFactory()
        self.zone_factory = ZoneFactory()

    def sauvegarder(self, jeu: Any, nom_fichier: str = "sauvegarde.json") -> None:
        hero = jeu.hero
        stats = hero.stats

        inventaire_dict = self._serialiser_inventaire(hero.inventaire)
        arme_dict = self._serialiser_arme(hero.inventaire.arme)
        armure_dict = self._serialiser_armure(hero.inventaire.armure)

        data = SauvegardeDonnee(
            classe_hero=hero.classe,
            nom_hero=hero.nom,
            pv_hero=stats.pv,
            pv_max_hero=stats.pv_max,
            attaque_hero=stats.attaque,
            defense_hero=stats.defense,
            vitesse_hero=stats.vitesse,
            agilite_hero=stats.agilite,
            endurance_hero=stats.endurance,
            intelligence_hero=getattr(stats, "intelligence", 0),
            or_hero=hero.or_,

            zone_actuelle=jeu.zone_actuelle.nom,
            etat_quete=jeu.quete_principale.etat.value,

            inventaire=inventaire_dict,
            arme_equipee=arme_dict,
            armure_equipee=armure_dict,
        )

        chemin = self.dossier / nom_fichier
        with chemin.open("w", encoding="utf-8") as f:
            json.dump(data.en_dict(), f, ensure_ascii=False, indent=2)

    def _serialiser_inventaire(self, inventaire: Inventaire):
    # NE PAS OUBLIER DE COMPLETER DEMAIN
        result = []
        for obj in inventaire.objets:
            if isinstance(obj, Arme):
                result.append({
                    "type": "arme",
                    "nom": obj.name,
                    "degats": obj.degats,
                    "element": obj.element,
                })
            elif isinstance(obj, Armure):
                result.append({
                    "type": "armure",
                    "nom": obj.name,
                    "degats": obj.degats,
                    "element": obj.element,
                })
            elif isinstance(obj, Consommable):
                result.append({
                    "type": "consommable",
                    "nom": obj.name,
                })
        return result

    def _serialiser_arme(self, arme: Arme | None):
        if arme is None:
            return None
        return {"nom": arme.name, "degats": arme.degats, "element": arme.element}

    def _serialiser_armure(self, armure: Armure | None):
        if armure is None:
            return None
        return {"nom": armure.name, "degats": armure.degats, "element": armure.element}

    def charger(self, nom_fichier: str = "sauvegarde.json") -> Any:
        chemin = self.dossier / nom_fichier
        with chemin.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        hero = self.heros_factory.creer_hero(
            classe=raw["classe_hero"],
            nom=raw["nom_hero"]
        )

        zone = self.zone_factory.creer_zone(raw["zone_actuelle"])

        inventaire = Inventaire()
        self._reconstituer_inventaire(inventaire, raw["inventaire"])
        hero.inventaire = inventaire

        return None

    def _reconstituer_inventaire(self, inventaire: Inventaire, data_liste):
        for data in data_liste:
            type_ = data["type"]
            if type_ == "arme":
                obj = Arme(data["nom"], data["degats"], data["element"])
            elif type_ == "armure":
                obj = Armure(data["nom"], data["degats"], data["element"])
            elif type_ == "consommable":
                obj = Consommable(data["nom"])
            else:
                continue
            inventaire.ajout(obj)