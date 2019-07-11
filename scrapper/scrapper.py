import requests
from bs4 import BeautifulSoup
import csv
import json
from config import *


def soup(keyword):
    url_const = "https://www.amazon.in/s?k={}&ref=nb_sb_noss".format(keyword)
    page = requests.get(url=url_const, headers=headers)
    soupy = BeautifulSoup(page.content, 'html.parser')
    return soupy

def zip_items(keyword):
    """Gets the price list and titles list and zips them into one single list
    
    Returns:
        zippered_items [list] -- [list of serial_number, price, title]
    """
    try:
        soupy = soup(keyword)
        prices_list = [ f'"{price.get_text()}"' for price in soupy.find_all('span', {'class': 'a-price-whole'}) ]
        titles_list = [ f'"{title.get_text()}"' for title in soupy.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}) ]
        serial_numbers = [ str(serial_number) for serial_number in range(1, len(prices_list))]
        zipped_items = zip(serial_numbers, prices_list, titles_list)
        return zipped_items
    except Exception as err:
        return err

def write_csv_file(keyword):
    """Writes the data into a csv file
    """
    csv_headers = ['Serial Number', 'Price', 'Product']
    zipped_items = zip_items(keyword)
    try:
        with open('products.csv', 'w') as f:
            f.write(','.join(csv_headers) + '\n')
            for item in zipped_items:
                f.write(','.join(item) + '\n')
        print("products.csv is ready")
    except Exception as err:
        return err

def write_json_file(keyword):
    """Converts the csv to json format and writes the data to products.json
    """
    try:
        write_csv_file(keyword)
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        with open('products.json', 'w') as f:
            json.dump(rows, f, indent=4, separators=(',', ': '))
    except Exception as err:
        return err   

if __name__ == "__main__":
    keyword = input("Enter the key word to search: ")
    write_json_file(keyword)
