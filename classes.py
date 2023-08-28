class Car:
    def __init__(self,color,plate_number,brand,no_of_wheels):
        self.color = color
        self.plate_number = plate_number
        self.brand = brand
        self.no_of_wheels = no_of_wheels
    
    def print_no_wheels(self):
        print(self.no_of_wheels)

    def drive():
        print("The car is moving forward")
    
    def play_music():
        print("The car is na mp3 player")
    

adolph = Car('red',3456,'benz',4)
print(adolph.no_of_wheels())

try:
    pass
except:
    pass
