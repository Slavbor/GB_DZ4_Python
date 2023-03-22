# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во
# входном файле грядки.

import random

number = int(input("Введи количество кустов: "))
list = [random.randint(0, 40) for _ in range(number)]
print(list)
maximal_berry = list[0] + list[1] + list[-1]
for i in range(len(list) - 1):
    list = list[1:] + list[:1]
    if list[0] + list[1] + list[-1] > maximal_berry:
        maximal_berry = list[0] + list[1] + list[-1]
print("Максимальное количество ягод: ", maximal_berry)
