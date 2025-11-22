# class called Animal. Needs name and species attributes and speak(self) method that returns the sound the animal makes

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return ("Animal sound")
    
# Create a class called Mammal that inherits from the Animal class. Add a method give_birth(self) that prints a message indicating that the mammal has given birth.

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return (f"{self.name} the {self.species} has given birth")
    
### End of Part 1 ###

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return (f"{self.name} the {self.species} is basking in the sun")
    
class Primate(Mammal, Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return (f"{self.name} the {self.species} is climbing trees")
    
class Marsupial(Mammal, Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return (f"{self.name} the {self.species} is carrying its baby")
    
### End of Part 2 ###

reptile1 = Reptile("Noodle", "Ball Python")
reptile2 = Reptile("Slinky", "Western Hognose")
#lion = Mammal("Leo", "Lion", )
bird1 = Bird("Big Bird", "Scary Big", 6)
bird2 = Bird("Mama", "Mother Goose", 3)


class Aviary: # Aviary inherits from Bird and Bird inherits from Animal # Maybe not inherit?

    def __init__(self):
        # super().__init__(self)
        self.birds = []

    # def bird_enclosure(self):
    #     Aviary.birds = [Aviary("Big Bird"), Aviary("Mother Goose")]


class ReptileEnclosure:
# look at the req. and stop overcomplicating it. 
# This class should have an attribute reptiles (instance attribute) that stores a list of reptile instances.
# so it is using composition and just needs to init on self. Then. an "instance att" that stores a list of instances. 
# look at the test. The assertion is that an instance of ReptileEnclosure has an att (reptiles) that has
# a list of reptile. 

    def __init__(self):
        self.reptiles = []
    
