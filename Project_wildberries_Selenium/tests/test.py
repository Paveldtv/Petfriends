
#
#python -m pytest -v --driver Chrome --driver-path D:/Project_wildberries_Selenium/tests/chromedriver.exe D:/Project_wildberries_Selenium/tests/test.py
import time

import pytest

from pages.wildberries import MainPage

@pytest.mark.parametrize("_search", ['стол', 'телевизор', "фен","телефон"])
def test_1_search(web_browser, _search):
    """ Проверка,что поиск работает. """

    page = MainPage(web_browser)

    page.search = _search
    page.search_run_button.click()

    # Проверка, что список товаров не пустой:
    assert page.products_titles_eng.count() != 0

    for title in page.products_titles_eng.get_text():
        msg = 'Проверяем наличие в названии "{}"'.format(title)
        print("title",title)
        print("msg",msg)
        assert _search in title.lower(), msg

def test_2_search_eng_keyboard(web_browser):
    """ Проверка, что поиск с неправильной раскладкой клавиатуры работает нормально. """

    page = MainPage(web_browser)

    # Вводим "телевизор" с английской раскладкой клавиатуры:
    page.search.move_to_element()
    page.search = 'ntktdbpjh'
    page.search_run_button.move_to_element()
    page.search_run_button.click()

    # Проверяем что список товаров не пустой :
    assert page.products_titles_eng.count() != 0

    # Проверяем что пользователь нашел соответствующие товары
    for title in page.products_titles_eng.get_text():
        msg = 'Проверяем наличие в названии "{}"'.format(title)
        assert 'телевизор' in title.lower(), msg

def test_3_sort_price(web_browser):
      """"Проверка работоспособности сортировки по цене"""
      page = MainPage(web_browser)

      page.search = 'телефон'
      page.search_run_button.click()

      page.sort_products_by_price.click()
      page.wait_page_loaded()

      all_prices = page.products_prices.get_text()

      # Берем числовую часть и конвертируем в числовой формат
      all_prices = [float(p[:len(p)-1].replace(' ', '')) for p in all_prices]
      print("all_prices",all_prices)
      print(sorted(all_prices))

      assert all_prices == sorted(all_prices), "Сортировка по цене не работает!"

def test_4_sort_price(web_browser):
      """"Проверка работоспособности сортировки по рейтингу"""
      page = MainPage(web_browser)

      page.search = 'кружка'
      page.search_run_button.click()

      page.sort_products_by_rating.click()
      page.wait_page_loaded()

      all_ratings = page.products_rating.get_text()

      # Проверяем количество отзывов и оценок
      all_ratings = [float(p.replace(' ', '')) for p in all_ratings]
      print("all_ratings",all_ratings)
      print(sorted(all_ratings))

      assert all_ratings == sorted(all_ratings, reverse=True), "Сортировка по рейтингу не работает!"

def test_5_sort_sale(web_browser):
      """"Проверка работоспособности сортировки по скидке """
      page = MainPage(web_browser)

      page.search = 'кружка'
      page.search_run_button.click()

      page.sort_products_by_sale.click()
      page.wait_page_loaded()

      all_sales = page.products_sale.get_text()

      # Конвертация размера скидки в числовой формат
      all_sales = [float(p[1:len(p)-1].replace(' ', '')) for p in all_sales]
      print("all_sales",all_sales)
      print(sorted(all_sales))

      assert all_sales == sorted(all_sales, reverse=True), "Сортировка по скидке не работает!"

def test_6_sort_day_delivery(web_browser):
      """"Проверяем работоспособность сортировки по дате доставки"""
      page = MainPage(web_browser)

      page.search = 'велосипед'
      page.search_run_button.click()

      page.sorted_one_day.click()
      page.wait_page_loaded()

      for delivery in page.delivery_day.get_text():
        msg = 'Проверяем наличие в названии "{}"'.format(delivery)
        print("delivery",delivery)
        print("msg",msg)

        assert 'завтра' in delivery.lower(), msg

def test_7_sort_brand(web_browser):
      """"Проверяем работоспособность сортировки по бренду"""
      page = MainPage(web_browser)

      page.search = 'телевизор'
      page.search_run_button.click()

      page.sorted_brand.click()
      page.wait_page_loaded()

      for brand_name in page.brand_name.get_text():
        msg = 'Проверяем наличие в названии "{}"'.format(brand_name)
        print("brand_name",brand_name)
        print("msg",msg)

        assert 'lg' in brand_name.lower(), msg

def test_8_link_logo(web_browser):
      """"Проверяем работоспособность ссылки логотипа в панели навигации"""
      page = MainPage(web_browser)
      page.delivery_link.click()
      page.logo_link.click()

      assert page.get_current_url() == 'https://www.wildberries.ru/'

