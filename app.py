from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep # this should go at the top of the file
from selenium.webdriver.support import expected_conditions as expect
import re
import json

      # Selenium::WebDriver::Chrome.driver_path = "/Users/kenwang/bin/chromedriver"
#id="Icons-/-Semantic-/-Place"


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<var>')
def daily_post(var):
    diction = {}
    browser = webdriver.PhantomJS()
    browser.set_window_size(411, 768)
    url = "https://deliveroo.com.au/restaurants/sydney/"
    url = url +var

    #RestaurantsList-f37d5282571072cb
    #RestaurantsList-f37d5282571072cb
    browser.get(url)

    arr=[];
    arr = browser.find_elements_by_class_name("RestaurantsList-f37d5282571072cb");
    counter = 0;
    for x in arr:
        xarr = []
        xarr = x.text.splitlines()
        toBeAddedArray = []
        for data in xarr:
            if (re.search(r'\d', data) or data.find("$")!= -1 or data=="Min" or data=="Pre-order"):
                data = None
            # print(data)
            if(data != None):
                toBeAddedArray.append(data)



        #things to remove. numbers, $$$, Pre-order, Min

        barr=[]
        barr = x.find_elements_by_class_name("RestaurantCard-4ed7f323d018d7ae")
        for i in barr:
            shadyHTML = i.get_attribute('innerHTML')
            replaced = re.sub('\"><.*', "", shadyHTML)
            shadyHTML = re.sub('<a href=\"', "", replaced)

            #print(shadyHTML)
            toBeAddedArray.append(shadyHTML)
        # print("\n")
        diction[counter] = toBeAddedArray;
        counter+=1

    html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    # html = browser.page_source
    print (diction)
    diction = json.dumps(diction)

    return diction
