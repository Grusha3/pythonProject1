from dataclasses import dataclass,field
class BookMarks:
    def __init__(self,name,surname,telephone,other = []):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.other = other
person1 = BookMarks('Joe','Stalin','18892345',['some_adress','something'])
person2 = BookMarks('Zack','Barison','19895672')
print(person1.other)
#print(person1.name)
@dataclass(frozen=True)
class People:
    name:str
    surname : str
    telephone : str
    age: int = 76
    other : list = field(default_factory=list)


person3 = People('Robin','Good','12345686')
person4 = People('Andrew','Tate','15673423')
print(person3.age == person4.age)
print(person3)
#some = {'name':'joe','surname': 'stalin','telephone': '+12346784','age': 23}
#person6 = People(**some)
#print(person6)
