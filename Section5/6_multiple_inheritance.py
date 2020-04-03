class User:  # Use brackets only when inheriting from a super

    def sign_in(self):
        return 'Logged in'

    def attack(self):
        print('do nothing')


class Wizard(User):  # Pass the parent class that we wanna inherit from
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with {self.power}')


class Archer(User):  # Subclasses/Derived classes
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        # User.attack(self)
        print(f'Arrows left: {self.arrows}')

    def run(self):
        print('Ran really fast')

# The order Wizard 1st and Archer 2nd matters a lot


class HybridBorg(Wizard, Archer):  # has powers of both Wizard and Archer
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


# Instantiating a class
# wizard1 = Wizard('Merlin', 50)
hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