def test_9_chat(web_browser):
      """"Проверяем работоспособность чата в навигации"""
      page = MainPage(web_browser)

      page.chat.click()
      page.chat_input.send_keys("Товар можно вернуть?")
      page.chat_btn.click()

      assert page.chat_mesage.get_text() == "Товар можно вернуть?"

@pytest.mark.xfail(reason="Добавить в корзину не работает")
def test_10_menu(web_browser):
      """"Проверка добавления в корзину из карточки товара"""
      page = MainPage(web_browser)

      page.search = 'ноутбук'
      page.search_run_button.click()

      page.cart_product.click()
      page.wait_page_loaded()
      page.block_aad.find()
      page.block_aad.move_to_element()

      page.add_in_basket.move_to_element()
      page.add_in_basket.click()

      page.basket.click()

      assert page.basket_block_product.is_presented()

@pytest.mark.xfail(reason="Добавить в корзину из общего списка не работает")
def test_11_add_in_basket(web_browser):
      """"Проверка добавления в корзину  из общего списка"""
      page = MainPage(web_browser)

      page.search = 'ноутбук'
      page.search_run_button.click()

      page.cart_product.move_to_element()
      time.sleep(5)
      page.basket_in_search.move_to_element()
      page.basket_in_search.click()
      page.basket.click()

      assert page.basket_block_product.is_presented()

def test_12_sorted_color(web_browser):
      """"Проверка сортировки по цвету"""
      page = MainPage(web_browser)

      page.search = 'стол'
      page.search_run_button.click()

      page.sorted_color.scroll_to_element()
      page.sorted_color.click()
      page.wait_page_loaded()

      page.cart_product_test_12.click()

      assert 'красный' in page.color.get_text().lower()


def test_13_sorted_color_bacspace(web_browser):
    """"Проверка сброса сортировки по цвету"""
    page = MainPage(web_browser)

    page.search = 'стол'
    page.search_run_button.click()

    page.sorted_color.scroll_to_element()
    page.sorted_color.click()
    page.wait_page_loaded()
    page.sorted_color_backspace.scroll_to_element()
    page.sorted_color_backspace.click()

    page.cart_product_test_12.scroll_to_element()
    page.cart_product_test_12.click()

    for color in page.color.get_text():
        msg = 'Проверяем наличие в названии "{}"'.format(color)
        print("color",color)
        print("msg",msg)
        assert 'белый' in page.color.get_text().lower()

def test_14_link_kak_sdelat_zakaz(web_browser):
    """"Проверка работоспособности ссылки "Как сделать заказ" в футере"""
    page = MainPage(web_browser)

    page.kak_zakazat.scroll_to_element()
    page.kak_zakazat.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/kak-sdelat-zakaz'

def test_15_link_payment_method(web_browser):
    """"Проверка работоспособности ссылки "Способы оплаты" в футере"""
    page = MainPage(web_browser)

    page.payment_method.scroll_to_element()
    page.payment_method.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/sposoby-oplaty'

def test_16_link_delivery(web_browser):
    """"Проверка работоспособности ссылки "Доставка" в футере"""
    page = MainPage(web_browser)

    page.link_delivery_footer.scroll_to_element()
    page.link_delivery_footer.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka'


def test_17_link_delivery(web_browser):
    """"Проверка работоспособности ссылки "Возврат товара" в футере"""
    page = MainPage(web_browser)

    page.link_return_product.scroll_to_element()
    page.link_return_product.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-tovara'

def test_18_link_delivery(web_browser):
    """"Проверка работоспособности ссылки "Возврат денежныхс средств" в футере"""
    page = MainPage(web_browser)

    page.link_return_money.scroll_to_element()
    page.link_return_money.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-denezhnyh-sredstv'

def test_19_link_rules(web_browser):
    """"Проверка работоспособности ссылки "Правила продажи" в футере"""
    page = MainPage(web_browser)

    page.link_rules.scroll_to_element()
    page.link_rules.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-prodazhi'

def test_20_link_rules_wildberries(web_browser):
    """"Проверка работоспособности ссылки "Правила пользования торговой площадкой" в футере"""
    page = MainPage(web_browser)

    page.link_rules_wildberries.scroll_to_element()
    page.link_rules_wildberries.click()

    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-polzovaniya-torgovoy-ploshchadkoy'

def test_21_link_faq(web_browser):
    """"Проверка работоспособности ссылки "Вопросы и ответы" в футере"""
    page = MainPage(web_browser)

    page.link_faq.scroll_to_element()
    page.link_faq.click()

    assert page.get_current_url() =='https://www.wildberries.ru/services/voprosy-i-otvety'

