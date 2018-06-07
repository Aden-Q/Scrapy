import scrapy
from scrapy.selector import Selector
from quotes_crawl.items import QuotesCrawlItem


class QuoteSpider(scrapy.Spider):
	name = "quotespider"
	urls = "http://quotes.toscrape.com/page/"
	start_urls = []
	for i in range(1,11):
		start_urls.append(urls+str(i)+'/')
	
	def parse(self, response):
		hxs = Selector(response)
		infos = hxs.xpath('//div[@class="quote"]')
		for info in infos:
			item = QuotesCrawlItem()
			item['author'] = info.xpath('./span/small[@class = "author"]/text()').extract()[0].strip()
			item['quote'] = info.xpath('./span[@class="text"]/text()').extract()[0].strip()
			yield item
		
