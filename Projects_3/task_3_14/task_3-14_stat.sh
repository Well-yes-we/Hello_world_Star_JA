#!/bin/bash

echo "Статистика по оценкам студентов:"

# Сумма оценок
sum=$(awk '{sum+=$2} END {print sum}' students.txt)
echo "Сумма оценок: $sum"

# Средняя оценка (с одним знаком после запятой)
avg=$(awk '{sum+=$2; count++} END {printf "%.1f", sum/count}' students.txt)
echo "Средняя оценка: $avg"

# Максимальная оценка
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $max"

