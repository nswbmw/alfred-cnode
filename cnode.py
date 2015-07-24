# -*- coding: UTF-8 -*-

import urllib2
import json
import string

BASEURL = 'https://cnodejs.org'
URL = 'https://cnodejs.org/api/v1/topics?limit=20&mdrender=false'
TAB = { u'good': u'精华', u'share': u'分享', 'ask': u'问答', u'job': u'招聘' }

def main():
    query = '{query}'
    if not query.strip() or query not in ['good', 'share', 'ask', 'job']:
        query = 'all'

    data = json.loads(urllib2.urlopen(URL + '&tab=' + query).read(), encoding='utf-8')[u'data']
    result = ['<?xml version="1.0"?><items>']
    for i in range(len(data)):
        item = '<item uid="' + data[i][u'id'] + '" arg="' + data[i][u'id'] + '">'
        try:
            tab = data[i][u'tab']
        except:
            tab = u'share'
        title = '<title>[' + TAB[tab] + '] ' + data[i][u'title'] + '</title>'
        subtitle = '<subtitle>' + u'阅读: ' + str(data[i][u'visit_count']) + u' | 回复: ' + str(data[i][u'reply_count']) + u' | 最后回复: ' + data[i][u'last_reply_at'][11:16] + '</subtitle>'
        icon = '<icon>icon.png</icon>'
        result.append(item + title + subtitle + icon + '</item>')

    result.append('</items>')
    print(string.join(result, ''))

if __name__ == "__main__":
    main()