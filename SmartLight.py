class SmartLight:
    def __init__(self):
        self.is_on = False
    def toggle(self):
       self.is_on = not self.is_on 
    def status(self):
        if self.is_on:
            print("the light is on")
        else:
            print('the light is off')

light = SmartLight()
light.status()
light.toggle()
light.status()