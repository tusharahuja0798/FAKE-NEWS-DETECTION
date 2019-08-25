import scrapy
 
class BbcRssSpider(scrapy.Spider):
    name = "cnn_rss"
 
    def start_requests(self):
        urls = [
            'http://rss.cnn.com/rss/edition.rss',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first()
                
            }