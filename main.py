from app.io import input
from app.io import output

def main():
    # Введення тексту з консолі
    text_from_console = input.input_from_console()

    # Введення тексту з файлу за допомогою вбудованих можливостей Python
    text_from_file = input.input_from_file("data/input_file.txt")

    # Введення тексту з файлу за допомогою бібліотеки pandas
    text_from_pandas = input.input_from_file_with_pandas("data/input_file.csv")
    
    # Вивід тексту у консоль
    output.output_to_console(text_from_console)
    output.output_to_console(text_from_file)
    output.output_to_console(text_from_pandas)

    # Запис тексту до файлу за допомогою вбудованих можливостей Python
    output.output_to_file("data/output_file.txt", text_from_console)
    output.output_to_file("data/output_file.txt", text_from_file)
    output.output_to_file("data/output_file.txt", text_from_pandas)

if __name__ == "__main__":
    main()

