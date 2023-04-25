import os

while True:
    # Запитуємо користувача про шлях до файлу
    filepath = input("Enter the file path: ")

    # Перевіряємо чи файл існує
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Try again...".format(filepath))
        continue

    # Відкриваємо файл і читаємо його рядки
    with open(filepath) as file:
        lines = file.readlines()

    # Ініціалізуємо лічильники
    total_lines = len(lines)
    empty_lines = 0
    lines_with_z = 0
    z_count = 0
    lines_with_and = 0

    # Обчислюємо статистику
    for line in lines:
        if line.strip() == "":
            empty_lines += 1
        if "z" in line:
            lines_with_z += 1
            z_count += line.count("z")
        if "and" in line:
            lines_with_and += 1

    # Виводимо статистику
    print("File: {}".format(filepath))
    print(" total lines: {}".format(total_lines))
    print(" empty lines: {}".format(empty_lines))
    print(" lines with \"z\": {}".format(lines_with_z))
    print(" \"z\" count: {}".format(z_count))
    print(" lines with \"and\": {}".format(lines_with_and))

    # Питаємо користувача чи хоче він продовжувати
    choice = input("Do you want to analyze another file? (y/n): ")
    if choice.lower() != "y":
        break




