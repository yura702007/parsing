import re
import time
from bs4 import BeautifulSoup
from get_response import get_response


def get_links():
    """
    получение ссылок из каталога товаров
    :return: dict_links
    """
    html_doc = get_response().text
    soup = BeautifulSoup(html_doc, features='lxml')
    rubrics = soup.find('div', class_='rubrics_table clearfix')
    titles = rubrics.find_all('div', class_='title')
    links_tuple = (link.find('a', href=re.compile('/catalog/'), class_=False, text=True) for link in titles)
    dict_links = {link.text: link.get('href') for link in links_tuple if link}
    return dict_links


def main():
    print(time.strftime('%X'))
    for link in get_links().values():
        print(get_response(link).status_code)
    print(time.strftime('%X'))
    # 16:27:57 ==> 16:29:55


if __name__ == '__main__':
    main()
