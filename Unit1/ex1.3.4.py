
def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(''.join(map(lambda char: char if char == ' ' or char == ':' else chr(ord(char) + 2), password)))
    # print the decoded password 
    # create a new string from the password for every character in the password return the same character
    # if it is a space or a colon, otherwise return the character that is two positions to the right
    # of the current character in the ASCII table    

if __name__ == "__main__":
    main()