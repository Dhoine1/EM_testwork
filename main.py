class Books:
    # Read library from file in JSON format
    # При создании объекта, читается строка из файла library.txt и преобразуется в JSON, либо создается
    # пустой словарь, если файл пуст.
    def __init__(self):
        self.search_field = ""       # переменная для функции поиска
        with open("library.txt", "r") as f:
            try:
                self.library = eval(f.readline())
            except:
                self.library = {}

    # Create new book
    # Находит максимально возможный ID у книг через set и добавляет 1 к создаваемому объекту, для пустого списка
    # индекс равен 1. Затем создает новую запись в библиотеке, используя полученные данные
    def add_book(self, name: str, author: str, year: str) -> dict:
        try:
            index = max(set(self.library.keys()))
        except:
            index = 0
        self.library[index + 1] = {'title': name, 'author': author, 'year': year, 'status': 0}
        write_file(self.library)        # функция записи изменений в файл
        print('\nКнига добавлена успешно\n')
        return self.library[index+1]    # нужно для тестов

    # Delete book by ID
    # По полученному ID либо находит книгу в библиотеке и удаляет её, либо сообщает, что не найдено такой книги,
    # либо, что книг совсем не найдено
    def delete_book(self, id: int) -> dict:
        try:
            if id in self.library.keys():
                del self.library[id]
                write_file(self.library)
                print('\nКнига удалена успешно\n')
            else:
                print("Книги с таким ID не найдено")
        except:
            print("Книг не найдено")
        return self.library         # нужно для тестов

    # Find book by srting
    # Принимает поле по которому будет проведен поиск и фрагмент строки поиска.
    # Перебирает библиотеку, и если что-то найшлось - выводит на экран
    def find_book(self, field: str, text: str) -> list:
        if field == "1":
            self.search_field = 'title'
        elif field == "2":
            self.search_field = 'author'
        elif field == "3":
            self.search_field = 'year'
        found_books = []  # нужно для тестов
        for i in self.library:
            if str(self.library[i][self.search_field]).lower().find(text.lower()) >= 0:
                found_books.append(self.library[i])      # нужно для тестов
                print(f'ID: {i}, Название: {self.library[i]["title"]}, Автор: {self.library[i]["author"]},'
                      f'  Год выхода: {self.library[i]["year"]}, Статус: {return_status(self.library[i]["status"])}')
        return found_books   # нужно для тестов

    # Print all books
    # Перебирает всю библиотеку и выводит на экран построчно
    def allbooks(self) -> dict:
        for i in self.library:
            print(f'ID: {i}, Название: {self.library[i]["title"]}, Автор: {self.library[i]["author"]},'
                  f'  Год выхода: {self.library[i]["year"]}, Статус: {return_status(self.library[i]["status"])}')
        return self.library     # нужно для тестов

    # Change book status by ID
    # Принимает ID и нужный статус, если ID есть в библиотеке, меняет статус книги.
    # Если не нашел, то сообщает об этом. Если книг совсем нет, тоже сообщает.
    def change_status(self, id: int, status: int) -> dict or bool:
        try:
            if id in self.library.keys():
                self.library[id]["status"] = status
                write_file(self.library)
                print('\nСтатус изменен успешно\n')
                return self.library[id]   # нужно для тестов
            else:
                print("Книги с таким ID не найдено")
                return False    # нужно для тестов
        except:
            print("Книг не найдено")
            return False    # нужно для тестов


# Write library in file. JSON format
# Сохранияет полученную переменную в файл, перезаписывая его
def write_file(text: dict) -> None:
    with open("library.txt", "w") as f:
        f.write(str(text))


# Convert the status into an understandable format
# Для вывода на экран, для читаемости, меняет статус 0,1 на "выдана","в наличии"
def return_status(status: int) -> str:
    return "В наличии" if status == 0 else "Выдана"


# Test typed year. Number and <= 2024
# проверяет, что введенный год является числом и меньше либо равен текущему
def test_year(year: str) -> bool:
    return True if year.isdigit() and int(year) <= 2024 else False


if __name__ == "__main__":
    book = Books()
    # циклим работу
    while True:
        # печать меню и выбор пункта
        print("\n\nЭЛЕКТРОННАЯ БИБЛИОТЕКА \n1 - Добавить книгу \n2 - Удалить книгу\n3 - Поиск книги"
              "\n4 - Отображение всех книг \n5 - Изменение статуса книги \n6 - Выход\n")
        variant = input("Введите номер пункта: ")

        # Добавление книги. Проверяется корректность ввод года до вызова метода.
        if variant == "1":
            print('\nДОБАВИТЬ КНИГУ:')
            name = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год выхода книги: ")
            book.add_book(name, author, year) if test_year(year) else print("\nВведен некорректный год\n")

        # Удаление года. Проверяется корретность ввоода ID (цифра > 0)
        elif variant == "2":
            print('\nУДАЛИТЬ КНИГУ:')
            name = input("Введите id книги: ")
            book.delete_book(int(name)) if str(name).isdigit() and int(name) > 0 else print("\nID должен быть положительным числом\n")

        # Поиск книги. Проверяется корректность года при выборе пункта 3 и то, что введено одно из
        # возможных значений
        elif variant == "3":
            print('\nПОИСК КНИГИ:')
            field = input("Будете искать по:\n 1 - Названию \n 2 - Автору \n 3 - Году выхода: ")
            if field not in ['1', '2', '3']:
                print("Статус введен неверно")
                continue
            find_text = input("Введите строку поиска: ")
            if field == "3" and not test_year(find_text):
                print("Год введен некорректно")
                continue
            book.find_book(field, find_text)

        # Вывод на экран всех книг библиотеки
        elif variant == "4":
            print('\nВСЕ КНИГИ:')
            book.allbooks()

        # Изменение статуса книги. Проверяется корректность ввода ID и то, что статус выбран
        # из возможных вариантов
        elif variant == "5":
            print('\nИЗМЕНИТЬ СТАТУС КНИГИ:')
            name = input("Введите id книги: ")
            if not str(name).isdigit() or int(name) < 0:
                print("\nID должен быть положительным числом\n")
                continue
            status = input("Введите новый статус книги:\n 1 - Выдана \n 0 - В наличии: ")
            book.change_status(int(name), int(status)) if status in ['1', '0'] else print("Статус введен неверно")

        # Выход из программы
        elif variant == "6":
            break
        else:
            print("\nВведеный вариант недоступен")
