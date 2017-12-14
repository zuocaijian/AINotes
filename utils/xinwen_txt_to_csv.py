# -*- coding:utf-8 -*-

"""
author:zcj
create:2017.12.15
fun:处理搜狗新闻语料库，将txt转换为csv
"""

import re

import pandas as pd

if __name__ == '__main__':
    with open('xinwen.txt', mode='r', encoding='gbk') as f:
        raw_data = f.read()
        urls = []
        docnos = []
        titles = []
        contents = []

        result = re.findall("<doc>(.*?)</doc>", raw_data, re.S)
        for item in result:
            url = re.findall("<url>(.*?)</url>", item)
            urls.append(url[0])
            docno = re.findall("<docno>(.*?)</docno>", item)
            docnos.append(docno[0])
            title = re.findall("<contenttitle>(.*?)</contenttitle>", item)
            titles.append(title[0])
            content = re.findall("<content>(.*?)</content>", item, re.S)
            contents.append(content[0].replace('\n', ''))

    # way 1
    url_column = pd.Series(urls, name='url')
    docno_column = pd.Series(docnos, name='docno')
    title_column = pd.Series(titles, name='title')
    content_column = pd.Series(contents, name='content')
    data = pd.concat([url_column, docno_column, title_column, content_column], axis=1)
    data.to_csv('xinwen.csv', index=False, encoding='utf-8')

    # way 2 会自己按照列名重新排序
    data = pd.DataFrame({'url': urls, 'docno:': docnos, 'title': titles, 'content': contents})
    data.to_csv('xinwen2.csv', index=False)
