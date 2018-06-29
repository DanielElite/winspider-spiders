# -*- coding: utf-8 -*-
from pyspider.libs.base_handler import *
from winspider import HandlerMixin, ChromeObj, ResponseInspector

chrome_obj = ChromeObj()

checkpoint1 = (lambda response: response.etree.xpath(".//div[@class='Register']"), '知乎已退出登陆')


class Handler(BaseHandler, HandlerMixin):
    crawl_config = {
        'headers': {
            "User-Agent": chrome_obj.useragent
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl_with_chrome_cookies('https://www.zhihu.com/', callback=self.detail_page, validate_cert=False)

    @ResponseInspector(checkpoint1)
    def detail_page(self, response):
        for i, card in enumerate(
                response.etree.xpath('.//div[@class="Card TopstoryItem TopstoryItem--experimentExpand"]')):
            self.send_message(
                self.project_name,
                {
                    "url": card.xpath('.//div[@itemprop="zhihu:question"]/a/@href'),
                    "title": card.xpath('.//div[@itemprop="zhihu:question"]/a/text()'),
                },
                '%s#%i' % (response.url, i)
            )

    def on_message(self, project, msg):
        return msg
