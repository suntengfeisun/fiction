# -*- coding: utf-8 -*-

import time
import requests
import re
from lxml import etree
from public.mysqlpooldao import MysqlDao
from public.headers import Headers


def get_last_page(url, page=5):
    while True:
        urll = url % page
        print(urll)
        headers = Headers.get_headers()
        html = requests.get(urll, headers=headers, timeout=30).text
        if html == u'服务器缓存接口异常':
            break
        page = page + 5
    return page-5


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    mysql_dao = MysqlDao()
    sql = 'select `id`,`url` from fiction_category WHERE `url` <> "" AND `last_page`=0'
    res = mysql_dao.execute(sql)
    for r in res:
        id = r[0]
        url = r[1]
        last_page = get_last_page(url)
        sql = 'update fiction_category SET `last_page`=%s where `id`=%s' % (last_page, id)
        print(sql)
        mysql_dao.execute(sql)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
