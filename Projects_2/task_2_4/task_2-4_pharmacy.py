# Ввод данных
total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите количество капсул в одной упаковке: "))

# Расчет
full_packs = total_capsules // pack_size
remaining_capsules = total_capsules % pack_size

# Вывод отчета
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remaining_capsules}")