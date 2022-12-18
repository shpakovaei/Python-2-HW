# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число '))
list = []
for i in range (1, n+1):
    x = (1+1/i) **i
    list.append (round (x,2))
print (list)
print ('Сумма =', round (sum(list),2))
