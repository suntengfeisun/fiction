# -*- coding: utf-8 -*-

import time
from public.mysqlpooldao import MysqlDao

if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    mysql_dao = MysqlDao()
    limit_m = 0
    limit_n = 1000
    while True:
        sql = 'select `id` from fiction_list WHERE `chapter_id` = 0 AND `category_id`>175 limit %s,%s' % (
        limit_m, limit_n)
        res = mysql_dao.execute(sql)
        if len(res) == 0:
            break
        for r in res:
            list_id = r[0]
            sql = 'select `id`,`name`,`url` from fiction_chapter WHERE `list_id` = %s' % list_id
            chapters = mysql_dao.execute(sql)
            if len(chapters) > 0:
                chapter = chapters[-1]
                chapter_id = chapter[0]
                chapter_name = chapter[1]
                chapter_url = chapter[2]
                print(chapter_name)
                sql = 'update fiction_list SET `chapter_id`="%s",`chapter_name`="%s",`chapter_url`="%s" WHERE `id`="%s"' % (
                    chapter_id, chapter_name, chapter_url, list_id)
                mysql_dao.execute(sql)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
