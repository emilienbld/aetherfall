import random

class Zone:
    def __init__(self, name,ennemis,boss):
        self.name = name
        self.ennemis = ennemis
        self.boss = boss
        self.evenements = []
        self.bossFight = None

    def event_aleatoire(self, personnage):
        event = random.choice(self.evenements)
        event.executer()
        self.evenements.remove(event)