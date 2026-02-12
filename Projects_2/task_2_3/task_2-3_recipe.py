# Запрос данных у пользователя
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")

# Запись данных в файл
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n")
    file.write("===========\n")
    file.write(f"• Концентрация агара: {agar_concentration}%\n")
    file.write(f"• Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")