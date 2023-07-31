#Задание1
'''lst = [1,2,3,3,4,3,5,'hello','go','go']
lst_1 = []
for i in lst:
    if i not in lst_1:
        lst_1.append(i)
print(lst_1)
'''
#Задание2
'''d = [1,2,3,9,4,5,5,6,7,3,8,9,1,3,]
f = 0
for i in d:
    f += d.count(i)//2
    print(i,'-',d.count(i)//2)
print('пар в списке:', f)
'''
#Задание3
'''c_1 = (35,78,21,37,2,98,6,100,231)
c_2 = (45,21,124,76,5,23,91,234)
s_1 = sum(c_1)
print(s_1)
s_2 = sum(c_2)
print(s_2)
if s_1 > s_2:
    print('сумма больше в кортеже: c_1')
else:
    print('сумма больше в кортеже: c_2')
print('min c_1','-',min(c_1),'номер -',c_1.index(min(c_1))+1)
print('max c_1','-',max(c_1),'номер -',c_1.index(max(c_1))+1)
print('max c_2','-',max(c_2),'номер -',c_2.index(max(c_2))+1)
print('max c_2','-',min(c_2),'номер -',c_2.index(min(c_2))+1)
'''
#задание6
'''lst = [1,2,3,4,5,6,7,8,5,7]
lst_1 = [2,3,4,9,0,6,4]
set_1 = set(lst)
set_2 = set(lst_1)
inter = set_1 & set_2
print(inter)
print(len(inter))
'''
#задание4
'''str1 = "An apple a day keeps the doctor away"
dictionary = {symbol: str1.count(symbol) for symbol in str1}
print(dictionary)
'''
#задание7
'''try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
finally:
    print("Блок try завершил выполнение")
'''






