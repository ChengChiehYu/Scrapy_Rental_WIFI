# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyRentalWifiItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    discount_price_program = scrapy.Field()
    discount_price_description = scrapy.Field()
    discount_price_day1_text = scrapy.Field()
    discount_price_day1_price = scrapy.Field()
    discount_price_day1_after_text = scrapy.Field()
    discount_price_day1_after_price = scrapy.Field()
    daily_rental_program = scrapy.Field()
    daily_rental_day1_text = scrapy.Field()
    daily_rental_day1_price = scrapy.Field()
    daily_rental_day1_after_text = scrapy.Field()
    daily_rental_day1_after_price = scrapy.Field()
    monthly_rental_program = scrapy.Field()
    monthly_rental_text1 = scrapy.Field()
    monthly_rental_text2 = scrapy.Field()
    crawl_time = scrapy.Field()
    # pass
