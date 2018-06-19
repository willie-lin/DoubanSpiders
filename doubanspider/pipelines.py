# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log


class DoubanspiderPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # remove invalid data
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing %s of blogpost from %s' %(data, item['url']))
        if valid:
            # insert data in database
            new_movie = [{
                    'name': item['name'][0],
                    'year': item['year'][0],
                    'score': item['score'],
                    'len_time': item['len_time'],
                    'date': item['date'],
                    'classification': item['classification'],
                    'director': item['director'],
                    'celebrity': item['celebrity'],
                    'actor' : item['actor']


                }]
            self.collection.insert(new_movie)
            log.msg("Item wrote to Mongodb Database %s%s" % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
            level=log.DEBUG, spider=spider)
        return item
