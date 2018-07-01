# -*- coding: utf-8 -*-
from urllib.parse import urlencode

from pyspider.libs.base_handler import *
from winspider import HandlerMixin, ChromeObj, ResponseInspector

chrome_obj = ChromeObj()
checkpoint1 = (
    lambda response: response.etree.xpath("*//form[@action='/errors/validateCaptcha']/div/div/div/div/img"), '出现验证码')


class AmzHandler(BaseHandler, HandlerMixin):
    crawl_config = {
        'headers': {
            'User-Agent': chrome_obj.useragent
        }
    }

    @every(minutes=3)
    def on_start(self):
        for f in self.walk_files(['.txt']):
            with open(f, 'r') as file:
                for keyword in file.readlines():
                    keyword = keyword.strip()
                    if not keyword: continue
                    for page in range(1, 11):
                        self.crawl_with_chrome_cookies(
                            'https://www.amazon.es/gp/search/ref=sr_pg_2?' + urlencode(
                                {'keywords': keyword, 'page': page}),
                            callback=self.details_page,
                            validate_cert=False,
                            save={'keyword': keyword, 'page': page}
                        )

    @config(age=10 * 60)
    @ResponseInspector(checkpoint1)
    def details_page(self, response):
        for i, element in enumerate(response.etree.xpath(".//li[contains(@id, 'result_')]")):
            self.send_message(
                self.project_name,
                {
                    'page': response.save['page'],
                    'keyword': response.save['keyword'],
                    'serial': i + 1,
                    'img': ''.join(element.xpath("div//a/img/@src")),
                    'asin': ''.join(element.xpath("@data-asin")),
                    'review_count': ''.join(
                        element.xpath(
                            "div//span[@name='%s']/following::a[1]/text()" % ''.join(element.xpath("@data-asin")))),
                    'review_rating': ''.join(
                        element.xpath(
                            "div//span[@name='%s']/span/a/i/span/text()" % ''.join(element.xpath("@data-asin")))),
                    'price': ''.join(element.xpath("div//span[@class='sx-price sx-price-large']/.//text()")),
                    'title': ''.join(element.xpath("div//a/@title")),
                    'brand': ''.join(element.xpath("div//a[@title]/parent::div/following::div[1]/span[2]/text()")),
                    'is_ad': 1 if element.xpath("div//h5") else 0,
                    'is_bestseller': 1 if element.xpath("div//a[contains(@id, 'BESTSELLER')]") else 0
                },
                'https://www.amazon.es#%s#%i#%i' % (response.save['keyword'], response.save['page'], i + 1)
            )

    def on_message(self, project, msg):
        return msg
