class ChaiShop:
    def __init__(self, type_, size): #it is same as constructor in class for other program lang.
        self.type_ = type_
        self.size = size

    def summary(self):
        return (f"{self.type_} chai of quantity {self.size}ml.")

order1 = ChaiShop('masala', 200)
order2 = ChaiShop('lemon', 134)
print(order1.summary())
print(order2.summary())

# we can also write in this way.
# print(ChaiShop.summary(order1)) class with method and object as parameter for reference




# Inheritance and Composition
# Inheritance is a way for one class to resuse the feature of another class. The class that gets the feature is called child class and the class with provide the feature is called parent class.
# class Vechile:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def info(self):
#         print(f"Vechile brand is {self.brand} and it runs at speed {self.speed}km/hr.")

# class Car(Vechile):
#     def drive(self):
#         print('Car is driving')

# newCar = Car('Toyota', 120)
# newCar.info()
# newCar.drive()


# Composition means creating a class that uses another class as a part of itself 
# Instead of inheriting features, one class contians object of another calss and uses it 

class BaseVechile:
    def __init__(self, type_):
        self.type = type_

    def vechileType(self):
        print(f"Vechild type is {self.type}")

class Toyota:
    base_car = BaseVechile #Toyota doesn't inherit but this variable has a reference of base class and can use it

    def __init__(self,carType):
        self.car = self.base_car(carType)

    def drive(self):
        print(f"Driving toyota of {self.car.type} type")
        print(self.car)

mycar = Toyota('disel')
mycar.drive()

# Inheritance: “A Car is a Vehicle”. Inheritance is used when there is an “is-a” relationship.
# Composition: “A Car has an Engine”. Composition is used when there is a “has-a” relationship.


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def charge(self):
        print(f'Battery is charging with capacity {self.capacity}')

class Phone:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.battery = Battery(capacity)

    def call(self):
        print(f'Calling from {self.brand}')
        self.battery.charge()

class Nokia(Battery):
    nokia_phone = Phone('no kia', 130) #it is not a object, it is a class itself

# samsung = Phone('samsung', '128gb')
# samsung.call()
nokia = Nokia('150')
nokia.nokia_phone.call()
# “Instead of taking whole features, we are taking reference of another class and store in variable and use in another class”


# Ways to access base class 
class School:
    def __init__(self, type_):
        self.type = type_

class Boarding(School):
    def __init__(self, type_, fees):
        super().__init__(type_) # we can access like his or School.__init(type_)
        self.fees = fees


# MRO -> Method resolution order
class A:
    label = 'A Base class'

class B(A):
    label = 'B inherits A'

class C(A):
    label = 'C inherits A'

class D(B, C):
    pass

# so what will D has a label -> one which is written first like B here 
cup = D()
print(cup.label)



#Static methods in python
# method inside a class that don't use any self or instance of data. it belongs to a class but it doesn't depends on object of class
class MathHelper:
    @staticmethod
    def add(a,b):
        return a+b

    def subtract(a,b):  #this will still work but it is a bad design and may be confusing, not follow proper oops design
        return a-b

print(MathHelper.add(2,3))
print(MathHelper.subtract(2,3)) #python passes the object as first argument automatically



# Instance method → works with a single object
# Class method → works with the class itself, want to create objects in special way
# Static method → works without object or class state. don't have any dependency of object

class Student:
    total = 0
    def __init__(self,name,standard):
        self.name = name
        self.__standard = standard
        Student.total+=1

    @classmethod
    def get_total(cls):
        return cls.total

    @staticmethod
    def subtract(a,b):
        return a-b

    def summary(self):
        print(f'my name is {self.name}')

    @property
    def standard(self):
        return self.__standard

    @standard.setter
    def standard(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__standard = value



student1 = Student('Rohan',3)
student1.summary()
print(Student.total)
print(Student.get_total())
print(student1.standard)



class Employee:
    company = 'Google'
    def __init__(self,salary):
        self._salary = salary

    def company_name(self):
        print(f'Company name is {Employee.company}')

    @staticmethod
    def valid_age(age):
        if age > 18:
            print('valid age')
        else:
            raise AssertionError('Age must be greater than 18')

    @classmethod
    def company_data(cls):
        print(f'company is {cls.company}')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
        print(f'salary set to {value}')


employee1 = Employee(2000)
print(employee1.salary)
employee1.salary = 50
print(employee1.salary)
Employee.company_data()
print(Employee.valid_age(19))