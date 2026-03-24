class vehicle:
    def move(self):
        return "The vehicle is moving"
class car(vehicle):
    def carsound(self):
        return "Vroom Vroom"
class bike(vehicle):
    def bikesound(self):
        return "ting ting"
    
vehicles=[car(), bike()]

for v in vehicles:
    print(v.move())