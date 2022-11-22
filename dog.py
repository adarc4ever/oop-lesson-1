from common.mammal import Mammal,message,say_hello

class Dog(Mammal):
    legs = 4 
    eyes = 2

    def __init__(self, name,age,breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed
    def bark(self):
        print('Whoof,Woof')

    @staticmethod 
    def walk():
        print('Iam walking')

Clifford = Dog('Clifford',2,'Huskie')

# print(Mammal.feeds_milk)
# print(Dog.feeds_milk)
# print(Clifford.feeds_milk)
# print(message)
Dog.walk()
Clifford.walk()
