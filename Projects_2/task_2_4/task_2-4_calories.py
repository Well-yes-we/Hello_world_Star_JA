# Ввод данных
protein = float(input("Масса белков в продукте (г): "))
fat = float(input("Масса жиров в продукте (г): "))
carbohydrates = float(input("Масса углеводов в продукте (г): "))

# Расчет калорийности
calories = (protein * 4) + (fat * 9) + (carbohydrates * 4)

# Вывод результата
print(f"Калорийность продукта: {calories:.2f} ккал")