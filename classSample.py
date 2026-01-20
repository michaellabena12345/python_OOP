class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def details(self):
        print(f"my smartphone {self.brand}, and model is {self.model}, price is {self.price}")
    
phone = Smartphone("samsung", "S34", 999)
phone.details()