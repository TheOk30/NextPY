def is_funny(string):
    return all(char == 'a' or char == 'h' for char in string)

def main():
    print(is_funny("hahahahahaha")) # True

if __name__ == "__main__":
    main()