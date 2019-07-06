import requests
from bs4 import BeautifulSoup

#url = "https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=sr_1_1?keywords=oneplus+7&qid=1562397549&s=gateway&smid=A35FCS7U51TK3C&sr=8-1"
url = "https://www.amazon.in/s?k=oneplus+7&ref=nb_sb_noss"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find(id='productTitle').get_text()
# price = soup.find(id='priceblock_dealprice').get_text()


prices_text = [ f'"{price.get_text()}"' for price in soup.find_all('span', {'class': 'a-price-whole'}) ]
titles_text = [ f'"{title.get_text()}"' for title in soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}) ]
# print(price_text)
# print(title_text)

#prices_text = [ price.replace(',','') for price in prices_text ]
titles_text = [ title.replace(',','') for title in titles_text ]
serial_numbers = [ str(serial_number) for serial_number  in range(1, len(prices_text))]
zipped_items = zip(serial_numbers, prices_text, titles_text)

csv_headers = ['Serial Number', 'Price', 'Product']

# for item in zipped_items:
#     print(','.join(item))

with open('products.csv', 'w') as f:
    f.write(','.join(csv_headers) + '\n')
    for item in zipped_items:
        f.write(','.join(item) + '\n')


