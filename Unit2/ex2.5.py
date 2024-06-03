class Animal:
    # animal class that is the father of all the subsequent classes
    
    # Class variable
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("talk")


class Dog(Animal):
    # dog class that is the child of the animal class
    def talk(self):
        print("woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    # cat class that is the child of the animal class
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    # skunk class that is the child of the animal class
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    # unicorn class that is the child of the animal class
    _stink_count = 6

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    # dragon class that is the child of the animal class
    _color = "Greem"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    # Create instances of different animals
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    # Create a list of animals
    zoo_lst = [dog, cat, skunk, unicorn, dragon]

    # Create additional instances of animals
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    # Extend the list with additional animals
    zoo_lst.extend([dog2, cat2, skunk2, unicorn2, dragon2])

    # Iterate over the list of animals
    for animal in zoo_lst:
        if animal.is_hungry():
            # Print the type and name of the animal
            print(type(animal).__name__, animal.get_name())

            # Make the animal talk and feed it
            animal.talk()
            animal.feed()

            # Perform specific actions based on the animal type
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            elif isinstance(animal, Dragon):
                animal.breath_fire()

    # Print the zoo name
    print("Zoo name is:", Animal.zoo_name)


if __name__ == "__main__":
    main()