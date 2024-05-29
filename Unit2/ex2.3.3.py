class Animal:

    def __init__(self, name = "octavio", age = 0):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def birthday(self):
        self._age += 1

    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age

def main():
    octupus = Animal("Octupus", 2)
    chicken = Animal("Chicken", 1)
    octupus.birthday()
    chicken.birthday()
    print(octupus.get_name(), octupus.get_age()) # octupus 3
    print(chicken.get_name(), chicken.get_age()) # chicken 2
    octupus.set_name("Octavio")
    print(octupus.get_name(), octupus.get_age()) # Octavio 3


if __name__ == "__main__":
    main()