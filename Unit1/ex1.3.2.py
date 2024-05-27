def is_prime(number):
    return number > 1 and not any(number % i == 0 for i in range(2, number))

def main(): 
    print(is_prime(42)) # False
    print(is_prime(43)) # True

if __name__ == "__main__":
    main()