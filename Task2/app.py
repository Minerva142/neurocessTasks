from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
#app.config["DEBUG"] = False

@app.route('/')
def hello_world():
    return 'Just Main Page'

@app.route('/AmazonData', methods=['GET'])
def getData():
    # load driver
    driver = webdriver.Chrome('chromedriver.exe')

    # request a page and load it on driver web element
    driver.get(
        'https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4')

    # get web elements
    elementsPriceRaw = driver.find_elements(By.CLASS_NAME, "a-price-whole")
    elementPriceFraRaw = driver.find_elements(By.CLASS_NAME, "a-price-fraction")
    elementNamesRaw = driver.find_elements(By.CLASS_NAME, "a-size-base-plus.a-color-base.a-text-normal")
    elementsPriceSymbolsRaw = driver.find_elements(By.CLASS_NAME, "a-price-symbol")

    # get the information
    elementsPrice = list(map(getText, elementsPriceRaw))
    elementsPriceFra = list(map(getText, elementPriceFraRaw))
    elementsNames = list(map(getText, elementNamesRaw))
    elementsPriceSymbols = list(map(getText, elementsPriceSymbolsRaw))

    # add fraction to the price and add whole price to the name info and symbol info
    elements =[]
    for i in range(len(elementsPrice)):
        elements.append(elementsNames[i] + " :  " +elementsPrice[i] + "." + elementsPriceFra[i] + " " + elementsPriceSymbols[i])

    # show them on page
    return render_template('elements.html',elements = elements)

def getText(x):
    return x.text

if __name__ == '__main__':
    app.run()
