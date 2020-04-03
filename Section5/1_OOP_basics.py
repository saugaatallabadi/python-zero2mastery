# OOP

# Naming convention- CamelCase


class BigObject:
    # Create blueprint here
    pass


obj1 = BigObject()  # Instantiating a class to create an instance/object
obj2 = BigObject()  # Instantiating a class to create an instance/object
obj3 = BigObject()  # Instantiating a class to create an instance/object

# Video 112:


class PlayerCharacter:  # Usually singular (since it's a blueprint)
    # Class Object Attribute
    membership = True  # Not dynamic; It's static
    '''
        - A special method (dunder/magic method)
        - A constructor/init method
        - Gets called anytime we instantiate
        - Whatever we give after 'self' is the parameter
        - 'self' refers to the PlayerCharacter

    '''

    '''
        NOTE: Write _ before attribute names to denote that this is private i.e. please keep 'em private.
        You can override them, but please don't.

        Whatever params go inside init, that's what you have to use to use PlayerCharacter.
    '''

    def __init__(self, name='anonymous', age=0):  # name of character
        if self.membership == True:  # or use PlayerCharacter.membership
            self._name = name  # attributes/properties
            self._age = age

    def run(self):
        return 'Running'

    def speak(self):  # All methods have 'self' as first parameter
        return f'My name is {self._name} and I am {self._age} years old'

    @classmethod  # Does not need instantiation; Leverages __init__
    def adding_things(cls, num1, num2):  # cls = Class
        return num1 + num2

    @staticmethod  # Does not care what __init__ says
    def adding_things2(num1, num2):  # cls = Class
        return num1 + num2


player1 = PlayerCharacter('Cindy', 22)
player2 = PlayerCharacter('Tom', 24)
print(player1.run())
print(player1.membership)
print(player2._age)
print(player2.speak())
print(player1.adding_things(2, 3))
