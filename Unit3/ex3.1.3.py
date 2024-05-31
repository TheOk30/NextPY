'''
def StopIteration_error():
    #Function that creates a new StopIteration error
    # This error occurs when there are no more items 
    # to be returned by an iterator
    my_list = [1, 2, 3]
    iterator = iter(my_list)
    while True:
        item = next(iterator)
        print(item)

def ZeroDivisionError_error():
    #Function that creates a new ZeroDivisionError error
    # This error occurs when you try to divide a number by 0
    x = 5
    y = 0
    print(x / y)

def AssertionError_error():
    #Function that creates a new AssertionError error
    # This error occurs when an assert statement fails
    assert 1 == 2

def ImportError_error():
    #Function that creates a new ImportError error
    # This error occurs when a module is not found
    import my_module

def KeyError_error():
    #Function that creates a new KeyError error
    # This error occurs when a dictionary key is not found
    my_dict = {"name": "John", "age": 23}
    print(my_dict["city"])

def SyntaxError_error():
    #Function that creates a new SyntaxError error
    # This error occurs when there is a syntax error in the code
    print("Hello, world!"

def IndentationError_error():
    #Function that creates a new IndentationError error
    # This error occurs when there is an indentation error in the code
    for i in range(5):
    print(i)

def TypeError_error():
    #Function that creates a new TypeError error
    # This error occurs when an operation or function is applied to an object of an inappropriate type
    print("Hello" + 5)
'''