class UsernameContainsIllegalCharacter(Exception):
    # Error for username that Contains Illegal Character
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided username contains illegal characters: %s" % self.message

class UsernameTooShort(Exception):
    # Error for username that is too short
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided username is too short: %s" % self.message

class UsernameTooLong(Exception):
    # Error for username that is too long
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided username is too long: %s" % self.message

class PasswordMissingCharacter(Exception):
    # Error for password that is missing a character
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided password is missing a character: %s" % self.message

class PasswordTooShort(Exception):
    # Error for password that is too short
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided password is too short: %s" % self.message

class PasswordTooLong(Exception):
    # Error for password that is too long
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The provided password is too long: %s" % self.message
class PasswordMissingCharacterUppercase(PasswordMissingCharacter):
    # Error for password that is missing an uppercase character
    def __init__(self, message):
        super().__init__(message)    
    def __str__(self):
        return "The provided password is missing an uppercase character: %s" % self.message

class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    # Error for password that is missing a lowercase character
    def __init__(self, message):
        super().__init__(message)    
    
    def __str__(self):
        return "The provided password is missing a lowercase character: %s" % self.message

class PasswordMissingCharacterNumber(PasswordMissingCharacter):
    # Error for password that is missing a number character
    def __init__(self, message):
        super().__init__(message)    
    
    def __str__(self):
        return "The provided password is missing a number character: %s" % self.message

class PasswordMissingCharacterSpecialCharacter(PasswordMissingCharacter):
    # Error for password that is missing a special character
    def __init__(self, message):
        super().__init__(message)    
    
    def __str__(self):
        return "The provided password is missing a special character: %s" % self.message
    
def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif any(char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_" for char in username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif not any(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in password):
            raise PasswordMissingCharacterUppercase(password)
        elif not any(char in "abcdefghijklmnopqrstuvwxyz" for char in password):
            raise PasswordMissingCharacterLowercase(password)
        elif not any(char in "0123456789" for char in password):
            raise PasswordMissingCharacterNumber(password)
        elif not any(char in "!@#$%^&*()_+=-" for char in password):
            raise PasswordMissingCharacterSpecialCharacter(password)
    except UsernameTooShort as e:
        print(e)
    except UsernameTooLong as e:
        print(e)
    except UsernameContainsIllegalCharacter as e:
        print(e)
    except PasswordTooShort as e:
        print(e)
    except PasswordTooLong as e:
        print(e)
    except PasswordMissingCharacterUppercase as e:
        print(e)
    except PasswordMissingCharacterLowercase as e:
        print(e)
    except PasswordMissingCharacterNumber as e:
        print(e)
    except PasswordMissingCharacterSpecialCharacter as e:
        print(e)
    else:
        print("OK")
        

def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == "__main__":
    main()