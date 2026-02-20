from datetime import datetime

# Фиксированная дата взятия образца (например, 15 марта 2025 года)
sample_date = datetime(2025, 3, 15)

# Список файлов
files = ["seq1", "seq2.fasta", "seq3.fa", "seq4"]

print(f"Дата взятия образца: {sample_date.strftime('%d.%m.%Y')}\n")

for name in files:
    if name.endswith((".fasta", ".fa")):
        print(f"{name} уже имеет расширение")
    else:
        new_name = name + ".fasta"
        print(f"{new_name}")