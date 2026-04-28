-- 1. Вывести всё
SELECT * FROM products;

-- 2. Вывести название и категортю
SELECT name, category FROM products;

-- 3. Уникальные категории
SELECT DISTINCT category FROM products;

-- 4. Отсортированные по имени
SELECT * FROM products ORDER BY name ASC;

-- 5. В обратном порядке
SELECT * FROM products ORDER BY name DESC;

-- 6. Первые 10 товаров
SELECT * FROM products LIMIT 10;

-- 7. 10 товаров с 11-й записи (индекс с 0)
SELECT * FROM products OFFSET 10 LIMIT 10;

-- 8. 5 случайных
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

-- 9. Категории по алфавиту
SELECT category FROM products ORDER BY category ASC;

-- 10. Товары по категории, потом по названию
SELECT * FROM products ORDER BY category ASC, name ASC;