import csv
import json

#Read the file, not used anywhere.
def read_text():
    """Prints the file
    """
    with open('products.csv', 'r') as r:
        line = r.readlines()
        for l in line:
            print(l, end='\n')

def read_json_data():
    """Returns the json file
    """
    return json.load(open('products.json'))

def find_max_priced_product():
    """Sort the json file and return the max priced product
    
    Returns:
        product [list] -- [max priced product]
    """
    data = read_json_data()
    products = sorted(data, key=lambda product: int(product['Price'].replace(',','')), reverse=True)
    return products[0]

def get_price():
    """Get the price of all the products
    
    Returns:
        price_list [list] -- [price_list]
    """
    with open('products.csv', 'r') as f:
        f = csv.reader(f, delimiter=',')
        price_list = []
        for row in f:
            row[1] = row[1].replace(',','')
            if row[1].isdigit():
                price_list.append(int(row[1]))
    return price_list

def find_max_price():
    """Find the max price from the price list
    Returns:
        max price
    """
    price_list = get_price()
    price_list.sort()
    max_price = price_list[-1]
    return max_price

#Not used anywhere
def find_max_priced_product_csv():
    """Returns max priced product name and price
    
    Returns:
        product [list] -- [returns high priced product as a list]
    """
    with open('products.csv', 'r') as f:
        f = list(csv.reader(f, delimiter=','))
        products = sorted(f[1:], key=lambda item: int(item[1].replace(',','')), reverse=True)
    return products[0]

#Not used anywhere
def print_max_priced_product():
    print("Max Price from the list:", find_max_price())
    print(f"Price: {find_max_priced_product()[1]}")
    print(f"Product: {find_max_priced_product()[2]}")

