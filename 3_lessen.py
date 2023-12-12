# Write a program that stores in a dictionary the prices of the fruits in the table, asks
# the user for a fruit, a number of kilos and displays the price of that number of kilos of
# fruit. If the fruit is not in the dictionary, it should display a message informing about
# it.

dict_fruits = {
    "Banana":1.35,
    "Apple":0.80,
    "Pear":0.85,
    "Orange":0.70}

fruit_input = (input("Введите фрукт: ").lower()).capitalize()
kilograms = float(input("Введите количетсво фруктов: "))
if fruit_input in dict_fruits:
    itog = kilograms * dict_fruits[fruit_input]
    print(itog)
else:
    print("Нет такого фрукта")

