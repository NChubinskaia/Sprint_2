import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def book_rating_dict():
    books = BooksCollector()
    books.books_rating = {'Процесс': 6, 'Приглашение на казнь': 9, 'Другие берега': 3}
    return books
