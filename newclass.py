class Car:
    year = 2000
    body_type  = 'Suv'
    engine_type = 'Electric'
    
#constructor method

    def __init__(self,horse_power,number_of_seats,color = 'white') -> None:
        self.horse_power = horse_power
        self.number_of_seats = number_of_seats
        self.color = color

    def bio(self):
        print(f'Hello this is the car with {self.horse_power} and {self.color} color')
#create object/instance
tesla = Car('420_hp',5)
hyundai = Car('295_hp',7)
jeep = Car('340_hp',5,'red')

# check in object belongs t
tesla.bio()
hyundai.bio()
jeep.bio()

# tesla.year = 2022
# cars.year =2018
# print(tesla.year)
# print(jeep.year)