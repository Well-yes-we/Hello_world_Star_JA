-- 1. Количество записей в таблице prices для каждого товара
SELECT product_id, COUNT(*) AS price_records_count FROM prices GROUP BY product_id;

-- 2. Средняя цена товаров для каждого product_id
SELECT product_id, AVG(price) AS average_price FROM prices GROUP BY product_id;

-- 3. Минимальная цена для каждого товара
SELECT product_id, MIN(price) AS min_price FROM prices GROUP BY product_id;

-- 4. Максимальная цена для каждого товара
SELECT product_id, MAX(price) AS max_price FROM prices GROUP BY product_id;