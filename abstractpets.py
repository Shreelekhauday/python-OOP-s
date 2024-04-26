from zoopark import abstractpets

class Animal(abstractpets):
    def display_details(self):
        print("Animal details:")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
        
class Birds(abstractpets):
    def display_details(self):
        print("Birds details")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
        
class Shree(abstractpets):
    def display_details(self):
        print("Shree details")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
        
