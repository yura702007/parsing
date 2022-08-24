from following_links import following_links
import csv


def create_csv_file():
    for data_dict in following_links():
        title = give_title(_dict=data_dict)
        headers = give_headers(_list=data_dict[title])
        data = data_dict[title]
        path = f'{title}.csv'
        with open(path, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


def give_title(_dict):
    return list(_dict)[0]


def give_headers(_list):
    return list(_list[0])


def main():
    create_csv_file()


if __name__ == '__main__':
    main()
