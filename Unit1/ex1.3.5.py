import functools

def main():
    # 1
    # Create a list of names find the longest name using reduce and lambda functions
    names = open(r"Unit1\names.txt", "r").read().splitlines()
    print(functools.reduce(lambda x, y: x if x > y else y, names))
    # Valdimir

    # 2
    # Create a list of names caluclate the sum of the names using reduce and lambda functions
    names = open(r"Unit1\names.txt", "r").read().splitlines()
    print(functools.reduce(lambda x, y: x + len(y), names, 0))
    # 38

    # 3
    # print the shortest names from the using a one liner from
    names = open(r"Unit1\names.txt", "r").read().splitlines()
    print('\n'.join([line for line in names if len(line) == len(min(names, key=len))]))
    # Ed
    # Jo

    # 4
    # open a new file and write the length of the names to it
    names = open(r"Unit1\names.txt", "r").read().splitlines()
    open(r"Unit1\name_length.txt", "w").writelines([str(len(line)) + "\n" for line in names])
    # 4
    # 4
    # 8
    # 7
    # 2
    # 5
    # 6
    # 2

    # 5
    # enter length of name and the program will return the names with that length
    length = int(input("Enter the length of the name: "))
    names = open(r"Unit1\names.txt", "r").read().splitlines()
    print('\n'.join([line for line in names if len(line) == length]))
    # Hans
    # Anna


if __name__ == "__main__":
    main()