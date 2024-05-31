try:
    if '1' != 1:
        raise "SomeError"
    else:
        print("SomeError has not occurred")
except "someError":
    print("SomeError has occurred")

# התוכנית תקרוס בגלל קוד לא תקין.