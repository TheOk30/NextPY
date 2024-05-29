class test:
    def __init__(self, a="hello world"):
        self._a = a
    def display(self):
        print(self._a)
obj = test()
obj.display() # hello world