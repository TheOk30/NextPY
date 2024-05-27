import functools

def function(num, item):
    return num + 1

def main():
    password = input("Enter Your password (integers only): ")
    lst = list(map(int, password))
    magic = functools.reduce(function, lst)
    result = (lambda x: x % 4 == 0)(magic)
    if result:
        print("Correct password!")
    else:
        print("Wrong password.")

    # 16 - Wrong password.
    # 2301 - Wrong password
    # 444 - Wrong password
    # 1234 - Correct password

if __name__ == "__main__":
    main()