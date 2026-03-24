#!/bin/bash

# Вывод заголовка таблицы
printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

# Перебор всех FASTA-файлов
for file in *.fasta; do
    # Если нет файлов, выходим из цикла
    if [ ! -f "$file" ]; then
        continue
    fi

    # Пропускаем пустые файлы (размер 0 байт)
    if [ ! -s "$file" ]; then
        continue
    fi

    # Извлекаем последовательность: убираем заголовки (строки с '>'), удаляем переводы строк и пробелы
    seq=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' ')

    # Преобразуем в верхний регистр для единообразия
    seq=$(echo "$seq" | tr 'a-z' 'A-Z')

    # Подсчёт каждого нуклеотида (количество вхождений)
    a=$(echo "$seq" | grep -o "A" | wc -l)
    t=$(echo "$seq" | grep -o "T" | wc -l)
    g=$(echo "$seq" | grep -o "G" | wc -l)
    c=$(echo "$seq" | grep -o "C" | wc -l)

    # Вывод строки таблицы
    printf "%-15s %-7d %-7d %-7d %-7d\n" "$file" "$a" "$t" "$g" "$c"
done
