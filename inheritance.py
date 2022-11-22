class Mammal:

    feeds_milk = True

    # def bio():
    #     print('i am a mammal')

class Dog(Mammal):
    legs = 4 
    eyes = 2

    def __init__(self, name,age,breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed
    def bark(self):
        print('Whoof,Woof')
Clifford = Dog('Clifford',2,'Huskie')

print(Mammal.feeds_milk)
print(Dog.feeds_milk)
print(Clifford.feeds_milk)