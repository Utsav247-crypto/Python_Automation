from Test_Cases.utsav1 import Carr

class Bus:
    drain = "ABCD"
    test = Carr(drain)
    bus_type_bus = "Sedan_Bus"                 #class attribute

    def description_bus(self):
        #obj1 = Car()
        #obj1.description_car("Utsav")
        #Car.description_car(self, "Utsav")
        self.test.description_car("utsav")
        #print (Car.car_type_car)
        print("description_bus")

    def max_speed_bus(self, speed):
        print("max_speed_bus")


bus=Bus()
bus.description_bus()
