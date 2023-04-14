# qa_python
## Сlass BookCollector. Unit-test description

1. **test_add_new_book_add_two_books** </br>
*при добавлении в двух книг в словарь с помощью метода add_new_book() - 
в словарь записано именно 2 книги, словарь books_rating имеет длину 2*


2. **test_add_new_book_book_already_in_dict_dict_not_changes** </br>
*при попытке добавить книгу, которая уже есть в словаре, 
длина словаря не изменяется и книга по-прежнему остается в словаре*


3. **test_set_book_rating_rating8_rating_changes** </br>
*при использовании валидного значения (от 1 до 10) в методе set_book_rating(),
рейтинг соответствующей книги изменяется в словаре*


4. **test_set_book_rating_zero_rating_not_change_rating** </br>
*при использовании невалидного значения (например, 0) в методе set_book_rating(),
рейтинг соответствующей книги **не** изменяется в словаре*


5. **test_get_book_rating_rating6_true** </br>
*при вызове метода get_book_rating() с коррекным аргументом (названием книги, 
которая есть в словаре), выведенный рейтинг соответствует рейтингу книги, 
записанному в словаре*


6. **test_get_books_with_specific_rating_rating9_book_in_list** </br>
*при вызове метода get_books_with_specific_rating() с коррекным аргументом
(рейтингом, который есть в словаре), соответствующая книга записывается в список*


7. **test_get_books_with_specific_rating_no_reting_empty_list** </br>
*при вызове метода get_books_with_specific_rating() и некоррекного аргумента
(рейтинга, которого нет в словаре), 
соответствующая книга **не** записывается в список, длина списка = 0*


8. **test_get_books_rating_shows_dict** </br>
*при вызове метода get_books_rating(), выведенный словарь соответствует 
словарю book_rating*


9. **test_add_book_in_favorites_one_new_book_in_favorites_true** </br>
*при вызове метода add_book_in_favorites, книга
записывается в список favorites и длина списка соответствует 
количеству добавленных книг*


10. **test_delete_book_from_favorites_true** </br>
*при вызове метода delete_book_from_favorites_book, книга
из списка favorites удаляется и длина списка соответствует 
количеству оставшихся книг*

    
11. **test_delete_book_from_favorites_book_not_in_list_list_not_changes** </br>
*при вызове метода delete_book_from_favorites, книга, которой нет
в списке favorites не удаляется и длина списка не изменяется*

12. **test_get_list_of_favorites_books_true** </br>
*при вызове метода get_list_of_favorites, выводятся все книги, которые добавлены в список,
 длина списка соответствует количеству книг, которые были добавлены в избранное*
