
#
#python -m pytest -v --driver Chrome --driver-path D:/Project_Yandex_Selenium/tests/chromedriver.exe D:/Project_Yandex_Selenium/tests/test.py

import time
import pytest
from pages.yandex import MainPage



# def test_search(web_browser):
#     """ Проверка работы поиска. """
#
#     page = MainPage(web_browser)
#
#     page.SEARCH.is_presented()
#     page.SEARCH.send_keys("Тензор")
#     page.SUGGEST.is_presented()
#     page.SEARCH.enter_key()
#
#     # Проверка, что результат поиска есть на странице
#     assert page.RESULT_SEARCH
#
#     i = 0
#     while i < 5:
#
#         table = page.URL_RESULT.get_text()
#         msg = "Проверяем наличие cссылки "f"{table[i]}"
#         print("i=", i)
#         print("msg=", msg)
#         assert "tensor.ru" in table[i].lower(), msg
#         i = + 1

def test_pictures(web_browser):
    """ Проверка раздела "Картинки". """

    page = MainPage(web_browser)

    page.BTN_PICTURES.is_presented()
    page.BTN_PICTURES.click()
    page.swith_to_window()
    page.wait_page_loaded()

    # Проверка, что перешли на страницу с картинками
    assert page.get_current_url().split("?")[0] == "https://yandex.ru/images/"

    title = page.CATEGORY_TITLE.get_text()
    page.CATEGORY_LINK.click()

    # адрес сответствует
    assert page.get_current_url().split("?")[0] == "https://yandex.ru/images/search"
    page.wait_page_loaded()

    # Проверка что зашли в категорию
    assert title == page.CATEGORY_SEARCH_NAME.get_attribute('value')


    page.PICTURES[0].click()
    name = page.TITLE_PICTURES.get_text()

    # Проверка, что картинка открылась
    assert name

    page.NAVIGATION[3].click()

    # Перелистнули вперед
    assert name != page.TITLE_PICTURES.get_text()
    page.NAVIGATION[0].click()

    # Перелистнули назад
    assert name == page.TITLE_PICTURES.get_text()


