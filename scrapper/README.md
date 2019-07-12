### Web Scrapper using beautifulSoup and requests

How to run: <br>
`python scrapper.py`

products.csv and products.json are created at runtime. <br>

What it scraps:
* url: amazon.in product search page<br>
* product: key_word<br>
* Exports the data in csv format
* Finds the highest priced product and price

Need to improve:
* Add: <br>
    [ ] Update readme with api endpoints
    [ ] Add helper functions
* Feat: <br>
    [x] Build a rest api with the data gathered.
    [ ] Build the app as a web app with Flask
    [ ] Add logger
* Issues: <br>
    [ ] Do not add products if the price is missing or the tag is missing.