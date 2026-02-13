from Personnage.Ennemi.ennemi import Ennemi

class Boss(Ennemi):
    def __init__(self, nom: str = "Gardien du Donjon"):
        super().__init__(nom,250,25,20,10,10,20)
        self.phase_2 = False

    def verifier_phase(self):

        if not self.phase_2 and self.pv <= self.pv_max / 2:
            self.phase_2 = True
            self.attaque += 5

    def choisir_action(self, cible):
        self.verifier_phase()
        return super().choisir_action(cible)
