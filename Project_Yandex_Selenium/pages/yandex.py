#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://yandex.ru/"

        super().__init__(web_driver, url)

    # Поиск
    SEARCH = WebElement(css_selector='#text')

    # Кнопка найти
    SEARCH_BUTTON = WebElement(css_selector='.button.mini-suggest__button.button_theme_search.button_size_search.i-bem.button_js_inited')

    # Список подсказок
    SUGGEST = WebElement(css_selector='.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')

    # Название товара
    URL_RESULT = ManyWebElements(css_selector='.Path.Organic-Path.path.organic__path a b')

    # Сортировка по цене
    RESULT_SEARCH = WebElement(css_selector='#search-result')

    # Кнопка "Картинки"
    BTN_PICTURES = WebElement(css_selector='a[data-id="images"]')

    # Ссылка на категорию
    CATEGORY_LINK = WebElement(css_selector='.PopularRequestList-Item.PopularRequestList-Item_pos_0 a')

    # Название категории
    CATEGORY_TITLE = WebElement(css_selector='.PopularRequestList-Item.PopularRequestList-Item_pos_0 .PopularRequestList-SearchText')

    # Имя категории в поле поиска
    CATEGORY_SEARCH_NAME = WebElement(css_selector='.input__control.mini-suggest__input')

    # Ссылки на картинки
    PICTURES = ManyWebElements(css_selector='.serp-item__link')

    # Название картинки в открытой картинке
    TITLE_PICTURES = ManyWebElements(css_selector='.MMOrganicSnippet-Text')

    # Кнопки навигации
    NAVIGATION = ManyWebElements(css_selector='.CircleButton-Icon')


