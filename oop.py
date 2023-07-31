'''dct = {'name':'joe',
       'age':'45'}
print(dct)
class cat:
     #переменные внутри класса назыв поля,а функции называются методами

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'cats name {self.name},{self.age} old'
    def sound (self):
        return f'{self.name},say mey'
cat1 = cat('joe','7')#экзэмпляры
cat2 = cat('olaf','5')#экзэмпляры
cat3 = cat('john','3')#экзэмпляры

print(cat1.name)
print(cat2.name)
print(cat3.name)
print(cat3.sound())
'''
class calculator:
    def plus (self,a,b):
        return a + b
    def minus (self,a,b):
        return a - b
    def mult (self,a,b):
        return a * b
    def delenie (self,a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return a / b
calc = calculator()
print(calc.plus(4,8))
