# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 电影名
    year = scrapy.Field()  # 上映年份
    score = scrapy.Field()  # 豆瓣评分
    director = scrapy.Field()  # 导演
    celebrity = scrapy.Field()  # 编剧
    date = scrapy.Field()  # 上映日期
    classification = scrapy.Field()  # 分类
    actor = scrapy.Field()  # 演员
    len_time = scrapy.Field()  # 片长
    # pass
