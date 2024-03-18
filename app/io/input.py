def input_from_console():
    """
    Функція для введення тексту з консолі.
    Returns:
        str: Введений користувачем текст.
    """
    text = input("Введіть текст з консолі: ")
    return text

def input_from_file(filename):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.
    Args:
        filename (str): Назва файлу, з якого потрібно зчитати текст.

    Returns:
        str: Текст, який було зчитано з файлу.
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
    Args:
        filename (str): Назва файлу, з якого потрібно зчитати текст.

    Returns:
        str: Текст, який було зчитано з файлу.
    """
    try:
        import pandas as pd
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

