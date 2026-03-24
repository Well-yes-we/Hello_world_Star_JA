#!/bin/bash

echo "Создание файлов:"
# Цикл for для создания файлов test1.txt ... test10.txt
for i in {1..10}; do
    touch "test$i.txt"
    echo "  создан test$i.txt"
done

echo
echo "Удаление файлов в обратном порядке:"
# Цикл while для удаления файлов от test10.txt до test1.txt
i=10
while [ $i -ge 1 ]; do
    rm "test$i.txt"
    echo "  удалён test$i.txt"
    ((i--))
done

echo
echo "Готово."
