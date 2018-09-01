"RTS with prototype desing pattern."
from prototype_1 import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"

        FILENAME = f"{self.unit_type.lower()}_{level}.dat"

        with open(FILENAME, "r") as parameter_file:
            lines = parameter_file.read().split("\n")

            self.life = int(lines[0])
            self.speed = int(lines[1])
            self.attack_power = int(lines[2])
            self.attack_range = int(lines[3])
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
               f"Life: {self.life}\n" \
               f"Speed: {self.speed}\n" \
               f"Attack Power: {self.attack_power}\n" \
               f"Attack Range: {self.attack_range}\n" \
               f"Weapon: {self.weapon}\n"

    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"

        FILENAME = f"{self.unit_type.lower()}_{level}.dat"

        with open(FILENAME, "r") as parameter_file:
            lines = parameter_file.read().split("\n")

            self.life = int(lines[0])
            self.speed = int(lines[1])
            self.attack_power = int(lines[2])
            self.attack_range = int(lines[3])
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
               f"Life: {self.life}\n" \
               f"Speed: {self.speed}\n" \
               f"Attack Power: {self.attack_power}\n" \
               f"Attack Range: {self.attack_range}\n" \
               f"Weapon: {self.weapon}\n"

    def clone(self):
        return deepcopy(self)

class Barracks(object):
    def __init__(self):
        self.units = {
            "Knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "Archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":

    barracks = Barracks()

    knight1 = barracks.build_unit("Knight", 1)
    archer1 = barracks.build_unit("Archer", 2)

    print(f"[knight1] {knight1}")
    print(f"[archer1] {archer1}")