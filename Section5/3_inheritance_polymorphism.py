# INHERITANCE (Python supports multiple inheritances)

# Users can be wizards/archers

# class User(object):  # Same thing


class User:  # Use brackets only when inheriting from a super
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return 'Logged in'

    def attack(self):
        print('do nothing')


class Wizard(User):  # Pass the parent class that we wanna inherit from
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # Calling init method of User inside Wizard
        super().__init__(email)  # Or use this!
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with {self.power}')


class Archer(User):  # Subclasses/Derived classes
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        # User.attack(self)
        print(f'Arrows left: {self.num_arrows}')


# Instantiating a class
wizard1 = Wizard('Merlin', 50, 'him@sample.com')
archer1 = Archer('Robin', 100)
print(wizard1.email)
print(wizard1.attack())
print(wizard1.sign_in())
print(archer1.attack())
print(archer1.sign_in())

# isinstance(instance, Class)
print(isinstance(wizard1, Wizard))  # Prints True
print(isinstance(wizard1, User))  # Prints True
# Prints True; everything is an object / Inherits from object
print(isinstance(wizard1, object))


# POLYMORPHISM

def player_attack(character):
    character.attack()


player_attack(wizard1)
player_attack(archer1)


for char in [wizard1, archer1]:
    char.attack()
