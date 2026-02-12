# Запрос данных у пользователя
reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))

# Формирование отчета
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

# Вывод отчета в консоль
print(report)

# Запись отчета в файл
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Отчет сохранен в файл inventory.txt")