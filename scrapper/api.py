from flask import Flask, jsonify
from read import find_max_priced_product, read_json_data
from scrapper import write_json_file

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search/<keyword>')
def search(keyword):
    res = write_json_file(keyword=keyword)
    return jsonify(dict(success=True))

@app.route('/all', methods=['GET'])
def home():
    data = read_json_data()
    return jsonify(data)

@app.route('/max', methods=['GET'])
def max_price():
    max = find_max_priced_product()
    return jsonify(max)

if __name__ == "__main__":
    app.run(port=5010)
