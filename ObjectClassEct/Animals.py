def main():
    class Animal:
        def __init__(self,type, species) -> None:
            self.type  = type
            self.species = species
        def noise(self) -> str:
            return "..."
        def __str__(self) -> str:
            return f"{self.species}({self.type})"
    class Dog(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
        def noise(self) -> str:
            return f"{self.name}: BARK!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    class Lizard(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
        def noise(self) -> str:
            return f"{self.name}: HISSSSSS!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    class Goldfish(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
        def noise(self) -> str:
            return f"{self.name}: BLUB!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    a = Animal("Amphibian", "Frog")
    print(a)
    b = Dog("Mammal","Dog","Spike")
    print(b)
    c = Lizard("Reptile", "Lizard", "Lizzy")
    print(c)
    d = Goldfish("Fish", "Goldfish", "Shiny")
    print(d)
    for i in [a,b,c,d]:
        print(i.noise())

if __name__ == '__main__':
    main()