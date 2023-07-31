from abc import ABC, abstractmethod
class Button(ABC):
    @abstractmethod
    def get_name (self):
        pass

    def on(self):
        print(f'{self.get_name()} work')
    def off(self):
        print(f'{self.get_name()} dont work')

class Lamp(Button):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name
lamp1=Lamp('lighter')
lamp1.on()

class VacCleaner(Button):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
cleaner1 = VacCleaner('Bosch')
cleaner1.on()
#data class
