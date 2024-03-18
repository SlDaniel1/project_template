import pandas as pd
def output_to_console(text):
    """
    Функція для виводу тексту у консоль.
    Args:
        text (str): Текст, який потрібно вивести у консоль.
    """
    print(text)

def output_to_file(filename, text):
    """
    Функція для запису тексту до файлу за допомогою вбудованих можливостей Python.
    Args:
        filename (str): Назва файлу, у який потрібно записати текст.
        text (str): Текст, який потрібно записати до файлу.
    """
    try:
        with open(filename, 'a') as file:  # режим додавання до файлу
            if isinstance(text, pd.DataFrame):
                text = text.to_string()  # перетворюємо DataFrame у рядок
            file.write(text + "\n")  # додаємо перенос рядка, щоб розділити тексти
        print(f"Текст успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Виникла помилка при записі у файл '{filename}': {e}")
        