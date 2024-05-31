def divider(a, b):
    try:
        result = a / b
        print(result)
    except ArithmeticError :
        print("print me!")
    except ZeroDivisionError:
        print("don't print me!")
divider(5, 0) # print me!