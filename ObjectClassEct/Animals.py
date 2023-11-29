def main():
    # parent Animal class with a type and species
    class Animal:
        def __init__(self,type, species) -> None:
            self.type  = type
            self.species = species
        # a function for what the animal might sound like
        def noise(self) -> str:
            return "..."
        def __str__(self) -> str:
            return f"{self.species}({self.type})"
    # child Dog class to Animal with a type,species,and name
    class Dog(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
        # overrides parent animal sound function
        def noise(self) -> str:
            return f"{self.name}: BARK!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    # child Lizard class to Animal with a type,species,and name
    class Lizard(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
            # overrides parent animal sound function
        def noise(self) -> str:
            return f"{self.name}: HISSSSSS!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    # child Goldfish class to Animal with a type,species, and name
    class Goldfish(Animal):
        def __init__(self, type, species, name) -> None:
            super().__init__(type, species)
            self.name = name
        # overreds parent animal sound function
        def noise(self) -> str:
            return f"{self.name}: BLUB!"
        def __str__(self) -> str:
            return super().__str__() + "\nName: " + str(self.name)
    # prints info about each animal
    a = Animal("Amphibian", "Frog")
    print(a)
    b = Dog("Mammal","Dog","Spike")
    print(b)
    c = Lizard("Reptile", "Lizard", "Lizzy")
    print(c)
    d = Goldfish("Fish", "Goldfish", "Shiny")
    print(d)
    # print what sound each animal would make
    for i in [a,b,c,d]:
        print(i.noise())

if __name__ == '__main__':
    main()