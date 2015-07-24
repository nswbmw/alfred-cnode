#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import json

BASEURL = u'https://cnodejs.org'
URL = u'https://cnodejs.org/api/v1/topics?limit=20&mdrender=false'
TAB = { u'good': u'精华', u'share': u'分享', 'ask': u'问答', u'job': u'招聘' }

def main():
    query = u'{query}'
    if not query.strip() or query not in [u'good', u'share', u'ask', u'job']:
        query = u'all'

    data = json.loads(urllib2.urlopen(u'%s&tab=%s' % (URL, query)).read())[u'data']
    result = [u'<?xml version="1.0"?><items>']
    for i in data:
        template = u'<item uid="%s" arg="%s"><title>[%s] %s</title><subtitle>阅读: %d | 回复: %d | 最后回复: %s</subtitle><icon>icon.png</icon></item>' % (
            i[u'id'],
            i[u'id'],
            TAB.get(i.get(u'tab', u'share')),
            i[u'title'],
            i[u'visit_count'],
            i[u'reply_count'],
            i[u'last_reply_at'][11:16]
            )
        result.append(template)
    result.append(u'</items>')
    print(''.join(result))

if __name__ == "__main__":
    main()