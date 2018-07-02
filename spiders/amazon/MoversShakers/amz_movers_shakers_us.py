# -*- coding: utf-8 -*-
import re

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
                for url in file.readlines():
                    url = url.strip()
                    if not url: continue
                    self.crawl_with_chrome_cookies(url, callback=self.details_page, validate_cert=False)
                    self.crawl_with_chrome_cookies(url + '?pg=2', callback=self.details_page, validate_cert=False)

    @config(age=60 * 60)
    @ResponseInspector(checkpoint1)
    def details_page(self, response):
        for element in response.etree.xpath(".//li[@class='zg-item-immersion']"):
            if not element.xpath(".//span[contains(@class, 'zg-item')]/a"): continue
            self.send_message(
                self.project_name,
                {
                    'url': response.url,
                    'category': ''.join(response.etree.xpath(".//span[@class='category']/text()")),
                    'asin': re.search('dp/(.+?)/',
                                      element.xpath(".//span[contains(@class, 'zg-item')]/a/@href")[0]).group(1),
                    'ranking': ''.join(element.xpath(".//span[@class='zg-badge-text']/text()")),
                    'img': ''.join(element.xpath(".//img/@src")),
                    'title': ''.join(element.xpath(".//img/@alt")),
                    'review_rating': ''.join(element.xpath(".//i[contains(@class, 'a-icon-star')]/span/text()")),
                    'review_count': ''.join(
                        element.xpath(".//i[contains(@class, 'a-icon-star')]/parent::a/following-sibling::a/text()")),
                    'price': ''.join(element.xpath(".//span[@class='p13n-sc-price']/text()")),
                    'percent_change': ''.join(element.xpath(".//span[@class='zg-percent-change']/text()")),
                    'sales_movement': ''.join(element.xpath(".//span[@class='zg-sales-movement']/text()"))
                },
                response.url + ''.join(element.xpath(".//span[@class='zg-badge-text']/text()")).strip()
            )

    def on_message(self, project, msg):
        return msg
