from scrapy import cmdline
name = 'jd'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())