import unittest
import main

unittest.TestLoader.sortTestMethodsUsing = None


class TestLibrary(unittest.TestCase):
    # ADD book 1
    def test_test1(self):
        book = main.Books()
        self.assertEqual(book.add_book("Book1", "Author1", "1980"), {'title': "Book1", 'author': "Author1", 'year': "1980", 'status': 0})

    # ADD book 2
    def test_test2(self):
        book = main.Books()
        self.assertEqual(book.add_book("Book2", "Author2", "1950"), {'title': "Book2", 'author': "Author2", 'year': "1950", 'status': 0})

    # List books
    def test_test3(self):
        book = main.Books()
        self.assertEqual(book.allbooks(), {1: {'title': "Book1", 'author': "Author1", 'year': "1980", 'status': 0},
                                           2: {'title': "Book2", 'author': "Author2", 'year': "1950", 'status': 0}})

    # Delete book 1
    def test_test4(self):
        book = main.Books()
        self.assertEqual(book.delete_book(1), {2: {'title': "Book2", 'author': "Author2", 'year': "1950", 'status': 0}})

    # ADD book 3
    def test_test5(self):
        book = main.Books()
        self.assertEqual(book.add_book("Book3", "Author3", "1970"), {'title': "Book3", 'author': "Author3", 'year': "1970", 'status': 0})

    # Find book by year
    def test_test6(self):
        book = main.Books()
        self.assertEqual(book.find_book("3", "97"), [{'title': "Book3", 'author': "Author3", 'year': "1970", 'status': 0}])

    # Find book by title
    def test_test7(self):
        book = main.Books()
        self.assertEqual(book.find_book("1", "b"), [{'title': 'Book2', 'author': 'Author2', 'year': '1950', 'status': 0},
                                                    {'title': 'Book3', 'author': 'Author3', 'year': '1970', 'status': 0}])

    # Change status
    def test_test8(self):
        book = main.Books()
        self.assertEqual(book.change_status(5, 1), False)

    # Change status
    def test_test9(self):
        book = main.Books()
        self.assertEqual(book.change_status(3, 1), {'title': 'Book3', 'author': 'Author3', 'year': '1970', 'status': 1})

    # Funtion return_status
    def test_add(self):
        self.assertEqual(main.return_status(1), 'Выдана')

    # 3 year tests
    def test_year(self):
        self.assertEqual(main.test_year("abc"), False)

    def test_year2(self):
        self.assertEqual(main.test_year("-54"), False)

    def test_year3(self):
        self.assertEqual(main.test_year("2001"), True)
