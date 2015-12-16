# -*- coding: utf-8 -*-
from mainGUI import *
import sys
import urllib2
from kakaoText import kakaoText

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class myMainGui(Ui_MainWindow):
    def myInit(self):
        self.tabWidget.dragEnterEvent = self.dragEnterEvent
        self.tabWidget.dropEvent = self.dropEvent
        self.timelineTables = []
        QtCore.QObject.connect(self.runSqlButton, QtCore.SIGNAL("clicked()"), self.runSql)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            url = e.mimeData().urls()[0]
            if '.txt' in url.toString():
                e.accept()

    def dropEvent(self, e):
        print 'dropevent!'
        try:
            del self.kakaoText
        except:
            pass

        '''기존정보 삭제'''
        self.sqlResultTable.clearContents()
        self.sqlResultTable.clear()
        self.sqlResultTable.setColumnCount(0)
        self.sqlResultTable.setRowCount(0)
        self.timelineTabs.clear()

        url = e.mimeData().urls()[0]
        filePath = str(url.toString())
        f = urllib2.urlopen(filePath)
        self.kakaoText = kakaoText(f.read())
        self.kakaoText.getBaseInfo()
        self.kakaoText.splitByDate()

        self.allTimelineTable.setColumnCount(7)
        self.allTimelineTable.setRowCount(24)
        self.allTimelineTable.horizontalHeader().setDefaultSectionSize(50)
        self.allTimelineTable.horizontalHeader().setMinimumSectionSize(30)
        self.allTimelineTable.verticalHeader().setDefaultSectionSize(20)
        dowText = [u'월요일', u'화요일', u'수요일', u'목요일', u'금요일', u'토요일', u'일요일']

        '''전체타임라인 설정'''
        for n in range(7):
            item = QtGui.QTableWidgetItem(dowText[n])
            self.allTimelineTable.setHorizontalHeaderItem(n, item)
        for n in range(24):
            item = QtGui.QTableWidgetItem(u'%02d시' % n)
            self.allTimelineTable.setVerticalHeaderItem(n, item)

        self.kakaoText.execute('SELECT dow,hour,count(*) from chat group by dow,hour order by dow, hour')
        sqlret = self.kakaoText.cur.fetchall()
        chatCountMax = 0
        for dow, hour, chatCount in sqlret:
            if chatCountMax < chatCount:
                chatCountMax = chatCount

        for dow, hour, chatCount in sqlret:
            timelineTable = self.allTimelineTable
            value = float(chatCount) / chatCountMax
            item = QtGui.QTableWidgetItem('%0.2f' % value)
            timelineTable.setItem(hour, dow, item)
            color = QtGui.QColor()
            color.setHsl(0, 255, 255 - (value * 255 / 2))
            timelineTable.item(hour, dow).setBackground(color)

        '''개인 타임라인 설정'''
        for user in self.kakaoText.users:
            timelineTab = QtGui.QWidget()
            timelineTable = QtGui.QTableWidget(timelineTab)
            self.timelineTabs.addTab(timelineTab, user)
            self.timelineTables.append(timelineTable)
            timelineTable.setColumnCount(7)
            timelineTable.setRowCount(24)
            timelineTable.horizontalHeader().setDefaultSectionSize(50)
            timelineTable.horizontalHeader().setMinimumSectionSize(30)
            timelineTable.verticalHeader().setDefaultSectionSize(20)
            for n in range(7):
                item = QtGui.QTableWidgetItem(dowText[n])
                timelineTable.setHorizontalHeaderItem(n, item)
            for n in range(24):
                item = QtGui.QTableWidgetItem(u'%02d시' % n)
                timelineTable.setVerticalHeaderItem(n, item)
            layout = QtGui.QGridLayout(timelineTab)
            layout.addWidget(timelineTable, 0, 0, 1, 1)

        dictForTabText = {}
        for n in range(self.timelineTabs.count()):
            tabText = unicode(self.timelineTabs.tabText(n))
            dictForTabText[tabText] = n

        self.kakaoText.execute('SELECT user,dow,hour,count(*) from chat group by user,dow,hour order by user, dow, hour')
        sqlret = self.kakaoText.cur.fetchall()
        chatCountMaxTable = {}
        for user, dow, hour, chatCount in sqlret:
            if user not in chatCountMaxTable:
                chatCountMaxTable[user] = 0
            if chatCountMaxTable[user] < chatCount:
                chatCountMaxTable[user] = chatCount

        for user, dow, hour, chatCount in sqlret:
            timelineTable = self.timelineTables[dictForTabText[user]]
            value = float(chatCount) / chatCountMaxTable[user]
            item = QtGui.QTableWidgetItem('%0.2f' % value)
            timelineTable.setItem(hour, dow, item)
            color = QtGui.QColor()
            color.setHsl(0, 255, 255 - (value * 255 / 2))
            timelineTable.item(hour, dow).setBackground(color)

    def runSql(self):
        query = self.sqlQueryTextbox.text()
        query = unicode(query)
        self.kakaoText.execute(query)
        num_fields = len(self.kakaoText.cur.description)
        field_names = [i[0] for i in self.kakaoText.cur.description]
        queryRet = self.kakaoText.cur.fetchall()
        self.sqlResultTable.setColumnCount(num_fields)
        self.sqlResultTable.setRowCount(len(queryRet))
        for n, fieldName in enumerate(field_names):
            item = QtGui.QTableWidgetItem(fieldName)
            self.sqlResultTable.setHorizontalHeaderItem(n, item)
        for n, item in enumerate(queryRet):
            for m, text in enumerate(item):
                if not isinstance(text, unicode):
                    text = str(text)
                item = QtGui.QTableWidgetItem(text)
                self.sqlResultTable.setItem(n, m, item)


class analyzeThread(QtCore.QThread):
    '''카톡 분석하는 쓰레드
    전부 self에 박음'''
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = myMainGui()
    ui.setupUi(MainWindow)
    ui.myInit()
    MainWindow.show()
    sys.exit(app.exec_())
