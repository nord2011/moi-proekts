print("Угадайте, что я загадал: камень, ножницы или бумагу?")
comand = input("Введите <<камень>>, <<ножницы>> или <<бумага>>")

while comand != "камень" and comand != "ножницы" and comand != "бумага" and comand:
    print("Верный ввод!")
    comand = input("Введите <<камень>>,  <<ножницы>> или <<бумага>>")

if comand == "камень":
    print("Угадали!")
else:
    print("Не угадали!")