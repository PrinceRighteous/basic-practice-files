class vehicle: # - This is a class
    def __init__(self,price,color,company,): # - this is the inital/first function/method for a newor every instance/object.
        self.price = price # - this is an attribute/variable
        self.color = color # - this is an attribute/variable
        self.company = company # - this is an attribute/variable
        self.vehicle_name = ["accord","ferrari"]
    def show(self): # - this is a class/object method/function.
        print(self.price)
        print(self.color)
        print(self.company)
        if self.price == 11000:
            return  self.vehicle_name[0]
        elif self.price == 72000:
            return self.vehicle_name[1]
        else:
            return "vehicle name unknown."
    def expensive(self): # - this is a class/object method/function.
        if self.price > 10000:
            return "This car is expensive as HeLL!!"
        elif self.price <= 10000:
            return "this car is kinda Affordable."
        else:
            return "you have not entered a car!"



type = vehicle(11000,"blue","honda") # - this is an instance/object
type2 = vehicle(72000,"black","ferarri") # - this is an instance/object
print(type.price)
print(type.show())
print(type2.show())
print(type2.expensive())