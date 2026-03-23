# oop
from pyscript import display, document


# creating the class
class Section:
    def __init__(self, numstudents, name, level, adviser):
        # attributes . . .
        self.numstudents = numstudents
        self.name = name
        self.level = level
        self.adviser = adviser


# intantiating an object
section1 = Section(24, 'Topaz', 10, 'Mr. Cortez')
section2 = Section(25, 'Sapphire', 10, 'Mr. De Guzman')

display(f'{section1.level} {section1.name} (adviser: {section1.adviser}), with {section1.numstudents} players, is part of red bulldogs.', target='output1')
display(f'{section2.level} {section2.name} (adviser: {section2.adviser}), with {section2.numstudents} players, is part of green hornets.', target='output2')


class Dog:
    def __init__(self, breed, age, name, owner):
        self.breed = breed
        self.age = age
        self.name = name
        self.owner = owner


    def bark(self): # creating a method
        display('arf '*3, target='output3')


dog1 = Dog('Shih Tzu', 2, 'Chewey', 'Ivy')
dog2 = Dog('American Bully', 1, 'Mari', 'Sky')
dog1.bark()

display(f'{dog1.name} is an {dog1.breed}. It was {dog1.age} years old and owned by {dog1.owner}.', target='output3')
display(f'{dog2.name} is an {dog2.breed}. It is {dog2.age} years old and owned by {dog2.owner}.', target='output3')

# creating a child class
class GermanShepherd(Dog):
    pass

dog1 = GermanShepherd('German Shepherd', 10, 'Jack', 'Sim')

display(f'{dog1.name} is an {dog1.breed}. It is {dog1.age} years old and owned by {dog1.owner}.', target='output3')

class User(Dog):
    pass

def userdoginfo(e):
    document.getElementById('output4').innerHTML = ''
    Username = document.getElementById('input1').value
    Userdogname = document.getElementById('input2').value
    Userdogage = document.getElementById('input3').value
    Userdogbreed = document.getElementById('input4').value

    dog1 = User(Userdogbreed, Userdogage, Userdogname, Username)
    display(f'{dog1.name} is an {dog1.breed}. It is {dog1.age} years old and owned by {dog1.owner}.', target='output4')
