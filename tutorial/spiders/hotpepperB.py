import scrapy


class HotpepperbSpider(scrapy.Spider):
    name = 'hotpepperB'
    allowed_domains = ['beauty.hotpepper.jp']
    start_urls = ['https://beauty.hotpepper.jp/slnH000048556/blog/']

    def parse(self, response):
        #ファイル出力の設定
        filename: str = 'hotpepperB.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
