'''class Cars:
    wheels = 4
    windows = True
    def __init__(self,color,doors=4):
        self.color = color
        self.doors = doors
    def sound (self):
        return 'beeeeeeeeeep!'
class FuelCar(Cars):
    def __init__(self,tank,type_fuel,color,doors=4):
        super().__init__(color,doors)
        self.tank = tank
        self.type_fuel = type_fuel
class Honda(FuelCar):
    __manufacture = 'Honda'
    def __call__(self, *args, **kwargs):
        print(f'марка {self.__manufacture}')
car = Honda(65,'gasoline','blue',0)
car()
print(car._Honda__manufacture)
'''
class DbConnector:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if DbConnector.__instance is None:
            DbConnector.__instance = super().__new__(cls)
        return DbConnector.__instance
    def __init__(self,login,password):
        self.login = login
        self.password = password
    def save (self):
        print('saved')
    def dalete_data(self):
        print('delete')
db_connector1 = DbConnector('admin','guli')
db_connector2 = DbConnector('hoe','***')
db_connector3 = DbConnector('hgs','****')
print(db_connector1)
print(db_connector2)
print(db_connector3)