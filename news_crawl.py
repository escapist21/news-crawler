from time import sleep
import random
import csv
from google import google

last_page = 40
url_file = 'english_url.csv'
districts = ['sahebganj', 'pakur', 'dumka', 'jamtara', 'deoghar', 'godda', 'koderma', 'hazaribagh',
             'chatra', 'giridih', 'bokaro', 'bokaro', 'dhanbad', 'east singhbhum', 'seraikella kharsawan',
             'west singhbum',
             'ranchi', 'khunti', 'gumla', 'simdega', 'lohardaga', 'latehar', 'palamu', 'garhwa']


def read_csv_file(file, skip_header=True):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if skip_header:
            return list(reader)[1:]
        else:
            return list


def write_csv_file(file, data):
    with open(file, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for i in range(len(data)):
            writer.writerow(data[i])


def news_searcher(url_file):
    urls = read_csv_file(url_file)
    district = str(input('Enter name of district: '))
    if district.lower() in districts:

        name = []
        link = []
        description = []

        for url in urls:
            print('Downloading news from {}'.format(url[0]))

            for i in range(last_page):
                print('Downloading from page {}'.format(i + 1))
                search_results = google.search('site:{} {}'.format(url[0], district), first_page=i + 1,
                                               sort_by_date=True)

                for result in search_results:
                    name.append(result.name)
                    link.append(result.link)
                    description.append(result.description)
                sleep(random.randint(1, 64))

            sleep(random.randint(180, 300))

        data_tuple = list(zip(name, link, description))

        new_file = '{}_english.csv'.format(district)

        write_csv_file(file=new_file, data=data_tuple)

        print('district {} is downloaded'.format(district))


def main():
    news_searcher(url_file=url_file)


if __name__ == '__main__':
    main()
