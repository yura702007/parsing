from pprint import pprint

from get_response import get_response
from bs4 import BeautifulSoup
from settings import URL


class ParserPage:
    """
    Извлечение данных о товаре
    """

    def __init__(self, category='Для детей и младенцев', link='https://e-dostavka.by/catalog/8008.html'):
        self.url = link
        self.list_of_products = []
        self.dict_of_products = {category: self.list_of_products}

    def get_page(self):
        """
        Получение ответа от страницы
        """
        while self.url:
            resp = get_response(url=self.url)
            self.give_html_code(page_code=resp.text)

    def give_html_code(self, page_code):
        """
        Получение исходного кода страницы
        """
        soup = BeautifulSoup(page_code, features='lxml')
        block = soup.find('div', class_='products_block__wrapper products_4_columns vertical')
        self.parse_info(block=block)
        self.set_url(block=block)

    def set_url(self, block):
        """
        Перезагрузка url
        :param block: bs4.BeautifulSoup
        :return: url
        """
        try:
            more_cards = block.find('a', class_='show_more')
            if more_cards:
                self.url = self.give_url(more_cards)
                return
            next_page = block.find('a', class_='next_page_link')
            self.url = self.give_url(next_page)
            return
        except AttributeError:
            return

    @staticmethod
    def give_url(tag):
        """
        Получение ссылок перехода по странице
        """
        if tag:
            link = tag.get('href')
            return URL + link
        return

    def parse_info(self, block):
        """
        Сохранение данных о товаре
        """
        try:
            cards = block.find_all('div', class_='form_wrapper')
            for card in cards:
                title = card.find('div', class_='title').text.strip()
                price = card.find('div', class_='price').text.strip()
                url = card.find('a', class_='fancy_ajax').get('href')
                try:
                    country = card.find('div', class_='small_country').text.strip()
                    self.list_of_products.append(
                        {'title': title, 'price': price, 'country': country.strip(), 'url': url}
                    )
                except AttributeError:
                    self.list_of_products.append(
                        {'title': title, 'price': price, 'country': None, 'url': url}
                    )
        except AttributeError:
            pass


def main():
    p = ParserPage()
    p.get_page()
    result = p.dict_of_products
    pprint(result)


if __name__ == '__main__':
    main()
