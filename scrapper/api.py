from flask import Flask, jsonify
from read import find_max_priced_product, read_json_data
from scrapper import write_json_file

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search/<keyword>')
def search(keyword):
    """Main function to invoke search based on the keyword
    creates a csv file and converts into the json format

    Arguments:
        keyword {[str]} -- [keyword to search]

    Returns:
        Success -- [ prints success]
        Note: Need to edit the return statement based on the request status
    """
    write_json_file(keyword=keyword)
    return jsonify(dict(success=True))

@app.route('/all', methods=['GET'])
def home():
    """Lists all the products from the datastore

    Returns:
        products [json] -- [all the products from the datastore]
    """
    data = read_json_data()
    return jsonify(data)

@app.route('/max', methods=['GET'])
def max_price():
    """Returns product with maximum price

    Returns:
        product [json] -- [product name, price, serial number]
    """
    product = find_max_priced_product()
    return jsonify(product)

if __name__ == "__main__":
    app.run(port=5010)
