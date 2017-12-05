#!/usr/bin/env python

#-*- coding: utf-8 -*-

import time
from cupang_crawler import CupangCrawler

if __name__ == "__main__":

    crawler = CupangCrawler()

    # setting search keyword
    #crawler.init('아이리버 휴대용 선풍기')
    #crawler.init('삼성 블루투스 이어폰')
    #crawler.init('삼성 냉장고')
    #crawler.init('LG 냉장고')
    #crawler.init('LG 블루투스 이어폰')
    #crawler.init('탈모 샴푸')
    crawler.init('전기히터')

    # store search urls
    crawler.search_item_list()

    # get reviews for urls
    crawler.item_list_load()

    count = 1
    while not crawler.list_done:
        crawler.search_item()
        count = count + 1

    crawler.end()
