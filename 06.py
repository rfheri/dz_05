#Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
a = int(input("введите число: "))
if a % 2 == 0:
    print("число четное")
else:
    print("число нечетное")