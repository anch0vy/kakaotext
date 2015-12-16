# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = FingerTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setMouseTracking(False)
        self.tab1.setAcceptDrops(True)
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab1)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.textBrowser = QtGui.QTextBrowser(self.tab1)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setAcceptDrops(True)
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setAcceptDrops(True)
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.allTimelineTable = QtGui.QTableWidget(self.tab)
        self.allTimelineTable.setObjectName(_fromUtf8("allTimelineTable"))
        self.allTimelineTable.setColumnCount(0)
        self.allTimelineTable.setRowCount(0)
        self.gridLayout_3.addWidget(self.allTimelineTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab4 = QtGui.QWidget()
        self.tab4.setAcceptDrops(True)
        self.tab4.setObjectName(_fromUtf8("tab4"))
        self.gridLayout = QtGui.QGridLayout(self.tab4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.timelineTabs = FingerTabWidget(self.tab4)
        self.timelineTabs.setTabPosition(QtGui.QTabWidget.West)
        self.timelineTabs.setObjectName(_fromUtf8("timelineTabs"))
        self.gridLayout.addWidget(self.timelineTabs, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab4, _fromUtf8(""))
        self.tab5 = QtGui.QWidget()
        self.tab5.setObjectName(_fromUtf8("tab5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sqlQueryTextbox = QtGui.QLineEdit(self.tab5)
        self.sqlQueryTextbox.setObjectName(_fromUtf8("sqlQueryTextbox"))
        self.horizontalLayout.addWidget(self.sqlQueryTextbox)
        self.runSqlButton = QtGui.QPushButton(self.tab5)
        self.runSqlButton.setObjectName(_fromUtf8("runSqlButton"))
        self.horizontalLayout.addWidget(self.runSqlButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sqlResultTable = QtGui.QTableWidget(self.tab5)
        self.sqlResultTable.setEnabled(True)
        self.sqlResultTable.setObjectName(_fromUtf8("sqlResultTable"))
        self.sqlResultTable.setColumnCount(0)
        self.sqlResultTable.setRowCount(0)
        self.sqlResultTable.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.sqlResultTable)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab5, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.timelineTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">파일을 여기로 드래그!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "시작", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "단어빈도", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "말이많은사람", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "전체 타임라인", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "개인 타임라인", None))
        self.sqlQueryTextbox.setText(_translate("MainWindow", "SELECT * from chat limit 100", None))
        self.runSqlButton.setText(_translate("MainWindow", "RUN", None))
        self.sqlResultTable.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "custom SQL", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">anch0vy</span></p></body></html>", None))

from FingerTabs import FingerTabWidget
