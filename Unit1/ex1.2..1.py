def main():
    a = lambda x: 1
    print(a(3)) # 1
    print(a("s")) # 1
    print(a(2)) # 1
    print(type(a(3))) # <class 'int'>

if __name__ == "__main__":
    main()