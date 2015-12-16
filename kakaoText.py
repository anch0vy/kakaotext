# -*- coding: utf-8 -*-
import arrow
import re
import collections
import ujson
import sqlite3
from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query
from dateutil import tz

class kakaoText():
    '''카카오톡 글 분석하는 클래스'''
    def __init__(self, text):
        self.text = unicode(text, 'utf-8')
        self.isKakaoChat = False
        self.isGroupChat = None
        self.users = []
        self.textByDate = {}
        self.conn = sqlite3.connect(':memory:')
        self.commit = self.conn.commit
        self.cur = self.conn.cursor()
        self.execute = self.cur.execute

        sql = 'CREATE TABLE chat(user text, time INTEGER, text text, year INTEGER, month INTEGER, day INTEGER, hour INTEGER, dow INTEGER)'
        '''dow : day of week, 0~6, 월~일'''
        self.execute(sql)


    def getBaseInfo(self):
        '''저장한날, 그룹채팅인지 파싱'''
        rawBaseInfo = self.text.split('\n')[:2]
        if u'그룹채팅' in rawBaseInfo[0]:
            self.isGroupChat = True
            reret = re.search(u'그룹채팅 - (.*) 님과', rawBaseInfo[0])
        else:
            self.isGroupChat = False
            reret = re.search(u'^(.*) 님과', rawBaseInfo[0])
        if reret is None:
            self.isKakaoChat = False
            return

    def splitByDate(self):
        """채팅을 날자별로 사전에 넣음. 사전에 들어가는건 리스트"""
        rawTexts = self.text.split('\n')[2:]
        textByDateList = []
        newDate = None
        text = ''
        ctimeobject = arrow.get(0)
        for rawText in rawTexts:
            if rawText.startswith(u'---------------'):
                if newDate is not None:
                    self.textByDate[newDate] = textByDateList
                textByDateList = []
                reret = re.search(u'\-{15} (.*)년 (.*)월 (.*)일 (.*) \-{15}', rawText)
                ymd = reret.group(1), reret.group(2), reret.group(3)
                ymd = map(int, ymd)
                timeobject = arrow.get(*ymd)
                newDate = timeobject.timestamp

            elif rawText.startswith(u'[') and rawText.count(u'[') >= 2:
                if text:
                    reret = re.search(u'\[(.*?)\] \[(.*?)\] (.*)', text, re.MULTILINE)
                    if reret is None:
                        text = text + '\n' + rawText
                        continue
                    user, rawTime, text_read = reret.group(1), reret.group(2), reret.group(3)
                    isPM, hm = rawTime.split(' ')
                    hour, min = map(int, hm.split(':'))
                    isPM = isPM == u'오후'
                    time = newDate + (isPM * 12 + hour) * 3600 + min * 60
                    ctimeobject = arrow.get(time, tzinfo = tz.tzlocal())
                    q = 'INSERT INTO chat (user, time, text, year, month, day, hour, dow) VALUES (?,?,?,?,?,?,?,?)'
                    arg = (user, time, text_read, ctimeobject.year, ctimeobject.month, ctimeobject.day, ctimeobject.hour, ctimeobject.weekday())
                    self.execute(q,arg)
                text = rawText
            else:
                text = text + '\n' + rawText
        self.commit()
        q = 'SELECT user as count from chat group by user'
        self.execute(q)
        for ret in self.cur:
            self.users.append(ret[0])

    def getWord(self):
        pass

    def getChatCount(self):
        '''
        q_day  : 날자별
        q_hour : 유저별
        q_user : 시간별
        q_user_hour : 유저로 나눈걸 시간으로 나눔
        q_user_dow_hour : 유저로 나눈걸 요일로 나눈뒤 시간으로 나눔 -> heatmap
        ?? : 말이 바이트로 많은사람
        ?? : 한문장이 짧은사람 긴사람
        '''
        q_day = 'SELECT year,month,day,count(*) as count from chat group by year||month||day order by time'
        q_hour = 'SELECT hour,count(*) as count from chat group by hour order by hour'
        q_user = 'SELECT user,count(*) as count from chat group by user order by user'
        q_user_dow_hour = 'SELECT user,dow,hour,count(*) from chat group by user,dow,hour order by user, dow, hour'

if __name__ == '__main__':
    import json
    k = kakaoText(open('test.txt','r').read())
    k.getBaseInfo()
    k.splitByDate()
    k.getChatCount()
    print json.dumps(k.users)
