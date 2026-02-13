from Personnage.Ennemi.ennemi_factory import EnnemiFactory
from Evenements.evenement_factory import EvenementFactory
from Zone.zone import Zone


class ZoneFactory:
    @staticmethod
    def creer_village():
        zone = Zone(
            "Village",
            None,
            None,
        )

        zone.evenements = EvenementFactory.creer_factory_village()
        return zone

    @staticmethod
    def creer_foret():
        zone = Zone("Foret",
                    EnnemiFactory.creer_ennemis_foret(),
                    None
                    )

        zone.evenements = EvenementFactory.creer_factory_foret(zone)
        return zone

    @staticmethod
    def creer_donjon():
        zone = Zone("Donjon",
                    EnnemiFactory.creer_ennemis_donjon(),
                    EnnemiFactory.creer_boss()
                    )

        zone.evenements = EvenementFactory.creer_factory_donjon(zone)
        zone.bossFight = EvenementFactory.creer_boss_donjon(zone)
        return zone