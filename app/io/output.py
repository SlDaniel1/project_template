def output_to_console(text):
    """
    Функція для виводу тексту у консоль.
    """
    print(text)

def output_to_file(filename, text):
    """
    Функція для запису тексту до файлу за допомогою вбудованих можливостей Python.
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Текст успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Виникла помилка при записі у файл '{filename}': {e}")