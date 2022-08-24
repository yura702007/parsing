from pprint import pprint

from get_response import get_response
from bs4 import BeautifulSoup
from settings import URL


class ParserPage:
    """
    Извлечение данных о товаре
    """
    def __init__(self, category, link):
        self.url = link
        self.list_of_products = []
        self.dict_of_products = {category: self.list_of_products}
        self.block = None

    def get_page(self):
        """
        Получение ответа от страницы
        """
        url = self.url
        resp = get_response(url=url)
        self.parse_page(resp.text)

    def parse_page(self, page_code):
        """
        Парсинг страницы
        """
        soup = BeautifulSoup(page_code, features='lxml')
        self.block = soup.find('div', class_='products_block__wrapper products_4_columns vertical')
        self.parse_info()
        more_cards = soup.find('a', class_='show_more')
        if more_cards:
            self.give_url(more_cards)
        next_page = soup.find('a', class_='next_page_link')
        if next_page:
            self.give_url(next_page)

    def give_url(self, tag):
        """
        Получение ссылок навигации по странице
        """
        link = tag.get('href').split('/')[-1]
        self.url = URL + link
        self.get_page()

    def parse_info(self):
        """
        Сохранение данных о товаре
        """
        cards = self.block.find_all('div', class_='form_wrapper')
        try:
            for card in cards:
                title = card.find('div', class_='title').text.strip()
                price = card.find('div', class_='price').text.strip()
                url = card.find('a', class_='fancy_ajax').get('href')
                try:
                    country = card.find('div', class_='small_country').text.strip()
                    self.list_of_products.append(
                        {'title': title, 'price': price, 'country': country.strip(), 'url': url})
                except AttributeError:
                    self.list_of_products.append({'title': title, 'price': price, 'country': None, 'url': url})
        except AttributeError:
            pass


def main():
    p = ParserPage(category='Овощи и фрукты', link='https://e-dostavka.by/catalog/7998.html')
    p.get_page()
    result = p.dict_of_products
    pprint(result)


if __name__ == '__main__':
    main()
