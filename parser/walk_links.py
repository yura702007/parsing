import time

from parser_links import get_links
from parser_data import ParserPage
from save_data import create_csv_file


def walk_links():
    """
    получение данных о товарах по категориям
    :yield: dict_of_products
    """
    for dict_link in get_links():
        title, link = list(dict_link.keys())[0], list(dict_link.values())[0]
        data = ParserPage(category=title, link=link)
        data.get_page()
        result = data.dict_of_products
        create_csv_file(result)


def main():
    print(time.strftime('%X'))
    walk_links()
    print(time.strftime('%X'))


if __name__ == '__main__':
    main()
