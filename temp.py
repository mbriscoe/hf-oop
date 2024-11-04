class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "A bird thingy!"

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        parrot = "Norwegian Blue"

        if self.kind[0].upper() in ("A", "E", "I", "O", "U"):
            pre = "An"
        else:
            pre = "A"

        return f"{pre} {self.kind} goes {self.call}"


class BigBird(Bird):

    def __init__(self, kind, call, wingspan):
        self.wingspan = wingspan
        super().__init__(kind, call)

    def description(self):
        if self.kind[0].upper() in ("A", "E", "I", "O", "U"):
            pre = "An"
        else:
            pre = "A"

        return f"{pre} {self.kind} goes {self.call} and has a wingspan of {self.wingspan} feet!"


owl = Bird('Owl', 'Twit Twoo!')
crow = Bird("Crow", "Caaw")
eagle = BigBird("Eagle", "Screeeech!", "10")


print(eagle.description())
print(owl.description())
