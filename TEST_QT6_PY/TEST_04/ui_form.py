# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_Youtube = QAction(MainWindow)
        self.action_Youtube.setObjectName(u"action_Youtube")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Exit.setCheckable(True)
        self.action_Exit.setProperty("clicked()", False)
        self.action_Action_Cut = QAction(MainWindow)
        self.action_Action_Cut.setObjectName(u"action_Action_Cut")
        self.action_Action_Copy = QAction(MainWindow)
        self.action_Action_Copy.setObjectName(u"action_Action_Copy")
        self.action_Action_Paste = QAction(MainWindow)
        self.action_Action_Paste.setObjectName(u"action_Action_Paste")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_Youtube)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Action_Cut)
        self.menu_Edit.addAction(self.action_Action_Copy)
        self.menu_Edit.addAction(self.action_Action_Paste)

        self.retranslateUi(MainWindow)
        self.action_Exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Youtube.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0437\u0434\u0430\u0442\u044c Youtube", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_Action_Cut.setText(QCoreApplication.translate("MainWindow", u"Action_Cut", None))
        self.action_Action_Copy.setText(QCoreApplication.translate("MainWindow", u"Action_Copy", None))
        self.action_Action_Paste.setText(QCoreApplication.translate("MainWindow", u"Action_Paste", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

