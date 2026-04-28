
-- 1. Все товары категории «Электроника»
SELECT * FROM products WHERE category = 'Электроника';

-- 2. Товары категории «Одежда» со словом «женские» в названии
SELECT * FROM products WHERE category = 'Одежда' AND name ILIKE '%женские%';

-- 3. Товары категорий «Продукты» или «Книги»
SELECT * FROM products WHERE category IN ('Продукты', 'Книги');

-- 4. Все товары, кроме категории «Бытовая техника»
SELECT * FROM products WHERE category != 'Бытовая техника';

-- 5. Товары категорий: «Электроника», «Одежда», «Книги»
SELECT * FROM products WHERE category IN ('Электроника', 'Одежда', 'Книги');

-- 6. Сложное условие: (Электроника и Samsung) ИЛИ (Бытовая техника)
SELECT * FROM products 
WHERE (category = 'Электроника' AND name ILIKE '%Samsung%') 
   OR category = 'Бытовая техника';

-- 7. Супер-сложное условие: 
-- ((Электроника/Одежда/Быт.техника) AND id 1-15 AND не Samsung) ИЛИ (Книги)
SELECT * FROM products 
WHERE (
    category IN ('Электроника', 'Одежда', 'Бытовая техника') 
    AND id BETWEEN 1 AND 15 
    AND name NOT ILIKE '%Samsung%'
) 
OR category = 'Книги';