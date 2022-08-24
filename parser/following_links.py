from parser_links import get_links
from get_response import get_response


def following_links():
    for title, link in get_links().items():
        yield {'title_category': title, 'response': get_response(url=link)}


def main():
    for title, answer in following_links():
        print(f'Категория - {title}, статус ответа - {answer.status_code}')


if __name__ == '__main__':
    main()
