class A:
    def one(self):
        return self.two()
    def two(self):
        print('A')
class B(A):
    def two(self):
        print('B')
def main():
    my_object = B()
    my_object.two()
main()

# output B