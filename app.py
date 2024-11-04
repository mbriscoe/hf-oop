import os

os.system("clear")

# CLASSES

# Inheritance
# Polymorphism
# Encapsulation


class Bird:
    # CLASS ATTRIBUTES
    num_birds = 0

    def __init__(self, kind, call):
        # INSTANCE ATTRIBUTES
        self.kind = kind
        self.call = call
        Bird.num_birds += 1

    def describe(self):
        return f"{self.kind} goes {self.call}"


birdA = Bird("Crow", "Caaaaw")
birdB = Bird("Owl", "Twit Twoo")

print(birdA.describe())
print(birdB.describe())
