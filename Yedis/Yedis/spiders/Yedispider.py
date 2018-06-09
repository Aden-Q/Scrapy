import scrapy
import scrapy.selector as Selector
from Yedis.items import YedisItem


class Yedispider(scrapy.Spider):
    name = "yedispider"
    start_urls = ["https://github.com/Yedis"]
    allowed_domins = ['https://github.com']

    def parse(self, response):
        #hxs = Selector(response)
        infos = []
        infos_source = response.selector.xpath(
            '//li[@class="pinned-repo-item p-3 mb-3 border border-gray-dark rounded-1 public source"]')
        infos_fork = response.selector.xpath('//li[@class="pinned-repo-item p-3 mb-3 border border-gray-dark rounded-1 public fork"]')
        infos.extend(infos_source)
        infos.extend(infos_fork)
        for info in infos:
            item = YedisItem()
            item['repo_name'] = info.xpath('./span/span/a[@class="text-bold"]/@href').extract()[0].split('/')[2]
            item['language'] = info.xpath('./span/p[@class="mb-0 f6 text-gray"]/text()').extract()[1].strip()
            print(u'Repository: {0}, Language: {1}\n\n'.format(item['repo_name'], item['language']))
            yield item
