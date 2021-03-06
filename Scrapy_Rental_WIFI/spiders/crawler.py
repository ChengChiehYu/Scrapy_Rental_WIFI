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

            if(b == '【早鳥價】'):
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