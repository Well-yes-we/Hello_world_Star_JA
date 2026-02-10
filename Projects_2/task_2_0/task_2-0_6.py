# Создаем словарь с информацией
my_info = {
    "ФИО": "Старовойтова Юлия Алексеевна",
    "Дата рождения": "10.12.2007",
    "Место рождения": "Норильск",
    "Образование": "Получаю",
    "Специальность": "Технолог",
    "Хобби": "чтение, игры",
    "Контакты": "hsokomilk@gmail.com"
}

# Записываем информацию в файл
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Информация обо мне:\n")
    f.write("=" * 40 + "\n")
    for key, value in my_info.items():
        f.write(f"{key}: {value}\n")

print("Файл output.txt успешно создан!")

# Читаем и выводим содержимое файла для проверки
print("\nСодержимое файла output.txt:")
with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())