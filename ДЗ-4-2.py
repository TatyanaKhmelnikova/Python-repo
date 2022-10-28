#Задайте натуральное число N.
#Напишите программу, которая составит список простых множителей числа N

number = int(input("Integer: "))
a = []
for i in range(2, number):
    if number % i == 0:
        a.append(i)
print(a)