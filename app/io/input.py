def input_from_console():
    """
    Функція для введення тексту з консолі.
    """
    text = input("Введіть текст з консолі: ")
    return text

def input_from_file(filename):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

def input_from_file_with_pandas(filename):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.
    """
    try:
        import pandas as pd
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

