'''
class Car:
    print("Car")
obj1=Car
print(obj1)

#output - "<class '__main__.Car'>"
'''

'''
class Car:
    car_type = "Sedan"                 #class attribute
    def __init__(self, name, mileage):
        self.name = name               #instance attribute
        self.mileage = mileage         #instance attribute
        self.c = 1

    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"

obj2 = Car("Honda City",24.1)
print(obj2.description())
print(obj2.max_speed(150))

output:
The Honda City car gives the mileage of 24.1km/l
The Honda City runs at the maximum speed of 150km/hr
'''

class Car:
    car_type = "Sedan"                 #class attribute
    def __init__(self):
        self.name = 1               #instance attribute
        self.mileage = 1         #instance attribute
        self.c = 1

    def description(self):
        print("description")

    def max_speed(self, speed):
        print("max_speed")

test=Car()
print(test) #Object banane ke bad uske andar ke methods access kar sakte
test.description()
print(Car.car_type) #Agar class me koi cheez defined hai to usko sida class name se access kar skte
