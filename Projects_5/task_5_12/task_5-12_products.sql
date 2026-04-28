-- 1. Количество товаров в таблице products, сгруппированное по категориям
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

-- 2. Количество товаров в каждой категории, отсортированное по убыванию количества
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category ORDER BY product_count DESC;