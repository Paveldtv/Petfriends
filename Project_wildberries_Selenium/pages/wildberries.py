#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.wildberries.ru"

        super().__init__(web_driver, url)

    # Поиск
    search = WebElement(id='searchInput')

    # Кнопка найти
    search_run_button = WebElement(id='applySearchBtn')

    # Название товара
    products_titles_eng = ManyWebElements(xpath='//span[@class="goods-name"]')

    # Сортировка по цене
    sort_products_by_price = WebElement(xpath='//a[contains(text(), "цене")]')

    # Цена товара
    products_prices = ManyWebElements(xpath='//div/div/a/div/div/span/span[@class="lower-price"]')

    # Сортировка по рейтингу
    sort_products_by_rating = WebElement(xpath='//*[@id="catalog_sorter"]/a[2]')

    # Рейтинг товара
    products_rating = ManyWebElements(xpath='//span[@class="product-card__count"]')

    # Сортировка по скидке
    sort_products_by_sale = WebElement(xpath='//*[@id="catalog_sorter"]/a[4]')

    # Скидка на товар
    products_sale = ManyWebElements(xpath='//span[@class="product-card__sale"]')

    # Сортировка по доставке
    sorted_one_day =  WebElement(xpath='//label[@data-value="24"]')

    # Количество дней на доставку
    delivery_day = ManyWebElements(xpath='//b[@class="product-card__delivery-date"]')

    # Сортировка по брендам
    sorted_brand =  WebElement(
        xpath='//fieldset[@class="j-list filter__fieldset list_left_ftopbrand render_type_1 filter__fieldset--limited"]/label[1]')

    # Имя бренда
    brand_name = ManyWebElements(xpath='//strong[@class="brand-name"]')

    # Сортировка по цвету
    sorted_color = WebElement(xpath='//*[@class="j-list-item filter__item filter__item--color "][7]')

    # Цвет товара в карточке товара
    color = WebElement(xpath='//*[@class="color"]')

    # Карточка товара
    cart_product_test_12 = WebElement(xpath='//*[@class="product-card j-card-item j-good-for-listing-event"][1]')

    # Сброс сортировки по цвету
    sorted_color_backspace = WebElement(xpath='//button[@class="j-filter-reset filter__btn-reset show"]')

    # Добавить в корзину из каталога
    basket_in_search = WebElement(xpath='//*[@class="btn-main-sm j-add-to-basket"]')

    # Карточка товара
    cart_product = WebElement(xpath='//*[@class="product-card j-card-item j-advert-card-item advert-card-item j-good-for-listing-event"][1]')

    # Кнопка добавить в корзину в карточке товара
    # add_in_basket = WebElement(xpath='//*[@class="product-page__order-container"]/div/button[@class="btn-main"]')
    add_in_basket = WebElement(css_selector='.product-page__grid .product-page__order .product-page__order-container .order .btn-main .hide-mobile')

    # Блок добавить, кнопки добавить в корзину
    block_aad = WebElement(css_selector='.product-page__order-container .order')

    # Кнопка отложить
    favorit = WebElement(xpath='//*[@class="product-page__order-container"]/button[@aria-label="Добавить в избранное"]')

    # Корзина
    basket = WebElement(xpath='//*[@class="navbar-pc__item j-item-basket"]/a[@class="navbar-pc__link j-wba-header-item"]')

    # Блок с товаром в корзине
    basket_block_product = WebElement(xpath='//*[@class="basket-form__basket-section basket-section"]')

    # Ссылка логотип
    logo_link = WebElement(xpath='//a[@class="nav-element__logo j-wba-header-item"]')

    # Ссылка быстрая доставка
    delivery_link = WebElement(xpath='//li[@class="simple-menu__item"]/a[@class="simple-menu__link j-wba-header-item"]')

    # Кнопка чат в хедере
    chat = WebElement(xpath='//button[@class="header__btn-chat btn-chat j-btn-chat-open"]')

    # Поле для сообщения в чат
    chat_input = WebElement(xpath='//textarea[@placeholder="Ваше сообщение..."]')

    # Кнопка отправки сообщения в чат
    chat_btn = WebElement(xpath='//button[@class="chat__btn-submit active"]')

    #отправленное сообщение
    chat_mesage = WebElement(xpath='//div[@class="chat__message message message--question"]/div/p')

    # Кнопка меню в панели навигации
    menu = WebElement(xpath='//button[@class="nav-element__burger j-menu-burger-btn j-wba-header-item"]')

    # Ссылки в футере в разделе "Покупателям"
    kak_zakazat =  WebElement(xpath='//a[@href="/services/kak-sdelat-zakaz"]')
    payment_method = WebElement(xpath='//a[@href="/services/sposoby-oplaty"]')
    link_delivery_footer = WebElement(xpath='//a[@href="/services/besplatnaya-dostavka"]')
    link_return_product = WebElement(xpath='//a[@href="/services/vozvrat-tovara"]')
    link_return_money = WebElement(xpath='//a[@href="/services/vozvrat-denezhnyh-sredstv"]')
    link_rules = WebElement(xpath='//a[@href="/services/pravila-prodazhi"]')
    link_rules_wildberries = WebElement(xpath='//a[@href="/services/pravila-polzovaniya-torgovoy-ploshchadkoy"]')
    link_faq = WebElement(xpath='//a[@href="/services/voprosy-i-otvety"]')


