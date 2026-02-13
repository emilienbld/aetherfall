import json
from pathlib import Path
from typing import Any, List
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

    def _chemin_fichier(self, nom_sauvegarde: str) -> Path:
        nom_sauvegarde = nom_sauvegarde.strip()
        if not nom_sauvegarde:
            nom_sauvegarde = "sauvegarde"
        return self.dossier / f"{nom_sauvegarde}.json"

    def lister_sauvegardes(self) -> List[str]:
        noms: List[str] = []
        for fichier in self.dossier.glob("*.json"):
            noms.append(fichier.stem)
        return noms

    def sauvegarder(self, jeu: Any, nom_sauvegarde: str) -> None:
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

        chemin = self._chemin_fichier(nom_sauvegarde)
        with chemin.open("w", encoding="utf-8") as f:
            json.dump(data.en_dict(), f, ensure_ascii=False, indent=2)

    def _serialiser_inventaire(self, inventaire: Inventaire):
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
                    "protection": obj.protection,
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
        return {
            "nom": armure.name,
            "protection": armure.protection,
            "element": armure.element,
        }
    
    def charger(self, nom_sauvegarde: str) -> Any:
        chemin = self._chemin_fichier(nom_sauvegarde)
        if not chemin.exists():
            raise FileNotFoundError(f"Sauvegarde introuvable : {chemin}")

        with chemin.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        hero = self.heros_factory.creer_hero(
            classe=raw["classe_hero"],
            nom=raw["nom_hero"]
        )

        hero.stats.pv = raw["pv_hero"]
        hero.stats.pv_max = raw["pv_max_hero"]
        hero.stats.attaque = raw["attaque_hero"]
        hero.stats.defense = raw["defense_hero"]
        hero.stats.vitesse = raw["vitesse_hero"]
        hero.stats.agilite = raw["agilite_hero"]
        hero.stats.endurance = raw["endurance_hero"]
        hero.stats.intelligence = raw["intelligence_hero"]
        hero.or_ = raw["or_hero"]

        zone = self.zone_factory.creer_zone(raw["zone_actuelle"])

        inventaire = Inventaire()
        self._reconstituer_inventaire(inventaire, raw["inventaire"])

        if raw.get("arme_equipee"):
            arme_data = raw["arme_equipee"]
            arme = Arme(arme_data["nom"], arme_data["degats"], arme_data["element"])
            inventaire.equiper_arme(arme)

        if raw.get("armure_equipee"):
            armure_data = raw["armure_equipee"]
            armure = Armure(
                armure_data["nom"],
                armure_data["protection"],
                armure_data["element"],
            )
            inventaire.equiper_armure(armure)

        hero.inventaire = inventaire

        etat_quete = raw["etat_quete"]

        return hero, zone, etat_quete

    def _reconstituer_inventaire(self, inventaire: Inventaire, data_liste):
        for data in data_liste:
            type_ = data["type"]
            if type_ == "arme":
                obj = Arme(data["nom"], data["degats"], data.get("element"))
            elif type_ == "armure":
                obj = Armure(data["nom"], data["protection"], data.get("element"))
            elif type_ == "consommable":
                obj = Consommable(data["nom"])
            else:
                continue
            inventaire.ajout(obj)