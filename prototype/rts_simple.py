"Simple implementation of rts game."

class Knight(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f"Life: {self.life}\n" \
               f"Speed: {self.speed}\n" \
               f"Attack Power: {self.attack_power}\n" \
               f"Attack Range: {self.attack_range}\n" \
               f"Weapon: {self.weapon}\n"

class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    print(f"[knight1] {knight1}")