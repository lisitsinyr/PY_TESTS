"""
There are some concepts to be clarified

[QT signal & slot] VS [Python signal & slot]

All the predefined signals & slots provided by pyqt are implemented by QT's c++ code. Whenever you want to have a customized signal & slot in Python, it is a python signal & slot. Hence there are four cases to emits a signal to a slot:

from a QT signal to a QT slot
from a QT signal to a Python slot
from a Python signal to a QT slot
from a Python signal to a Python slot
The code below shows how to connect for these four different scnarios

Conclusion is --

Signal signature for Python signal differentiate from that of QT signal in that it doesn't have the parenthesis and can be passed any python data types when you emit it. The Python signal is created when you emit it.

For slot, there are three forms of signatures.

s.connect(w, SIGNAL("signalSignature"), functionName)
s.connect(w,SIGNAL("signalSignature"), instance.methodName)
s.connect(w,SIGNAL("signalSignature"), instance, SLOT("slotSignature"))
Number 1 & 2 are available for Python slot, while number 2 & 3 are available for QT slot. It is clear that besides QT predefined slot, any python callable function/methods is qulified to be a Python slot.

These points are made in Summerfield's article on Signals and Slots.

[Old style qt signal & slot] VS [new style qt singal & slot]

Well, all the description above is based on the old style pyqt signal & slot. As @Idan K suggested there is an alternative new-style to do the things, especially for the Python signal. Refer to here for more.
"""

import sys
from  PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QObject, QThread, Signal, Slot,
    QStringListModel, QModelIndex)

from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,
    QClipboard)
from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QHBoxLayout, QVBoxLayout,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton, QDial, QSpinBox,
    QWidget, QLabel)

# from PySide6.QtCore import *
# from PySide6.QtGui import *

class Foo(QObject):

    def __init__(self, parent=None):
        super(Foo, self).__init__(parent)
        dial = QDial()
        self.spinbox = QSpinBox()

        # --------------------------------------
        # QT signal & QT slot
        # --------------------------------------

        # option 1: more efficient
        self.connect(self.spinbox, QtCore.Signal("valueChanged(int)"), dial, Signal("setValue(int)"))
        # option 2:
        self.connect(self.spinbox, Signal("valueChanged(int)"), dial.setValue)

        # --------------------------------------
        # QT signal & Python slot
        # --------------------------------------

        self.connect(self.spinbox, SIGNAL("valueChanged(int)"), self.myValChanged)


        # --------------------------------------
        # Python signal & Qt slot
        # --------------------------------------

        # connect option 1: more efficient
        self.connect(self, SIGNAL("mysignal"), dial, SLOT("setValue(int)"))

        # connect option 2:
        self.connect(self, SIGNAL("mysignal"), dial.setValue)

        # emit
        param = 100
        self.emit(SIGNAL("mysignal"), param)

        # --------------------------------------
        # Python signal & Python slot
        # --------------------------------------

        # connect
        self.connect(self, SIGNAL("mysignal"), self.myValChanged)

        # emit
        param = 100
        self.emit(SIGNAL("mysignal"), param)


def myValChanged(self):
    print ("New spin val entered {0}".format(self.spinbox.value())
