import csv
from datetime import date
from pathlib import Path


def create_csv_file(data_dict):
    title = give_title(_dict=data_dict)
    headers = give_headers(_list=data_dict[title])
    if headers:
        today_dir_name = date.today()
        try:
            path = Path('..', 'data_files', f'{today_dir_name}')
            path.mkdir(parents=True)
        except FileExistsError:
            pass
        file = Path('..', 'data_files', f'{today_dir_name}', f'{title}.csv')
        data = data_dict[title]
        with open(file, 'w', encoding='utf8') as ff:
            writer = csv.DictWriter(ff, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


def give_title(_dict):
    return list(_dict)[0]


def give_headers(_list):
    try:
        return list(_list[0])
    except IndexError:
        return


def main():
    from parser_data import ParserPage
    p = ParserPage()
    p.get_page()
    result = p.dict_of_products
    create_csv_file(data_dict=result)


if __name__ == '__main__':
    main()
