# Ввод последовательности
dna_sequence = input("Введите последовательность ДНК: ").upper()

# Подсчет нуклеотидов
count_A = dna_sequence.count('A')
count_T = dna_sequence.count('T')
count_G = dna_sequence.count('G')
count_C = dna_sequence.count('C')

# Общая длина
total_length = len(dna_sequence)

# Вывод результатов
print("\n=== Анализ последовательности ДНК ===\n")
print(f"Введите последовательность ДНК: {dna_sequence.lower()}")
print(f"\nПоследовательность в верхнем регистре: {dna_sequence}")
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
print(f"\nОбщая длина: {total_length} нуклеотидов")

# Дополнительно: процентное содержание
print("\nПроцентное содержание:")
print(f"A: {count_A/total_length*100:.1f}%")
print(f"T: {count_T/total_length*100:.1f}%")
print(f"G: {count_G/total_length*100:.1f}%")
print(f"C: {count_C/total_length*100:.1f}%")