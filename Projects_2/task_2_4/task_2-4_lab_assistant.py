# Запрос объема раствора
volume_ml = float(input("Введите нужный объем физиологического раствора (мл): "))

# Расчеты
salt_mass = volume_ml * 0.009  # 0.9% концентрация
water_volume = volume_ml       # объем воды ≈ общему объему

# Запись в файл
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-----------------------\n")
    file.write(f"Общий объем:\t{volume_ml} мл\n")
    file.write(f"Масса соли:\t{salt_mass:.2f} г\n")
    file.write(f"Объем воды:\t{water_volume} мл\n")

print("Рецепт сохранен в файл recipe.txt")