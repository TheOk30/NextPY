from functools import reduce

class IDIterator():
    # Class to generate valid ID numbers using an iterator

    def __init__(self, id):
       self._id = int(id)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._id == 999999999:
            raise StopIteration
        
        self._id += 1

        while not check_id_valid(self._id):
            self._id += 1
        
        return self._id

def add(x, y):
    # Function to add every digit in the ID number
    # used for the sum calculation
    
    if y > 9:
        y = y % 10 + y // 10
    return x + y

def check_id_valid(id_number):
    # Function to check if the ID number is valid
    # Using the instructions from the exercise

    dig = list(int(d) for d in str(id_number))
    dig = [dig[d] * 2 if d % 2 != 0 else dig[d] for d in range(0, len(dig))]
    sum = reduce(add, dig, 0)
    return sum % 10 == 0

def id_generator(id):
    # Function to generate a valid ID number

    while id < 999999999:
        id += 1
        if check_id_valid(id):
            yield id

def main():
    print(check_id_valid(123456780)) # False
    print(check_id_valid(123456782)) # True

    id = int(input("Enter id: "))
    msg = input("Generator or Iterator? (gen/it)? ")
    if msg == "gen":
        valid_id_iter = iter(IDIterator(id))
        for _ in range(0, 10):
            print(next(valid_id_iter))

    elif msg == "it":
        id_gen = id_generator(id)
        for _ in range(0, 10):
            print(next(id_gen))
        
if __name__ == "__main__":
    main()