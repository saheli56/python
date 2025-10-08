class character:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
    def show(self):
        print(f"name: {self.name}, age: {self.age}, power: {self.power}")
c1 = character("goku", 24, "Kamehameha")
c2 = character("vegeta", 26, "Galick Gun")
c1.show()
c2.show()
    
    