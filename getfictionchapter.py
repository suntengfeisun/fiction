# -*- coding: utf-8 -*-

import time
import requests
import re
from lxml import etree
from public.mysqlpooldao import MysqlDao
from public.headers import Headers
from public.proxies import Proxies


def save_chapter(list_id, name, url, from_id):
    name = name.strip()
    print(name)
    created_at = time.strftime('%Y-%m-%d %H:%M:%S')
    sql = 'insert ignore into fiction_chapter_%s (`list_id`,`name`,`url`,`created_at`)VALUES ("%s","%s","%s","%s")' % (
        from_id, list_id, name, url, created_at)
    mysql_dao.execute(sql)


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    mysql_dao = MysqlDao()
    limit_m = 0
    limit_n = 10
    while True:
        sql = 'select `id`,`category_id`,`url` from fiction_list WHERE category_id > 175 limit %s,%s' % (
            limit_m, limit_n)
        res = mysql_dao.execute(sql)
        if len(res) == 0:
            break
        for r in res:
            try:
                list_id = r[0]
                category_id = r[1]
                url = r[2]
                if category_id >= 1 and category_id <= 17:
                    # http://xiaoshuo.sogou.com/book/19_295014/
                    pass
                elif category_id >= 18 and category_id <= 44:
                    # http://novel.hongxiu.com/a/1282095/list.html
                    chapter_url = url + 'list.html'
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="htmlList"]/dl/dd/ul/li/strong[1]/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            if 'vip' in c.xpath('@href')[0]:
                                url = c.xpath('@href')[0]
                            else:
                                url = 'http://novel.hongxiu.com' + c.xpath('@href')[0]
                            from_id = 2
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 45 and category_id <= 56:
                    # http://www.xxsy.net/info/809547.html
                    match_obj = re.search(r'http://www.xxsy.net/info/(.*?).html', url, re.M | re.I)
                    art_id = int(match_obj.group(1))
                    chapter_url = 'http://www.xxsy.net/books/%s/default.html' % art_id
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="catalog_list"]/ul/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url.replace('default.html', c.xpath('@href')[0])
                            from_id = 3
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 57 and category_id <= 69:
                    # http://book.zongheng.com/book/569675.html
                    chapter_url = url.replace('/book/', '/showchapter/')
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//td[@class="chapterBean"]/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = c.xpath('@href')[0]
                            from_id = 4
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 70 and category_id <= 85:
                    # http://www.17k.com/book/659991.html
                    chapter_url = url.replace('/book/', '/list/')
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//dl[@class="Volume"]/dd[1]/a')
                    for c in chapters:
                        try:
                            name = c.xpath('span[1]/text()')[0]
                            url = 'http://www.17k.com' + c.xpath('@href')[0]
                            from_id = 5
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 86 and category_id <= 99:
                    # http://chuangshi.qq.com/bk/qh/13586227.html
                    pass
                elif category_id >= 100 and category_id <= 115:
                    # http://www.quledu.com/wc-54342/
                    pass
                elif category_id >= 116 and category_id <= 127:
                    # http://b.faloo.com/f/396399.html
                    match_obj = re.search(r'http://b.faloo.com/f/(.*?).html', url, re.M | re.I)
                    art_id = int(match_obj.group(1))
                    chapter_url = 'http://b.faloo.com/html/%s/%s/' % (str(art_id)[0:3], art_id)
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="centent"]/ul/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = c.xpath('@href')[0]
                            from_id = 8
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 128 and category_id <= 142:
                    # http://book.sfacg.com/Novel/52084/
                    chapter_url = url + 'MainIndex/'
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//ul[@class="list_Content "]/volumeitem/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://book.sfacg.com' + c.xpath('@href')[0]
                            from_id = 9
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 143 and category_id <= 164:
                    # http://www.xs8.cn/book/296959/index.html
                    chapter_url = url.replace('index', 'readbook')
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="mod_container"]/ul/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = c.xpath('@href')[0]
                            from_id = 10
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 176 and category_id <= 183:
                    # http://m.biquge.com/9_9040/
                    match_obj = re.search(r'http://m.biquge.com/(.*?)_(.*?)/', url, re.M | re.I)
                    art_id = int(match_obj.group(2))
                    chapter_url = 'http://m.biquge.com/booklist/%s.html' % art_id
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//ul[@class="chapter"]/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://m.biquge.com' + c.xpath('@href')[0]
                            from_id = 11
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 185 and category_id <= 190:
                    # http://www.5du5.com/book/0/47/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="list"]/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 12
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 193 and category_id <= 202:
                    # http://www.ciluke.com/0/8/8457/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="list"]/dl/dd/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 13
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 204 and category_id <= 214:
                    # http://www.23wx.com/class/2_2.html
                    match_obj = re.search(r'http://www.23wx.com/book/(.*)', url, re.M | re.I)
                    art_id = int(match_obj.group(1))
                    chapter_url = 'http://www.23wx.com/html/%s/%s/' % (str(art_id)[0:2], art_id)
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//table[@id="at"]/tr/td/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 14
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 216 and category_id <= 224:
                    # http://www.x81zw.com/book/0/434/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//dl[@id="chapterlist"]/dd/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 15
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 226 and category_id <= 231:
                    # http://www.panqis.cn/woaihuxian/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="list_box"]/ul/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://www.panqis.cn' + c.xpath('@href')[0]
                            from_id = 16
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 233 and category_id <= 239:
                    # http://www.shuyuewu.com/kan_64521/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="list"]/dl/dd/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 17
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 241 and category_id <= 250:
                    # http://www.longtanshuw.com/9173/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="novel_list"]/dl/dd/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://www.longtanshuw.com' + c.xpath('@href')[0]
                            from_id = 18
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 252 and category_id <= 261:
                    # http://www.touxiang.la/xs/10/10526/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="book_list"]/ul/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://www.touxiang.la' + c.xpath('@href')[0]
                            from_id = 19
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 263 and category_id <= 278:
                    # http://www.quledu.com/wc-54342/
                    match_obj = re.search(r'http://www.quledu.com/wc-(.*?)/', url, re.M | re.I)
                    art_id = int(match_obj.group(1))
                    chapter_url = 'http://www.quledu.com/wcxs-%s/' % art_id
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@class="zjlist4"]/ol[1]/li/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://www.quledu.com' + c.xpath('@href')[0]
                            from_id = 20
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 280 and category_id <= 287:
                    # http://www.wucuo.cc/wcxs/18/18823/
                    chapter_url = url
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//div[@id="list"]/dl[1]/dd/a[1]')
                    n = 0
                    for c in chapters:
                        if n <= 12:
                            n = n + 1
                            continue
                        try:
                            name = c.xpath('text()')[0]
                            url = 'http://www.wucuo.cc' + c.xpath('@href')[0]
                            from_id = 21
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                elif category_id >= 289 and category_id <= 301:
                    # http://www.92zw.com/booksinfo/56/56620.html
                    match_obj = re.search(r'http://www.92zw.com/booksinfo/(.*?).html', url, re.M | re.I)
                    art_id = match_obj.group(1)
                    chapter_url = 'http://www.92zw.com/files/article/html/%s/' % art_id
                    print(chapter_url)
                    headers = Headers.get_headers()
                    proxies = Proxies.get_proxies()
                    html = requests.get(chapter_url, headers=headers, proxies=proxies, timeout=30).content
                    selector = etree.HTML(html)
                    chapters = selector.xpath('//table[@id="at"]/tr/td/a[1]')
                    for c in chapters:
                        try:
                            name = c.xpath('text()')[0]
                            url = chapter_url + c.xpath('@href')[0]
                            from_id = 23
                            save_chapter(list_id, name, url, from_id)
                        except Exception as e:
                            print(e)
                else:
                    pass
            except Exception as e:
                print(e)
                time.sleep(10)
                continue
        limit_m = limit_m + limit_n

    print('game over')
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
