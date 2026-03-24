#!/bin/bash

echo "Названия товаров:"
awk -F ',' '{print $2}' data.csv

echo
echo "Товары дороже 20 (название и цена):"
awk -F ',' '$3 > 20 {print $2, $3}' data.csv

echo
echo "Общая стоимость всех товаров:"
awk -F ',' '{sum+=$3} END {print sum}' data.csv

