import csv
from google import google
import pandas as pd

num_page = 100
url_file = ''
districts = ['sahebganj', 'pakur', 'dumka', 'jamtara', 'deoghar', 'godda', 'koderma', 'hazaribagh',
             'chatra', 'giridih', 'bokaro', 'bokaro', 'dhanbad', 'east singhbhum', 'seraikella kharsawan', 'west singhbum',
             'ranchi', 'khunti', 'gumla', 'simdega', 'lohardaga', 'latehar', 'palamu', 'garhwa']

def read_csv_file(file, skip_header=True):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if skip_header:
            return list(reader)[1:]
        else:
            return list


def news_searcher(url_file):
    urls = read_csv_file(url_file)
    for district in districts:

        name = []
        link = []
        description = []

        for url in urls:
            search_results = google.search('site:{} {}'.format(url, district), num_page)

            for result in search_results:
                name.append(result.name)
                link.append(result.link)
                description.append(result.description)

        data_tuple = list(zip(name, link, description))

        results = pd.DataFrame(data=data_tuple,
                               columns=['name', 'link','description'])
        results.to_csv('{}.csv'.format(district))


def main():
    news_searcher(url_file=urlfile)


if __name__ == '__main__':
    main()
