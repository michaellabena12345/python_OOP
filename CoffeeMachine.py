class CoffeeMachine:
    def __init__(self):
        self.water_level = 100

    def brew_coffee(self):
        if self.water_level >= 20: 
            self.water_level -= 20
            print("coffee is ready")
        else:
            print("refill water")
myCoffee = CoffeeMachine()
for i in range(1, 7):
      print(f"attemp {i}: ",end="")
      myCoffee.brew_coffee()

