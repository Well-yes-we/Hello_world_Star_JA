-- Увеличение цены на 5% для товаров с product_id <= 5 и ценой меньше 10000
UPDATE prices 
SET price = price * 1.05 
WHERE product_id <= 5 AND price < 10000;