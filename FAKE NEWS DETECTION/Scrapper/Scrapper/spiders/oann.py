import scrapy
 
class OANNRssSpider(scrapy.Spider):
    name = "oann_rss"
 
    def start_requests(self):
        urls = [
            'https://www.oann.com/feed/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'body' : post.xpath('title//text()').extract_first() + post.xpath('description//text()').extract_first(),
                'fake' : '1',
                'source': 'OANN'
                #'description': post.xpath('description//text()').extract_first()
                #'link': post.xpath('link//text()').extract_first(),
                #'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }