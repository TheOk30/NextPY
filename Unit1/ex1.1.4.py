from functools import reduce

def add(x, y):
    return x + y

def sum_of_digits(number):
    return reduce(add, [int(x) for x in str(number)])

def main():
    print(sum_of_digits(104)) # 5

if __name__ == "__main__":
    main()