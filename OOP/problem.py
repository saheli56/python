class student:
    def seld_details(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print(f"Name:{self.name},Age:{self.age}")
s1=student()
s1.seld_details("Alice",20)
s2=student()    
s2.seld_details("Bob",22)
s1.display_details()
s2.display_details()