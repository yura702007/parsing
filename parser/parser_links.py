import re
import time
from bs4 import BeautifulSoup
from get_response import get_response


def open_file(path='pages/index.html'):
    with open(path, 'r', encoding='utf8') as file:
        html_code = file.read()
    return html_code


def get_links():
    """
    получение ссылок из каталога товаров
    :return: dict_links
    """
    html_doc = get_response().text
    soup = BeautifulSoup(html_doc, features='lxml')
    menu = soup.find_all('li', class_='level_1')
    links = (
        elem.find('a', href=re.compile('/catalog/'), class_=False, text=True) for elem in menu
    )
    my_exceptions = ('Тематические подборки', 'Акции')
    for link in links:
        try:
            if link.text not in my_exceptions:
                yield {link.text: link.get('href')}
        except AttributeError:
            continue


def main():
    print(time.strftime('%X'))
    for link in get_links():
        print(get_response(list(link.values())[0]))
    print(time.strftime('%X'))
    # 16:27:57 ==> 16:29:55


if __name__ == '__main__':
    main()
