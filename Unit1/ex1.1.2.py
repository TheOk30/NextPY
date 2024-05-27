def letter_repeat(my_char):
    """
    Given a single character, return a string made of 2 of that char.
    """
    return my_char * 2

def double_letter(my_str):
    """
    Given a string, return a string where for every char in the original,
    there are two chars.
    """

    return "".join(map(letter_repeat, my_str))


def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))

    # ppyytthhoonn
    # wwee  aarree  tthhee  cchhaammppiioonnss!!

if __name__ == "__main__":
    main()