def devisable_by_four(num):
    return num % 4 == 0

def four_dividers(number):
    return list(filter(devisable_by_four, range(1, number + 1)))


def main():
    print(four_dividers(9)) # [4, 8]
    print(four_dividers(3)) # []

if __name__ == "__main__":
    main()