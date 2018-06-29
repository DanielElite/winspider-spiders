# -*- coding: utf-8 -*-
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
                for asin in file.readlines():
                    asin = asin.strip()
                    if asin:
                        self.crawl_with_chrome_cookies(
                            'https://www.amazon.com/dp/%s' % asin,
                            callback=self.details_page,
                            validate_cert=False
                        )
            self.recycle_file(f)

    @config(age=60 * 60)
    @ResponseInspector(checkpoint1)
    def details_page(self, response):
        if response.etree.xpath(".//span[@id='acrCustomerReviewText']/text()"):
            reviews_count = response.etree.xpath(".//span[@id='acrCustomerReviewText']/text()")[0].strip()
        else:
            reviews_count = 0

        if response.etree.xpath(".//span[@id='acrPopover']/@title"):
            star = response.etree.xpath(".//span[@id='acrPopover']/@title")[0].strip()
        else:
            star = ''

        return {
            'title': ''.join(response.etree.xpath(".//span[@id='productTitle']/text()")).strip(),
            'star': star,
            'reviews_count': reviews_count,
            'questions_count': ''.join(response.etree.xpath(".//a[@id='askATFLink']/span/text()")).strip(),
        }
