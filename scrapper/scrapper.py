import requests
from bs4 import BeautifulSoup
from config import *
from read import *

def get_key_word():
    key_word = input("Enter the key word to search: ")
    return key_word

url_cons = "https://www.amazon.in/s?k={}&ref=nb_sb_noss".format(get_key_word())
page = requests.get(url_cons, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

def zip_items():
    """Gets the price list and titles list and zips them into one single list
    
    Returns:
        zippered_items [list] -- [list of serial_number, price, title]
    """
    try:
        prices_list = [ f'"{price.get_text()}"' for price in soup.find_all('span', {'class': 'a-price-whole'}) ]
        titles_list = [ f'"{title.get_text()}"' for title in soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}) ]
        serial_numbers = [ str(serial_number) for serial_number in range(1, len(prices_list))]
        zipped_items = zip(serial_numbers, prices_list, titles_list)
        return zipped_items
    except Exception as err:
        return err

def write_file():
    """Writes the data into a csv file
    """
    csv_headers = ['Serial Number', 'Price', 'Product']
    zipped_items = zip_items()
    try:
        with open('products.csv', 'w') as f:
            f.write(','.join(csv_headers) + '\n')
            for item in zipped_items:
                f.write(','.join(item) + '\n')
        print("products.csv is ready")

    except Exception as err:
        return err
    
if __name__ == "__main__":
    write_file()
    print_max_priced_product()
