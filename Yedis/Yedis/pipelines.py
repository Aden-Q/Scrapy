# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YedisPipeline(object):
    def process_item(self, item, spider):
    	with open('Yedis.txt', 'a') as file:
    		line = u"Repository: {0}, Language: {1}\n\n".format(item['repo_name'], item['language'])
    		file.write(line)
    		return item
