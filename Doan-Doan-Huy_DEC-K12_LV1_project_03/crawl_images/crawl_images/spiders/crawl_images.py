import scrapy

class GlamiraSpider(scrapy.Spider):
    name = "image"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "gzip, deflate, br, zstd",
        "Accept-Encoding": "gzip, deflate",
        "sec-ch-ua-platform": "Linux",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    def start_requests(self):
        urls = ["https://www.glamira.com/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.HEADERS)

    def parse(self, response):
        image_urls = response.xpath('//img/@src').getall()  # Lấy tất cả các link ảnh
        valid_image_urls = [url for url in image_urls if url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg'))]
        if valid_image_urls:
            yield {
                'image_urls': valid_image_urls,
            }