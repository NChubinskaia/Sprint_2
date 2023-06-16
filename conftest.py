import pytest

from main import BooksCollector


@pytest.fixture()
def book_rating_dict():
    books = BooksCollector()
    return books
