class Mammal:
    def poop(self):
        print("Prprprprp...", end="")


class Cat(Mammal):
    """The Cat class"""

    def __init__(self, name=""):
        self.name = name

    def __str__(self):
        return "Miau."

    def print_hello(self):
        print(f"Hello! I'm {self.name}.")

    # __lt__(self, other):  # <
    # __le__(self, other):  # <=
    # __eq__(self, other):  # ==
    # __ne__(self, other):  # !=
    # __gt__(self, other):  # >
    # __ge__(self, other):  # >=

    def __repr__(self):
        return f"Cat({self.name})"

    def __hash__(self):
        return hash(f"#{self.name.lower()}")

    # def __eq__(self, other): ...

    def __bool__(self):
        return False if self.name == '' else True

    def poop(self):
        super().poop()
        print(" Sorry.")


cat1 = Cat("Mochi")

cat1.print_hello()

print(repr(cat1))

print(hash(cat1))

print(cat1)

cat2 = Cat()

print(f"Cat 1 is {bool(cat1)}.")
print(f"Cat 2 is {bool(cat2)}.")

cat1.poop()
