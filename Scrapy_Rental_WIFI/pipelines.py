# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.exceptions import DropItem

class ScrapyRentalWifiPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('Rental_WIFI.sqlite')
        self.cur =self.conn.cursor()
        self.cur.execute('create table if not exists Rental_WIFI(title text,url text,discount_price_program text,discount_price_description text,discount_price_day1_text text,discount_price_day1_price text,discount_price_day1_after_text text,discount_price_day1_after_price text,daily_rental_program text,daily_rental_day1_text text,daily_rental_day1_price text,daily_rental_day1_after_text text,daily_rental_day1_after_price text,monthly_rental_program text,monthly_rental_text1 text,monthly_rental_text2 text,crawl_time text);')

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        # dic = dict(item)
        # del dic['crawl_time']
        # print(dic)
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into Rental_WIFI({}) values({})'
        items = []
        for v in item.values():
            items.append(v)

        if(self.is_old_item(items)):
            DropItem('item exists already')
        else:
            self.cur.execute(sql.format(col, placeholders), items)
            return item

    def is_old_item(self , items):
        sql = 'select * from Rental_WIFI where url = ({})'
        res = self.cur.execute(sql.format('?'),(items[1],))
        row = self.cur.fetchone()
        print(items)

        if row == None:
            return False

        row = list(row)
        del row[-1]
        items = list(items)
        del items[-1]
        if row != None and set(items) == set(row):
            return True