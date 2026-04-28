-- 1. 5 самых дорогих записей
SELECT * FROM prices ORDER BY price DESC LIMIT 5;

-- 2. 10 последних добавленных записей
SELECT * FROM prices ORDER BY created_at DESC LIMIT 10;

-- 3. 10 самых дешёвых цен из таблицы prices.
SELECT * FROM prices ORDER BY price ASC LIMIT 10;

-- 4. 10 самых дорогих, пропустить 20
SELECT * FROM prices ORDER BY price DESC OFFSET 20 LIMIT 10;