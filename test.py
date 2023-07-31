'''def factorial(n):
    if n!=0:
        return n* factorial(n-1)
    else:
        return 1
print(factorial(5))
'''
import time
from functools import reduce

'''from functools import lru_cache
@lru_cache
def fibonachi(n):
    if n in (1,2):
        return 1
    return fibonachi(n-1) + fibonachi(n-2)
print(fibonachi(50))
'''
#дикаратор это обертка для функции используется для расширения функционала функции без ее изменения
'''def debugger(func):
    def inner(*args,**kwargs):
        print(*args,**kwargs)
        res = func(*args,**kwargs)
        print('function did')
        return res
    return inner
def timer(function):
    def wrapper(*args,**kwargs):
        star = time.time()
        result = function(*args,**kwargs)
        finish = f'Время выполнения{time.time()-star}'
        print(finish)
        return result
    return wrapper


@debugger
@timer
def sum_lst(lst:list)->int:
    return sum(lst)
print(sum_lst([1,4,5,2]))
'''
def plus(a,b): return a + b
print(plus(1,4))

z = lambda a , b:a + b
print(z(4,5))
lst = list(range(50))
new_lst = list(filter(lambda el:el%2,lst))# проверяет на тру или фолс
new_lst2 = list(map(lambda el:el**2,new_lst))#функции с математическими действиями
new_lst3 = reduce(lambda a,b:a+b,new_lst2)
print(new_lst)
print(new_lst2)
print(new_lst3)

