import requests
from settings import URL, HEADERS


def get_response(url=URL, headers=HEADERS):
    """
    Получение ответа от главной страницы сайта
    """
    resp = requests.get(url=url, headers=headers, allow_redirects=True)
    return resp


def main():
    print(get_response().status_code)


if __name__ == '__main__':
    main()
