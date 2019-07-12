import csv
import json

#Reads the file, not used anywhere.
def read_text():
    """Prints the file
    """
    with open('products.csv', 'r') as file_pointer:
        lines = file_pointer.readlines()
        for line in lines:
            print(line, end='\n')

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
    products = sorted(data, key=lambda product: int(product['Price'].replace(',', '')), reverse=True)
    return products[0]

def get_price():
    """Get the price of all the products

    Returns:
        price_list [list] -- [price_list]
    """
    with open('products.csv', 'r') as fp:
        fp = csv.reader(fp, delimiter=',')
        price_list = []
        for row in fp:
            row[1] = row[1].replace(',', '')
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
    with open('products.csv', 'r') as fp:
        fp = list(csv.reader(fp, delimiter=','))
        products = sorted(fp[1:], key=lambda item: int(item[1].replace(',', '')), reverse=True)
    return products[0]

def print_max_priced_product():
    """Prints the max priced product
    """
    print("Max Price from the list:", find_max_price())
    print(f"Price: {find_max_priced_product_csv()[1]}")
    print(f"Product: {find_max_priced_product_csv()[2]}")

if __name__ == '__main__':
    print_max_priced_product()