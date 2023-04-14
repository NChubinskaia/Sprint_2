import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_book_already_in_dict_dict_not_changes(self, book_rating_dict):
        book_rating_dict.add_new_book('Процесс')
        assert 'Процесс' in book_rating_dict.books_rating and len(book_rating_dict.books_rating) == 3

    def test_set_book_rating_valid_rating8_rating_changes(self, book_rating_dict):
        book_rating_dict.set_book_rating('Процесс', 8)
        assert book_rating_dict.books_rating['Процесс'] == 8

    def test_set_book_rating_zero_rating_not_change_rating(self, book_rating_dict):
        book_rating_dict.set_book_rating('Процесс', 0)
        assert book_rating_dict.books_rating['Процесс'] == 6

    def test_get_book_rating_rating6_true(self, book_rating_dict):
        assert book_rating_dict.get_book_rating('Другие берега') == 3

    def test_get_books_with_specific_rating_rating9_book_in_list(self, book_rating_dict):
        rating = 9
        assert 'Приглашение на казнь' in book_rating_dict.get_books_with_specific_rating(rating)

    def test_get_books_with_specific_rating_no_reting_empty_list(self, book_rating_dict):
        rating = 5
        assert len(book_rating_dict.get_books_with_specific_rating(rating)) == 0

    def test_get_books_rating_shows_dict(self, book_rating_dict):
        assert book_rating_dict.get_books_rating() == book_rating_dict.books_rating

    def test_add_book_in_favorites_one_new_book_in_favorites_true(self, book_rating_dict):
        book_rating_dict.add_book_in_favorites('Процесс')
        assert 'Процесс' in book_rating_dict.favorites and len(book_rating_dict.favorites) == 1

    def test_delete_book_from_favorites_true(self, book_rating_dict):
        book_rating_dict.add_book_in_favorites('Процесс')
        book_rating_dict.add_book_in_favorites('Другие берега')
        book_rating_dict.delete_book_from_favorites('Другие берега')
        assert 'Другие берега' not in book_rating_dict.favorites and len(book_rating_dict.favorites) == 1

    def test_delete_book_from_favorites_book_not_in_list_list_not_changes(self, book_rating_dict):
        book_rating_dict.add_book_in_favorites('Процесс')
        book_rating_dict.delete_book_from_favorites('Другие берега')
        assert 'Процесс' in book_rating_dict.favorites and len(book_rating_dict.favorites) == 1

    def test_get_list_of_favorites_books_true(self, book_rating_dict):
        book_rating_dict.add_book_in_favorites('Процесс')
        book_rating_dict.add_book_in_favorites('Другие берега')
        assert 'Процесс' in book_rating_dict.favorites and 'Другие берега' \
               in book_rating_dict.favorites and len(book_rating_dict.favorites) == 2
