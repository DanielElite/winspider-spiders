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
                for asin in file.readlines():
                    asin = asin.strip()
                    if not asin: continue
                    for page in range(1, 6):
                        self.crawl_with_chrome_cookies(
                            'https://www.amazon.de/product-reviews/%(asin)s/ref=cm_cr_arp_d_viewopt_srt?'
                            'ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=%(page)i' % {
                                'asin': asin,
                                'page': page
                            },
                            callback=self.details_page,
                            validate_cert=False,
                            save={'asin': asin}
                        )

    @config(age=30 * 60)
    @ResponseInspector(checkpoint1)
    def details_page(self, response):
        for element in response.etree.xpath(".//div[@id='cm_cr-review_list']/div[@data-hook='review']/div"):
            _child_asin = re.search('product-reviews/(.+?)/', ''.join(element.xpath("div[3]/a/@href")))
            self.send_message(
                self.project_name,
                {
                    'rating': ''.join(element.xpath("div[1]/a[1]/i/span/text()")).split()[0],
                    'title': ''.join(element.xpath("div[1]/a[2]/text()")),
                    'url': 'https://www.amazon.de' + ''.join(element.xpath("div[1]/a[2]/@href")),
                    'author': ''.join(element.xpath('div[2]/span[1]/a/text()')),
                    'asin': response.save['asin'],
                    'child_asin': _child_asin.group(1) if _child_asin else response.save['asin'],
                    'review_date': ''.join(element.xpath("div//span[@data-hook='review-date']/text()")),
                    'color': ' '.join(element.xpath("div[3]/a/text()")),
                    'verified_purchase': 1 if ''.join(element.xpath("div[3]/span/a/span/text()")) else 0,
                    'review_text': '\n'.join(element.xpath("div/span[@data-hook='review-body']//text()")),
                    'w_comments': ''.join(
                        element.xpath("div/div/a/span/span[@class='review-comment-total aok-hidden']/text()")),
                    'review_votes': ''.join(element.xpath("div[7]/div/span[3]/span/span[1]/span/text()")),
                    'review_id': ''.join(element.xpath("parent::div/@id"))
                },
                'https://www.amazon.de' + ''.join(element.xpath("div[1]/a[2]/@href"))
            )

    def on_message(self, project, msg):
        return msg
