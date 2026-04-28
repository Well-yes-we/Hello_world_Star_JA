-- Количество поставщиков для каждого товара (группировка по product_id)
SELECT product_id, COUNT(*) AS supplier_count FROM suppliers GROUP BY product_id;