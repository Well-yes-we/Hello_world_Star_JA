seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for sequence in seq:
    print(sequence)          # выводим последовательность целиком
    for letter in sequence:  # перебираем каждый символ
        print(letter)        # выводим символ на отдельной строке

print("Цикл выполнен")