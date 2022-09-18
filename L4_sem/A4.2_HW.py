from os import system
system('cls')
import utils as check



# 2 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


def prime_factors_number(n):
   i = 2
   list_prime_fact = []
   while 2 * 2 <= n:
       while n % i == 0:
           list_prime_fact.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       list_prime_fact.append(n)
   return list_prime_fact

print('Input a number: ')
n = check.CheckNumber()
print(f'{n} -> {prime_factors_number(n)}')
