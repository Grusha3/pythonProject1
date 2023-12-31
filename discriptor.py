class IntegerCoordinate:
    @staticmethod
    def validate_num(num):
        return num if isinstance(num,int) else 0
    def __set_name__(self, owner, name):
        self.name = '__'+ name
    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        return setattr(instance,self.name,self.validate_num(value))
class Point:
    x = IntegerCoordinate()
    y = IntegerCoordinate()
    z = IntegerCoordinate()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
point = Point('1',2,3)
point.x = 20
print(point.x,point.y,point.z)