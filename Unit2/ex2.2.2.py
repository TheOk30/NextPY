class Animal:

    def __init__(self):
        self.name = "octavio"
        self.age = 2
    
    def birthday(self):
        self.age += 1
    
    def display(self):
        print(self.name, self.age)

def main():
    octupus = Animal()
    chicken = Animal()
    octupus.birthday()
    chicken.birthday()
    octupus.display() # octupus 3
    chicken.display() # octupus 3


if __name__ == "__main__":
    main()