#С помощью enumerate перебирать весь список data:

data = [2, 5, 3, 4, 1, 5]
for num, val in enumerate(data, 1):
    print(str(num) + '-ое значение равно ' + str(val))