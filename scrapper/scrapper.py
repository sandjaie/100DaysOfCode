import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=oneplus+7&ref=nb_sb_noss"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

prices_text = [ f'"{price.get_text()}"' for price in soup.find_all('span', {'class': 'a-price-whole'}) ]
titles_text = [ f'"{title.get_text()}"' for title in soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}) ]

serial_numbers = [ str(serial_number) for serial_number  in range(1, len(prices_text))]
zipped_items = zip(serial_numbers, prices_text, titles_text)

csv_headers = ['Serial Number', 'Price', 'Product']


with open('products.csv', 'w') as f:
    f.write(','.join(csv_headers) + '\n')
    for item in zipped_items:
        f.write(','.join(item) + '\n')
