from scrapy import cmdline
name = 'yedispider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())