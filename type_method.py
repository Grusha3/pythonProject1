class Point:
    MIN = -100
    MAX = 100
    def __init__(self,x,y):
        self.x = self.y = 0
        if self.MIN <= x <= self.MAX and type(x)== int:
            self.x = x
        if self.MIN <= y <= self.MAX and type(y)== int:
            self.y = y

    @staticmethod
    def sum_points(p1,p2):
        return Point(p1.x + p2.x,p1.y + p2.y)
    @classmethod
    def validated_some_points(cls,p1,p2):
        result_x = p1.x + p2.x
        result_y = p1.y + p2.y
        return Point(
            result_x if cls.MIN <= result_x <= cls.MAX and isinstance(result_x,int) else cls.MAX,
            result_y if cls.MIN <= result_y <= cls.MAX and isinstance(result_y,int) else cls.MAX
        )

    def __str__(self):
        return f'x:{self.x},y:{self.y}'
point1 = Point(20,50)
point2 = Point(5,88)
print(point2)
print(point1)
point3 = Point.sum_points(point1,point2)
print(point3)
point4 = Point.validated_some_points(point3,point2)
print(point4)
