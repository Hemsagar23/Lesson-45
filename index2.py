class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Shaolin = Parrot("Shaolin", 10)
Ching = Parrot("Ching", 15)

print("Shaolin is a {}".format(Shaolin.species))
print("Ching is also a {}".format(Ching.species))

print("{} is {} years old".format(Shaolin.name, Shaolin.age))
print("{} is {} years old".format(Ching.name, Ching.age))