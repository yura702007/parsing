import requests
from settings import URL, HEADERS


def get_response(url=URL, headers=HEADERS):
    """
    Получение ответа от главной страницы сайта
    """
    response = requests.get(url=url, headers=headers, allow_redirects=True)
    return response


def main():
    print(get_response().status_code)


if __name__ == '__main__':
    main()
