class Point:
    MIN = -100
    MAX = 100
    DEFAULT = 0
    @classmethod
    def __validate_coordinate(cls,value):
        return value if isinstance(value,int) and cls.MIN <= value <= cls.MAX  else cls.DEFAULT

    def __init__(self,x,y):
        self.__x = self.__validate_coordinate(x)
        self.__y = self.__validate_coordinate(y)
    def  get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    def set_x(self,x):
        self.__x = self.__validate_coordinate(x)
    def set_y(self,y):
        self.__y = self.__validate_coordinate(y)



    def __str__(self):
        return f'x:{self.__x},y:{self.__y}'
point1 = Point(20,50)
point2 = Point(5,88)

print(point1)
point1.x = 100
print(point1)
point1.set_x(50)
point1.set_y(101)
print(point1.get_x(),point1.get_y())