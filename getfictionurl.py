# -*- coding: utf-8 -*-

import time
import requests
import random
import simplejson
from lxml import etree
from public.mysqlpooldao import MysqlDao
from public.headers import Headers


def get_category():
    mysql_dao = MysqlDao()
    # sql = 'select * from fiction_category WHERE `url` <> "" AND `from_id`=6'
    # sql = 'select * from fiction_category WHERE `url` <> ""'
    # sql = 'select * from fiction_category WHERE `url` <> "" AND `id`>175 AND `from_id`=13'
    sql = 'select * from fiction_category WHERE `url` <> "" AND `id`>175'
    res = mysql_dao.execute(sql)
    return res


def get_url(cates):
    cates = list(cates)
    random.shuffle(cates)
    for c in cates:
        id = c[0]
        base_url = c[2]
        last_page = c[3]
        from_id = c[4]
        page = last_page
        while True:
            if page == 0:
                break
            headers = Headers.get_headers()
            if last_page == 1:
                list_url = base_url
            else:
                list_url = base_url % page
            mysql_dao = MysqlDao()
            try:
                print(list_url)
                html = requests.get(list_url, headers=headers, timeout=30).content
                selector = etree.HTML(html)
                if from_id == 1:
                    titles = selector.xpath('//span[@class="de_name"]/a/text()')
                    urls = selector.xpath('//span[@class="de_name"]/a/@href')
                elif from_id == 2:
                    titles = selector.xpath('//div[@class="name"]/strong/a/text()')
                    urls = selector.xpath('//div[@class="name"]/strong/a/@href')
                elif from_id == 3:
                    data = simplejson.loads(html)
                    titles = []
                    urls = []
                    for b in data['booklist']:
                        titles.append(b['bookname'])
                        urls.append('http://www.xxsy.net/info/%s.html' % b['bookid'])
                elif from_id == 4:
                    titles = selector.xpath('//ul[@class="main_con"]/li/span[@class="chap"]/a[1]/text()')
                    urls = selector.xpath('//ul[@class="main_con"]/li/span[@class="chap"]/a[1]/@href')
                elif from_id == 5:
                    titles = selector.xpath('//td[@class="td3"]/span[1]/a[1]/text()')
                    urls = selector.xpath('//td[@class="td3"]/span[1]/a[1]/@href')
                elif from_id == 6:
                    titles = selector.xpath('//a[@class="green"]/text()')
                    urls = selector.xpath('//a[@class="green"]/@href')
                elif from_id == 7:
                    titles = selector.xpath('//a[@id="a_novel_name"]/text()')
                    urls = selector.xpath('//a[@id="a_novel_name"]/@href')
                elif from_id == 8:
                    titles = selector.xpath('//a[@class="a_16b"]/text()')
                    urls = selector.xpath('//a[@class="a_16b"]/@href')
                elif from_id == 9:
                    titles = selector.xpath('//ul[@class="Comic_Pic_List"]/li[2]/strong[1]/a[1]/text()')
                    urls = selector.xpath('//ul[@class="Comic_Pic_List"]/li[2]/strong[1]/a[1]/@href')
                elif from_id == 10:
                    titles = selector.xpath('//a[@class="book_pic"]/@title')
                    urls = selector.xpath('//a[@class="book_pic"]/@href')
                elif from_id == 11:
                    # http://m.biquge.com/fenlei1_2.html
                    titles = selector.xpath('//i[@class="iTit"]/a[1]/text()')
                    urls = selector.xpath('//i[@class="iTit"]/a[1]/@href')
                elif from_id == 12:
                    # http://www.5du5.com/fenlei2/fenlei2-2.html
                    titles = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/text()')
                    urls = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/@href')
                elif from_id == 13:
                    # http://www.ciluke.com/fenlei2/2/
                    titles = selector.xpath('//table[@class="grid"]/tr/td[1]/a[1]/text()')
                    urls = selector.xpath('//table[@class="grid"]/tr/td[1]/a[1]/@href')
                elif from_id == 14:
                    # http://www.23wx.com/class/2_2.html
                    titles = selector.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/text()')
                    urls = selector.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/@href')
                elif from_id == 15:
                    # http://www.x81zw.com/modules/article/articlelist.php?class=1&page=2
                    titles = selector.xpath('//div[@class="book_news_style_text"]/h1[1]/a[1]/text()')
                    urls = selector.xpath('//div[@class="book_news_style_text"]/h1[1]/a[1]/@href')
                elif from_id == 16:
                    # http://www.panqis.cn/xianxia/shuku_1070_2.html
                    titles = selector.xpath('//div[@class="title"]/div[1]/a[1]/text()')
                    urls = selector.xpath('//div[@class="title"]/div[1]/a[1]/@href')
                elif from_id == 17:
                    # http://www.shuyuewu.com/xianxia/2.html
                    titles = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/text()')
                    urls = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/@href')
                elif from_id == 18:
                    # http://www.longtanshuw.com/mulu/10-2.html
                    titles = selector.xpath('//div[@class="title"]/h2[1]/a[1]/text()')
                    urls = selector.xpath('//div[@class="title"]/h2[1]/a[1]/@href')
                elif from_id == 19:
                    # http://www.touxiang.la/xs/2-default-0-0-0-0-0-0-2.html
                    titles = selector.xpath('//div[@class="sitebox"]/dl/dd[1]/h3[1]/a[1]/text()')
                    urls = selector.xpath('//div[@class="sitebox"]/dl/dd[1]/h3[1]/a[1]/@href')
                elif from_id == 20:
                    # http://www.quledu.com/sort-3-2/
                    titles = selector.xpath('//a[@id="a_novel_name"]/text()')
                    urls = selector.xpath('//a[@id="a_novel_name"]/@href')
                elif from_id == 21:
                    # http://www.wucuo.cc/wcxs/xianxia_2.html
                    titles = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/text()')
                    urls = selector.xpath('//div[@class="l"]/ul[1]/li/span[@class="s2"]/a[1]/@href')
                elif from_id == 23:
                    # http://www.92zw.com/bookssort2/0/2.html
                    titles = selector.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/text()')
                    urls = selector.xpath('//tr[@bgcolor="#FFFFFF"]/td[1]/a[1]/@href')
                else:
                    titles = []
                    urls = []
                len_titles = len(titles)
                if len_titles > 0 and len(urls) > 0:
                    n = 0
                    while True:
                        if n == len_titles:
                            break
                        created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                        title = titles[n]
                        url = urls[n]
                        if from_id == 1:
                            url = 'http://xiaoshuo.sogou.com' + url
                        if from_id == 7:
                            url = 'http://www.quledu.com' + url
                        if from_id == 9:
                            url = 'http://book.sfacg.com' + url
                        if from_id == 11:
                            url = 'http://m.biquge.com' + url
                        if from_id == 12:
                            url = 'http://www.5du5.com' + url
                        if from_id == 15:
                            url = 'http://www.x81zw.com' + url
                        if from_id == 16:
                            url = 'http://www.panqis.cn' + url
                        if from_id == 18:
                            url = 'http://www.longtanshuw.com' + url
                        if from_id == 20:
                            url = 'http://www.quledu.com' + url
                        print(title)
                        sql = 'insert ignore into fiction_list (`category_id`,`title`,`url`,`created_at`)VALUES ("%s","%s","%s","%s")' % (
                            id, title, url, created_at)
                        mysql_dao.execute(sql)
                        n = n + 1
            except Exception as e:
                print(e)
            page = page - 1


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    cates = get_category()
    get_url(cates)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
