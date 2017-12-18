# -*- coding:utf-8 -*-

"""
author:zcj
create:2017.12.15
fun:搜狗语料库处理，将txt转csv
"""

import re

import pandas as pd

if __name__ == '__main__':
    with open('news.txt', 'r', encoding='gbk') as f:
        raw_data = f.read()

        urls = []
        docnos = []
        titles = []
        contents = []

        all_items = re.findall("<doc>(.*?)</doc>", raw_data, re.S)
        for item in all_items:
            url = re.findall("<url>(.*?)</url>", item)
            urls.append(url[0])
            docno = re.findall("<docno>(.*?)</docno>", item)
            docnos.append(docno[0])
            title = re.findall("<contenttitle>(.*?)</contenttitle>", item)
            titles.append(title[0])
            content = re.findall("<content>(.*?)</content>", item, re.S)
            contents.append(content[0].replace('\n', ''))

        # 拼接成csv 方式一：
        url_column = pd.Series(urls, name='url')
        docno_column = pd.Series(docnos, name='docno')
        title_column = pd.Series(titles, name='title')
        content_column = pd.Series(contents, name='content')
        news = pd.concat([url_column, docno_column, title_column, content_column], axis=1)
        news.to_csv('news.csv', index=False)

        # 拼接成csv 方式二：
        news = pd.DataFrame({'url': urls, 'docno': docnos, 'title': titles, 'content': contents})
        news.to_csv('news2.csv', index=False)
