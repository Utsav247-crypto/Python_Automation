class Carr:
    car_type_car = "Sedan_car"                 #class attribute
    def __init__(self, abc):
        self.name_car = "1"               #instance attribute
        self.mileage_car = 1         #instance attribute
        self.c_car = 1
        self.abc = abc

    def description_car(self, user):
        print("description_car")
        print(user)
        print(self.name_car)
        print(self.abc)

    def max_speed_car(self, speed):
        print("max_speed_car")

#obj1=Car("ABC")
#obj1.description_car("Utsav")