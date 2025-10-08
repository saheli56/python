class car:
    def set_details(self, model, color):
        self.model = model
        self.color = color

    def show_details(self):
        print(f"Model: {self.model}, Color: {self.color}")
c1 = car()
c1.set_details("BMW", "Black")
c2 = car()
c2.set_details("Audi", "White")
c1.show_details()
c2.show_details()