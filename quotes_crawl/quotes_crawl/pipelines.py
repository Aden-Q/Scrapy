# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesCrawlPipeline(object):
    def process_item(self, item, spider):
    	with open('quote.txt', 'a') as file:
    		line = u"author: {0}, quote: {1}\n\n".format(item['author'], item['quote'])
    		file.write(line)
    		return item
