#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : jsontocsv.py
# @Time      : 2018/6/15 17:53
# @software  : PyCharm


import csv
import json
import codecs
import sys


def trans(path):
    jsonData = codecs.open(path + '\\result.json', 'r', 'utf-8')
    csvfile = open(path + '\\result.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_ALL)
    flag = True
    for line in jsonData:
        dic = json.loads(line[0:-1])
        if flag:
            keys = list(dic.keys())
            print(keys)
            writer.writerow(keys)
            flag = False
        writer.writerow(list(dic.values()))
    jsonData.close()
    csvfile.close()


if __name__ == '__main__':
    path = 'D:\PycharmProjects\doubanspider'
    trans(path)