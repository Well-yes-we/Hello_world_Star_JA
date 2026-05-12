import psycopg2
import pandas as pd

try:
    # Подключаемся к базе данных
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
        database="testdb"
    )

    print("Подключение успешно!")

    # SQL-запрос
    query = """
    SELECT
        p.product_name,
        p.category,
        pr.price,
        pr.price_date
    FROM prices pr
    JOIN products p ON pr.product_id = p.product_id
    """

    # Загружаем данные в DataFrame
    df = pd.read_sql(query, connection)

    # Основная статистика по ценам
    print("Статистика по ценам:")

    print("Средняя цена:", round(df["price"].mean(), 2), "руб.")
    print("Медиана:", round(df["price"].median(), 2), "руб.")
    print("Стандартное отклонение:", round(df["price"].std(), 2), "руб.")
    print("Минимальная цена:", df["price"].min(), "руб.")
    print("Максимальная цена:", df["price"].max(), "руб.")

    # Квартили
    q1 = df["price"].quantile(0.25)
    q2 = df["price"].quantile(0.50)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1

    print("Квартили:")
    print("Q1 =", q1)
    print("Q2 =", q2)
    print("Q3 =", q3)
    print("IQR =", iqr)

    # цена которых выше Q3
    print("Товары с ценой выше Q3:")
    expensive = df[df["price"] > q3]
    print(expensive[["product_name", "category", "price"]])

    # по категориям
    print("Статистика по категориям:")

    by_category = df.groupby("category")["price"].agg(
        ["count", "mean", "median", "std"]
    )

    by_category = by_category.sort_values("mean", ascending=False)

    print(by_category)

    # Разброс цен по товарам
    print("Разброс цен по товарам:")

    by_product = df.groupby("product_name")["price"].agg(
        ["min", "max"]
    )

    by_product["difference"] = by_product["max"] - by_product["min"]

    by_product = by_product.sort_values(
        "difference",
        ascending=False
    )

    print(by_product.head(5))

except Exception as error:
    print("Ошибка:", error)

finally:
    connection.close()
    print("Соединение закрыто.")