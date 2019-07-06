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
    return price_list[-1]
