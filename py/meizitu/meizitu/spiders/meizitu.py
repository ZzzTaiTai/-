from scrapy import Request
from scrapy.spider import Spider
from meizitu.items import SpiderMeizituItem

class MeizituSpider(Spider):
    name = "meizitu"
    start_urls={'http://www.meizitu.com/a/sexy.html'}

    def parse(self, response):
        item=SpiderMeizituItem()
        meizi_photo=response.xpath('//ul[@class="wp-list clearfix"]/li')

        for meizi_tu in meizi_photo:
            images_url=meizi_tu.xpath('.//h3[@class="tit"]/a/@href').extract()[0]
            yield Request(images_url, callback=self.parse_meizi_pic)

    def parse_meizi_pic(self,response):
        item = SpiderMeizituItem()
        meizitu_pics = response.xpath('//div[@id="picture"]/p/img')

        for meizitu_pic in meizitu_pics:
            item['images'] = meizitu_pic.xpath('.//@alt').extract()[0].split('，')[0]
            item['image_urls'] = meizitu_pic.xpath('.//@src').extract()
            yield item
