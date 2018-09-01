"Functionality of rst game with unit parameters provided in files."

class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"
        file_name = f"{self.unit_type.lower()}_{level}.dat"

        with open(file_name, "r") as paramter_file:
            lines = paramter_file.read().split("\n")

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

class Archer(object):
    def __init__(self, level):
        self.unit_type = "Archer"
        file_name = f"{self.unit_type.lower()}_{level}.dat"

        with open(file_name, "r") as paramter_file:
            lines = paramter_file.read().split("\n")

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

class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "Knight":
            return Knight(level)
        elif unit_type == "Archer":
            return Archer(level)
        else:
            raise NoSuchType(f"Provided type: {unit_type} does not exist.")

class NoSuchType(Exception):
    pass


if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("Knight", 1)
    archer1 = barracks.build_unit("Archer", 2)

    print(f"[knight1] {knight1}")
    print(f"[archer1] {archer1}")