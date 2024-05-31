def read_file(file_name):
    print("__CONTENT_START__")

    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("__NO_SUCH_FILE__")
    finally:
        print("__CONTENT_END__")
def main():
    read_file("Unit1\names.txt")

if __name__ == "__main__":
    main()