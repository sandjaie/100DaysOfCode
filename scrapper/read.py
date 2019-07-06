import csv

#Read the file, not used anywhere.
def read_text():
    """Prints the file
    """
    with open('products.csv', 'r') as r:
        line = r.readlines()
        for l in line:
            print(l, end='\n')
    
def get_price():
    """Get the price of all the products
    
    Returns:
        Price_list [list] -- [price_list]
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
    """
    price_list = get_price()
    price_list.sort()
    max_price = price_list[-1]
    return max_price

# def key(item):
#     # ['6', '57,999', 'OnePlus 7 Pro (Nebula Blue, 12GB RAM, 256GB Storage)']
#     price = item[1].replace(',','')
#     return int(price)

def find_max_priced_product():
    """Returns max priced product name and price
    
    Returns:
        product [list] -- [returns high priced product as a list]
    """
    max_price = find_max_price()
    with open('products.csv', 'r') as f:
        f = list(csv.reader(f, delimiter=','))
        product = sorted(f[1:], key=lambda item: int(item[1].replace(',','')), reverse=True)
    return product[0]

if __name__ == "__main__":
    print("Max Price from the list:", find_max_price())
    print(f"Price: {find_max_priced_product()[1]}")
    print(f"Product: {find_max_priced_product()[2]}")
