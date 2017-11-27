# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from Scrapy_Rental_WIFI.items import ScrapyRentalWifiItem
from scrapy.utils.response import get_base_url
from time import gmtime, strftime

class WIFICrawler(scrapy.Spider):
    name = 'Scrapy_Rental_WIFI'
    domain = 'https://www.ivideo.com.tw'
    start_urls = ['https://www.ivideo.com.tw/rent_memory/wifi/japan']
    def parse(self, response):
        res = BeautifulSoup(response.body,'html5lib')
        urls = res.select('a[href^="/rent_memory/wifi/"]')
        for i in range(len(urls)):
            yield scrapy.Request(self.domain+urls[i]['href'], self.parse2)


    def parse2(self , response):
        res = BeautifulSoup(response.body,'html5lib')
        for td in res.select('td[align="center"]'):
            if(len(td.select('a[href^="/wifi/"]')) == 0 or len(td.select('fieldset')) == 0):
                continue

            for a in td.select('a[href^="/wifi/"]'):
                if(a.text== ''):
                    continue
                yield scrapy.Request(self.domain+a['href'] , self.parse3)

    def parse3(self , response):
        url = get_base_url(response)
        res = BeautifulSoup(response.body,'html5lib')
        item = ScrapyRentalWifiItem()
        item['title'] = None
        item['url'] = url
        item['discount_price_program'] = None
        item['discount_price_description'] = None
        item['discount_price_day1_text'] = None
        item['discount_price_day1_price'] = None
        item['discount_price_day1_after_text'] = None
        item['discount_price_day1_after_price'] = None
        item['daily_rental_program'] = None
        item['daily_rental_day1_text'] = None
        item['daily_rental_day1_price'] = None
        item['daily_rental_day1_after_text'] = None
        item['daily_rental_day1_after_price'] = None
        item['monthly_rental_program'] = None
        item['monthly_rental_text1'] = None
        item['monthly_rental_text2'] = None
        item['crawl_time'] = None

        item['crawl_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        title = res.select('h1')[0].text
        item['title'] = title

        for fieldset in res.select('.eayly'):
            b = fieldset.select('b')[0].text

            fieldset.find('b').string = ''

            if(b == '【優惠價】'):
                item['discount_price_program'] = b
                try:
                    item['discount_price_description'] = fieldset.select('legend')[0].next_sibling
                except Exception as e:
                    pass
                try:
                    item['discount_price_day1_text'] = fieldset.select('br')[0].next_sibling
                except Exception as e:
                    pass
                try:
                    item['discount_price_day1_price'] = fieldset.select('font')[0].text
                except Exception as e:
                    pass
                try:
                    item['discount_price_day1_after_text'] = fieldset.select('font')[1].previous_sibling
                except Exception as e:
                    pass
                try:
                    item['discount_price_day1_after_price'] = fieldset.select('font')[1].text
                except Exception as e:
                    pass

            elif(b == '【日租費用】'):
                item['daily_rental_program'] = b
                try:
                    item['daily_rental_day_text'] = fieldset.select('legend')[0].next_sibling
                except Exception as e:
                    pass
                try:
                    item['daily_rental_day1_price'] = fieldset.select('font')[0].text
                except Exception as e:
                    pass
                try:
                    item['daily_rental_day1_after_text'] = fieldset.select('font')[1].previous_sibling
                except Exception as e:
                    pass
                try:
                    item['daily_rental_day1_after_price'] = fieldset.select('font')[1].text
                except Exception as e:
                    pass

            elif(b == '【月租費用】'):
                item['monthly_rental_program'] = b
                try:
                    item['monthly_rental_text1'] = fieldset.select('legend')[0].next_sibling
                except Exception as e:
                    pass
                try:
                    item['monthly_rental_text2'] = fieldset.select('font')[0].text
                except Exception as e:
                    pass
            else:
                print('error')

        return item


from selenium import webdriver
import requests
import time
import random

def search_around(driver ,times, string):
    for i in range(times):
        try:
#             driver.switch_to_alert().click()
            time.sleep(2)
            elements = driver.find_elements_by_tag_name('a')
            if(len(elements) == 0):
                driver.back()
            rand_num = random.randint(1,len(elements))
            if(not elements[rand_num].is_displayed):
                print('123')
            print(elements[rand_num].text)
            elements[rand_num].click()
            print(i)
        except Exception as e:
            driver.back()
            print(e)
            pass

def send_keys_slow(inputElement, string):
#     inputElement.
    for i in range(len(string)):
        inputElement.send_keys(string[i])
        time.sleep(random.randint(30,150)/100)

driver = webdriver.Chrome()
driver.switch_to_window('')
driver.maximize_window()


# Sending latitude, longitude with JS script
driver.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){"+
                      "var position = {\"coords\" : {\"latitude\": \"37.773972\",\"longitude\": \"-122.431297\"}};"+
                                    "success(position);}"); 

# Printing latitude, longitude from the browser
# print(driver.execute_script("var positionStr=\"\";"+
#                                 "window.navigator.geolocation.getCurrentPosition(function(pos){positionStr=pos.coords.latitude+\":\"+pos.coords.longitude});"+
#                                 "return positionStr;")) % (fake_lat, fake_long)

# Neat stuff from google maps api!
# driver.get('https://www.google.com.tw/maps')
# driver.switch_to_window('')
# driver.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){"+
#                       "var position = {\"coords\" : {\"latitude\": 23.0185,\"longitude\": 120.3427}};"+
#                                     "success(position);}"); 
# time.sleep(5)
# googlemap_url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s" % (fake_lat, fake_long)
driver.get('https://www.google.com.tw')
time.sleep(5)
inputElement = driver.find_element_by_id('lst-ib')
# inputElement.send_keys('出國上網')
send_keys_slow(inputElement,'出國上網')
driver.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){"+
                      "var position = {\"coords\" : {\"latitude\": 27.773972,\"longitude\": 122.431297}};"+
                                    "success(position);}"); 
driver.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){"+"var position = {\"coords\" : {\"latitude\": \"52.520007\",\"longitude\": \"13.404954\"}};"+"success(position);}");
# driver.

inputElement.submit()
# get_data = requests.get(googlemap_url)
# print (get_data.content)
# for i in range(1000):
#     driver.execute_script('''
#       window.navigator.geolocation.getCurrentPosition = function(success) {
#         var position = { coords : { latitude: "23.0185", longitude: "120.3427" } }; 
#         success(position);
#       }
#     ''');
driver.execute_script('''
  window.navigator.geolocation.getCurrentPosition = function(success) {
    var position = { coords : { latitude: "24.565766", longitude: "120.8318" } }; 
    success(position);
  }
''');
time.sleep(10)
driver.refresh()


# element = driver.find_element_by_xpath('//a[@href^="https://www.googleadservices.com"]')
index = 0
while index < 10:
    try :
        element = driver.find_element_by_xpath('//a[text()[contains(.,"出國上網就選飛買家")]]')
        break
    except Exception as e:
        driver.refresh()
        pass
    finally :
        index = index + 1
actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
element.click()
search_around(driver,10,"")
time.sleep(30)
driver.quit()


    


