class car:
    def set_details(self,model,color):
        self.model=model
        self.color=color
        print(model,color)

car1=car()
car1.set_details("BMW","Black")
car2=car()  
car2.set_details("Audi","White")