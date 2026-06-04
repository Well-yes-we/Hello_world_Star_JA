# task_7_data_analysis.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# 1. Подключение к БД
DB = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'port': os.getenv('DB_PORT', '5435'),
    'dbname': os.getenv('DB_NAME', 'student'),
    'user': os.getenv('DB_USER', 'postgres_task'),
    'password': os.getenv('DB_PASSWORD', 'student')
}

try:
    conn = psycopg2.connect(**DB)
    # 2. Запрос и загрузка в DataFrame
    df = pd.read_sql("""
        SELECT p.price, pr.category 
        FROM prices p
        JOIN products pr ON p.product_id = pr.id
        WHERE p.price IS NOT NULL
    """, conn)
    conn.close()
    print("✓ Данные загружены из БД")
except Exception as e:
    print("ПОДКЛЮЧЕНИЕ НЕ УДАЛОСЬ, ПОПРОБУЙ ЗАПУСТИТЬ ДОКЕР, ПОТОМ ЗАПУСТИТЬ BAT ФАЙЛ", e)
    exit(1)
# 3. Визуализация
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# График 1: Гистограмма + статистика
m, med = df['price'].mean(), df['price'].median()
ax[0].hist(df['price'], bins=20, edgecolor='black', alpha=0.7)
ax[0].axvline(m, color='r', ls='--', label=f'Среднее: {m:.0f}')
ax[0].axvline(med, color='g', ls='--', label=f'Медиана: {med:.0f}')
ax[0].set_title('Распределение цен'); ax[0].legend(); ax[0].grid(alpha=0.3)

# График 2: Boxplot по категориям
df.boxplot(column='price', by='category', ax=ax[1])
ax[1].set_title('Цены по категориям'); ax[1].set_xlabel('')

plt.suptitle('Анализ данных БД', y=1.05)
plt.tight_layout()
plt.savefig('plots.png', dpi=150)
print("✓ Графики сохранены: plots.png")

# 4. Выводы и аномалии
Q1, Q3 = df['price'].quantile(0.25), df['price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['price'] < Q1 - 1.5*IQR) | (df['price'] > Q3 + 1.5*IQR)]

print("\n=== ВЫВОДЫ ===")
print(f"1. Записей: {len(df)} | Среднее: {m:.2f}₽ | Медиана: {med:.2f}₽")
print(f"2. Аномалии (IQR метод): {len(outliers)} шт.")
if len(outliers): print("   Значения:", outliers['price'].tolist())
else: print("   Аномалии не обнаружены.")
print("3. По категориям:")
for cat, grp in df.groupby('category'):
    print(f"   • {cat}: медиана={grp['price'].median():.0f}₽, кол-во={len(grp)}")