class Character:
    def __init__(self, name, status, strength, mc, home):
        self.name = name
        self.status = status
        self.strength = strength
        self.midichlorian_count = mc
        self.home = home

    def fight(self):
        print("Lightsaber activate!, says ", self.name)


class Droid(Character):
    def __init__(self, name, status, strength, mc, home, model):
        super().__init__(name, status, strength, mc, home)
        self.model = model

    def roger(self):
        print("Roger, Roger says", self.name)

    def fight(self):
        super(Droid, self).fight()
        print("That's the jedi, blast them!, says", self.name)


jedi_1 = Character("Obi-Wan Kenobi", "Jedi Master", 100, 20, "Tatooine")

jedi_2 = Character("Yoda", "Jedi Master", 200, 50, "Dagobah")

object1 = Droid("R4", "Commander", 1, 0, "Geonosis", "B1 Battle Droid")

jedi_1.fight()

jedi_2.fight()

object1.fight()
