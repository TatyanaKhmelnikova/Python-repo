#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

from random import randint
from collections import Counter

list_inp = [randint(1,10) for _ in range(10)]
print(list_inp)
a = Counter(list_inp)

res_list = []
for i in list(a.keys()):
  if a[i] == 1:
    res_list.append(i)
print(res_list)













#res_list = []

#for item in list_inp:
#    if item not in res_list:
#        res_list.append(item)

#print("Unique elements of the list using append():n")
#print(res_list)


