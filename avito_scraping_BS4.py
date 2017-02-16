import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(date):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((date['title'],
                    date['price'],
                    date['metro'],
                    date['url']))


def get_page_date(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        name = ad.find('div', class_='description').find('h3').text.strip().lower()
        if 'htc' in name:
            try:
                title = ad.find('div', class_='description').find('h3').text.strip()
            except:
                title= ''
            try:
                url = 'https://www.avito.ru/' + ad.find('div', class_='description').find('h3').find('a').get('href')
            except:
                url = ''
            try:
                price = ad.find('div', class_='about').text.strip()
            except:
                price = ''
            try:
                metro = ad.find('div', class_='data').find('p').text.strip()
            except:
                metro = ''
            date = {'title': title,
                    'price': price,
                    'metro': metro,
                    'url': url}
            write_csv(date)
        else:
            continue


def main():
    url = 'https://www.avito.ru/moskva/telefony/htc'
    base_url = 'https://www.avito.ru/moskva/telefony/htc?p='

    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        url_gen = base_url + str(i)
        html = get_html(url_gen)
        get_page_date(html)

if __name__ == '__main__':
    main()
