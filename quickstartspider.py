#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : quickstartspider.py
# @Time      : 2018/6/15 17:18
# @software  : PyCharm

from scrapy import cmdline

cmdline.execute("scrapy crawl movie".split())
