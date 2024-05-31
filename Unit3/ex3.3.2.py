class underAgeError(Exception):

    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "Provided age %s is not 18 or above." % self._arg

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise underAgeError(age)
    except underAgeError as e:
        print(e)
    else:
        print("Invitation sent to %s" % name)
        
def main():
    send_invitation("John", 20)
    send_invitation("Alice", 17)

if __name__ == "__main__":
    main()