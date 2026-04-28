-- Увеличение цены на 10% для всех товаров с ценой меньше 1000
UPDATE prices 
SET price = price * 1.10 
WHERE price < 1000;