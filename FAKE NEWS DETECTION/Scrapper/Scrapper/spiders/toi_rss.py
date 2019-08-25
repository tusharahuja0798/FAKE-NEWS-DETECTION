import scrapy
 
class TOIRssSpider(scrapy.Spider):
    name = "toi_rss"
 
    def start_requests(self):
        urls = [
            'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'body' : post.xpath('title//text()').extract_first() + post.xpath('description//text()').extract_first(),
                'fake' : '0',
                'source': 'Times Of India'
                #'description': post.xpath('description//text()').extract_first()
                #'link': post.xpath('link//text()').extract_first(),
                #'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }