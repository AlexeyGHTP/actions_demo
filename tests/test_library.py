from src.library import Library, PrintedBook, User


def test_lend_and_return():
    lib = Library()
    book = PrintedBook("Тест", "Автор", 2020, 100, "хорошая")
    user = User("Анна")

    lib.add_book(book)
    lib.add_user(user)

    assert book.is_available() is True
    assert lib.lend_book("Тест", "Анна") is True
    assert book.is_available() is False
    assert lib.return_book("Тест", "Анна") is True
    assert book.is_available() is True
