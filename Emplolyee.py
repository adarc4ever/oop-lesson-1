class Employee:
    os = 'linux'
    work_style = 'remote'
    hourly_salary =15

#constructor method
#build object from class

    def __init__(self,role,is_manager) -> None:
        self.role = role
        self.is_manager = is_manager
        pass
 #create object/instance
Marian = Employee('Developer',False)
Bob = Employee('QA',True)

print(Marian.role)
print(Bob.is_manager)
print(Bob.role)