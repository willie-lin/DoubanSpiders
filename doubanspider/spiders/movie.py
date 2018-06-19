#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : movie.py
# @Time      : 2018/6/15 9:34
# @software  : PyCharm

import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanspider.items import DoubanspiderItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),callback='parse_item')
    )

    # def parse_item(self, response):
    #     sel = Selector(response)
    #     item = DoubanspiderItem
    #     item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
    #     item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
    #     item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
    #     item['director'] = sel.xpath('//*[id="info"]/span[1]/a/text()').extract()
    #     item['classification'] = sel.xpath('//span[@property="v:genre"]/text()').extract()
    #     item['actor'] = sel.xpath('//*[@id="info"]/span[3]/a[1]/text()').extract()
    #     return item
    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanspiderItem()
        item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        # item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract()
        item['director'] = sel.xpath('//*[@id="info"]/span[1]/span/a/text()').extract()
        item['celebrity'] = sel.xpath('//*[@id="info"]/span[2]/span/a/text()').extract()
        item['classification'] = sel.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor'] = sel.xpath('//*[@id="info"]/span[3]//span/a/text()').extract()
        item['date'] = sel.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
        item['len_time'] = sel.xpath('//span[@property="v:runtime"]/text()').extract()
        return item