# Сбор данных
researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# Создание файла с рамкой
with open("journal.txt", "w", encoding="utf-8") as file:
    # Верхняя граница
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| {'Электронный лабораторный журнал':<49}|\n")
    file.write("+" + "-" * 50 + "+\n")
    
    # Основная информация
    file.write(f"| {'ФИО исследователя :':<20} {researcher_name:<29}|\n")
    file.write(f"| {'Дата :':<20} {date:<29}|\n")
    file.write(f"| {'Эксперимент :':<20} {experiment_name:<29}|\n")
    
    # Разделитель
    file.write("+" + "-" * 50 + "+\n")
    
    # Вывод
    file.write(f"| {'Вывод:':<49}|\n")
    file.write(f"| {conclusion:<49}|\n")
    
    # Нижняя граница
    file.write("+" + "-" * 50 + "+\n")

print("Данные успешно сохранены в journal.txt")