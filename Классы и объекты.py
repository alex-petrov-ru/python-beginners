class Goat:
    legs_number = 4

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __str__(self):
        s = "weight = {}, height = {}".format(self.height, self.weight)
        return s


marusya = Goat(60, 40)
notka = Goat(65, 42)
for x in marusya, notka:
    print(x)

notka.weight += 1

for x in marusya, notka:
    print(x)