from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep # this should go at the top of the file
from selenium.webdriver.support import expected_conditions as expect
import re

      # Selenium::WebDriver::Chrome.driver_path = "/Users/kenwang/bin/chromedriver"
#id="Icons-/-Semantic-/-Place"


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<var>')
def daily_post(var):
    browser = webdriver.PhantomJS()
    browser.set_window_size(411, 768)
    url = "https://deliveroo.com.au/restaurants/sydney/"
    url = url +var

    #RestaurantsList-f37d5282571072cb
    #RestaurantsList-f37d5282571072cb
    browser.get(url)

    arr=[];
    arr = browser.find_elements_by_class_name("RestaurantsList-f37d5282571072cb");

    for x in arr:
        print(x.text)
        barr=[]
        barr = x.find_elements_by_class_name("RestaurantCard-4ed7f323d018d7ae")
        for i in barr:
            shadyHTML = i.get_attribute('innerHTML')
            replaced = re.sub('\"><.*', "", shadyHTML)
            shadyHTML = re.sub('<a href=\"', "", replaced)

            print(shadyHTML)
        print("\n")

    html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    # html = browser.page_source

    return html
