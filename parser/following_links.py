from pprint import pprint

from parser_links import get_links
from parser_data import ParserPage


def following_links():
    """
    получение данных о товарах по категориям
    :yield: dict_of_products
    """
    for title, link in get_links().items():
        page = ParserPage(category=title, link=link)
        page.get_page()
        yield page.dict_of_products


def main():
    pprint(next(following_links()))


if __name__ == '__main__':
    main()
