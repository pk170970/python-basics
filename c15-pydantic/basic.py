# Pydantic is important because it turns untrusted input into validated Python objects.

# It is commonly used for:

# API request and response data
# Configuration files
# JSON parsing
# Data validation
# Type-safe application boundaries
# We will use Pydantic v2.

from pydantic import BaseModel, ValidationError

# 1.Basic model
# class User(BaseModel): #User describes the expected data structure
#     name:str
#     age:int

# user1 = User(name = 'ram', age=25)
# user2= User(name = 'ram', age="25") #automatic conversion possible but it has limits, '25a' will throw error as it can't become integer
# print(type(user2.age))

#Validation Error

# try:
#     user3 = User(name="pk", age='hello')
# except ValidationError as e:
#     print(e)


# 2. Typing
# from typing import Optional

# class Employee(BaseModel):
#     name:str #name is required
#     id:int #id is required
#     email: Optional[str] = None #email may be string or None
#     mobile: int | None = None #mobile may be string or None -> modern way to write
#     address: list[str]

# # 3. Nested models
# class Company(BaseModel):
#     cName:str
#     type: Employee

# company1 = Company(
#     cName= 'Lentra',
#     type={
#         "name":"Pratyush",
#         "id": 2701,
#         "address":['Blue ridge', 'Hinjewadi']
#     },
#     )

# # Pydantic converts the nested dictionary into an Address object.

# print(company1.type.address)


# 4. Field -> used for adding constrains and metadata
from pydantic import Field
from typing import Literal

class Car(BaseModel):
    name:str = Field(min_length=5, max_length=20)
    color:Literal['white', 'black', 'green']
    price:float = Field(ge=2500.45, le=2800)

# myCar = Car(name='bmw 3e', color='green', price=3100) will throw validation errror
# print(myCar.price)

# 5. Annotated: It keeps the type and validation rule together
from typing import Annotated
class Voter(BaseModel):
    name:Annotated[str, Field(min_length=5)]
    age: Annotated[int, Field(ge=18, le=120)]


# 6. Field Validators -> It validates or transform one field
from pydantic import field_validator, ValidationInfo

#Field order matters here

# class MobileUser(BaseModel):
#     password:str = Field(min_length=5, max_length=13)
#     confirmPassword:str = Field(min_length=5, max_length=13)

#     @field_validator('confirmPassword') #The validator runs when Pydantic validates confirmPassword.
#     @classmethod
#     def passwordReMatch(cls, value:str, info: ValidationInfo):
#         print(info.data) # Contains fields that Pydantic has already validated. Because password appears before confirm_password, it is available
#         if value != info.data.get('password'):
#             raise ValueError('Password do not match')
#         return value

# user = MobileUser(password='12345', confirmPassword='12345')
# print(user)
# For above example, for comparing multiple fields we have model_validator in pydantic 


# 7. After and before validator
# before validator runs before pydantic type check or conversions, after runs after pydantic validations 

class Boy(BaseModel):
    height: int

    @field_validator('height') # field validator by default has mode="after"
    @classmethod
    def valid_height(cls, value:int) -> int:
        print(value, type(value))
        if value < 130:
            raise ValueError('Height must be greater than 150')
        return value

# rohan = Boy(height='twentywo') # this fails before the after validator as pydantic can't convert string to number
rohan = Boy(height='132') # but this works, we can see integer as 132 because first pydantic validation happen then after validation happen
print(rohan)

#before field validator mostly for cleaning and inspect
class Girl(BaseModel):
    height:int

    @field_validator('height', mode='before')
    @classmethod
    def clean_height(cls, value):
        print(value, type(value))
        if isinstance(value, str):
            return value.strip()
        return value

# neha = Girl(height='thirty') #fails
neha = Girl(height="  20  ") # works fine, log will print string 20 because before field validator runs before pydantic conversion
print(neha)




# 8. Model Validators -> validates relationship between multiple fields
from pydantic import BaseModel, model_validator

class RegisteredUser(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError('Password do not match')
        return self #returning self means complete model passes validation. continue using model

# soham = RegisteredUser(password='abcde', confirm_password='abccc')
# First pydantic validates each individual string, then model validator validates complete model
# print(soham)

# NOTE 
# field_validator:
#     usually classmethod because it receives cls and a field value

# model_validator(mode="after"):
#     instance method because it receives self, the completed model

# model_validator(mode="before"):
#     classmethod because the model instance does not exist yet


# 9. Computed field

from pydantic import computed_field

class Booking(BaseModel):
    nights: int = Field(..., ge=1) #triple dots suggest mandatory
    rate_per_night: float = Field(2000, le=20000)

    @computed_field
    @property #having this property decorator so that it behaves as attribute not method, we can acess as self.total_amount
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night

booking = Booking(nights=2, rate_per_night=3000) # we haven't passed total_amount, it calculates at runtime from price and nights
print(booking.total_amount)
print(booking.model_dump()) #it returns the whole model result in the form of dictonary
print(booking.model_dump_json()) #it returns the whole model result as string


# If we want to convert back dictonary data into pydantic model, then we use model_validate

class Bike(BaseModel):
    max_speed:float
    price:float

data = {
    'id':123, #passing extra parameters are ignored, we can configure as model_config = ConfigDict(extra="forbid") inside Model to throw error for extra fields
    "max_speed": "200",
    "price":"20000",
}

yamah = Bike.model_validate(data)
# yamah = Bike(**data) # we can also expand the dictonary and pass data as well
print(yamah) 


# 10. Serialization
# Converting models into dictonaries , json strings, xmls 
