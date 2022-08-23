from pprint import pprint

from bs4 import BeautifulSoup
from following_links import following_links


def get_cards():
    for answer_dict in following_links():
        title_category = answer_dict['title_category']
        response = answer_dict['response']
        html_code = response.text
        soup = BeautifulSoup(html_code, features='lxml')
        block_cards = soup.find('div', class_='products_block__wrapper products_4_columns vertical')
        # if block_cards:
        result = parse_cards(block_cards)
        yield {title_category: result}


def parse_cards(bs4_element):
    list_of_products = []
    try:
        cards = bs4_element.find_all('div', class_='form_wrapper')
        for card in cards:
            title = card.find('div', class_='title').text.strip()
            price = card.find('div', class_='price').text.strip()
            url = card.find('a', class_='fancy_ajax').get('href')
            try:
                country = card.find('div', class_='small_country').text.strip()
                list_of_products.append(
                    {'title': title, 'price': price, 'country': country.strip(), 'url': url})
            except AttributeError:
                list_of_products.append({'title': title, 'price': price, 'url': url})
        print(len(list_of_products))
        return list_of_products
    except AttributeError:
        return


def main():
    result = get_cards()
    for res in result:
        pprint(res)


if __name__ == '__main__':
    main()
