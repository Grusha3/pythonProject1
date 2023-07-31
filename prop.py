class Cat:
    __MIN_AGE = 0
    __MAX_AGE = 20
    __MIN_NAME_LEN = 3
    @classmethod
    def __validate_age(cls,value):
        if type(value) != int:
            raise TypeError(f'age need to be integer,getting {value}')
        elif not (cls.__MIN_AGE<= value <= cls.__MAX_AGE):
            raise TypeError (f'age should be beetwen {cls.__MIN_AGE} and {cls.__MAX_AGE}')
        return value
    @classmethod
    def __validate_name(cls,value):
        if not isinstance(value,str):
            raise TypeError (f'name should be str')
        elif len(value) < cls.__MIN_NAME_LEN:
            raise TypeError (f'lengh should be bigger then {cls.__MIN_NAME_LEN}')
        return value

    def __init__(self,name,age):
        self.__name = self.__validate_name(name)
        self.__age = self.__validate_age(age)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__validate_name(name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age = self.__validate_age(value)



    def __str__(self):
        return (f'name:{self.__name},age:{self.__age}')

cat1 = Cat('joe',3)
print(cat1.name)
cat1.name = 'boris'
print(cat1.name)