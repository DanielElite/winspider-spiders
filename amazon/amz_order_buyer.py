# -*- coding: utf-8 -*-
from pyspider.libs.base_handler import *
from winspider import HandlerMixin, ChromeObj, ResponseInspector

chrome_obj = ChromeObj()
checkpoint = (lambda response: response.etree.xpath(".//div[@id='ap_signin1a_pagelet']"), '美国亚马逊卖家中心已退出登陆')


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
                for order in file.readlines():
                    order = order.strip()
                    if not order: continue
                    self.crawl_with_chrome_cookies(
                        'https://sellercentral.amazon.com/messaging/inbox/ajax/load-threads',
                        method='POST',
                        data={
                            'filter': 'Search',
                            'searchInput': order,
                            'currentPageNumber': -1
                        },
                        callback=self.search_page,
                        validate_cert=False,
                        save={'orderid': order}
                    )
            self.recycle_file(f)

    @config(age=60 * 60 * 24)
    @ResponseInspector(checkpoint)
    def search_page(self, response):
        return {
            'order_id': response.save['orderid'],
            'buyer_id': ''.join(response.etree.xpath(".//input[@id='currentThreadSenderId']/@value"))
        }

    def get_taskid(self, task):
        return md5string(task['url'] + task['fetch']['data'])
