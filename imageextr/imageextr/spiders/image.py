import scrapy
import urllib


class ImageSpiderSpider(scrapy.Spider):
    name = 'image_spider'
    allowed_domains = ['www.freepik.com']
    start_urls = ['https://www.freepik.com/free-photos-vectors/nature-wallpaper']

    def parse(self, response):
        for img in response.css('img'):
            image_url = img.css('img::attr(src)').get()
            if image_url:
                urllib.request.urlretrieve(image_url, image_url.split('/')[-1])
                yield {
                    'image_url': image_url,
                }

   