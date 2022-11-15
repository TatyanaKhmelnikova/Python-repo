#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = input('Введите текст через пробел: ').split(' ')
fragment = 'абв'
new_words = []
for i in words:
    if fragment not in i:
        new_words.append(i)
print(new_words)
