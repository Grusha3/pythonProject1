#def hello ():
 #   print('hello world')
#hello()
#hello()
def cat(name,color):
    return f'cat name {name},color {color}'
cat('joe','red')
#cat('мурка','белый')
#cat('феликс','черный')
'''def pluse(a,b):
    result = a + b
    return result
print(pluse(3,7))
'''
from functools import reduce
'''lst = [1,2,3,4,5,6,7]

def sum_lst(l:list)-> int:
    result = 0
    for i in l:
        result += i
    return result
print(sum_lst(lst))
'''
'''def is_year_leap(year:int)-> bool:
    if year % 4 == 0 or (year % 100==0 and year % 400 == 0):
        return True
    else:
        return False
print(is_year_leap(2004))
'''
'''def season(month:int)-> str:
    if month == 12 or month <= 2:
        return 'Winter'
    elif 2<month<=5:
        return 'spring'
    elif 5<month<= 8:
        return 'summer'
    elif 8 < month <=11:
        return 'Autum'
print(season(int(input())))
'''
'''from math import sqrt
def square(a:int)->dict:
    perimetr = 4 * a
    space = a**2
    diagonal = sqrt(a)
    return {'perimetr':perimetr,'space':space,'diagonal':diagonal}
print(square(int(input())))
'''


