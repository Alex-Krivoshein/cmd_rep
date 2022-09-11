#Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

float_num = input('Введите число: ')
print(type(float_num))
sum = 0
for i in float_num:
     if i != '.':
         sum += int(i)
print(sum)


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
     factorial *= i
print(factorial, end=' ')


#Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.

n = int(input('Введите число: ')) 

def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
print(round(sum(sequence(n))))


#Задание 5 Реализуйте алгоритм перемешивания списка.

import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 5
lft = -2
rght = 32

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)

