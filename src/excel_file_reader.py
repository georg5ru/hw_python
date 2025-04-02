import pandas as pd
import os

try:
    file_path = 'C:\\Users\\Pokhlebin.G\\Downloads\\transactions_excel.xlsx'


    # Проверим существование файла перед чтением
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден. Проверьте путь и имя файла.")

    # Чтение Excel файла
    df = pd.read_excel(file_path)

    # Вывод первых строк для проверки
    print("Данные успешно прочитаны:")
    print(df.head())

except FileNotFoundError as e:
    print(f"Ошибка: {e}")
    print("Убедитесь, что:")
    print("1. Файл существует в указанной директории")
    print("2. Имя файла указано верно (включая расширение .xlsx)")
    print("3. Вы используете правильный путь к файлу")

except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")