# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bvv\Documents\hygge_projekt_skrabet\GUI\GUI\mainwindow.ui'
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
        MainWindow.resize(1911, 983)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Pictures/Soccer-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("font: 12pt \"Roboto\";\n"
"\n"
"\n"
"\n"
"/*\n"
"QPushButton, QListWidget{\n"
"            margin: 1px;\n"
"            border-color: #0c457e;\n"
"            border-style: outset;\n"
"            border-radius: 3px;\n"
"           border-width: 1px;\n"
"           color: black;\n"
"min-height:24;\n"
"        }"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1841, 751))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.canvasLayout = QtGui.QVBoxLayout()
        self.canvasLayout.setMargin(11)
        self.canvasLayout.setSpacing(6)
        self.canvasLayout.setObjectName(_fromUtf8("canvasLayout"))
        self.horizontalLayout.addLayout(self.canvasLayout)
        self.tabWidget = QtGui.QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mainTab = QtGui.QWidget()
        self.mainTab.setObjectName(_fromUtf8("mainTab"))
        self.layoutWidget_2 = QtGui.QWidget(self.mainTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 460, 372, 81))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.mainTabLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.mainTabLayout_3.setMargin(6)
        self.mainTabLayout_3.setSpacing(6)
        self.mainTabLayout_3.setObjectName(_fromUtf8("mainTabLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setMargin(5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.tenSecBack_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.tenSecBack_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tenSecBack_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tenSecBack_4.setObjectName(_fromUtf8("tenSecBack_4"))
        self.horizontalLayout_7.addWidget(self.tenSecBack_4)
        self.fiveSecBack_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.fiveSecBack_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fiveSecBack_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fiveSecBack_4.setObjectName(_fromUtf8("fiveSecBack_4"))
        self.horizontalLayout_7.addWidget(self.fiveSecBack_4)
        self.pauseButton_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.pauseButton_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseButton_4.setObjectName(_fromUtf8("pauseButton_4"))
        self.horizontalLayout_7.addWidget(self.pauseButton_4)
        self.fiveSecForward_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.fiveSecForward_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fiveSecForward_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fiveSecForward_4.setObjectName(_fromUtf8("fiveSecForward_4"))
        self.horizontalLayout_7.addWidget(self.fiveSecForward_4)
        self.tenSecForward_4 = QtGui.QPushButton(self.layoutWidget_2)
        self.tenSecForward_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tenSecForward_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tenSecForward_4.setObjectName(_fromUtf8("tenSecForward_4"))
        self.horizontalLayout_7.addWidget(self.tenSecForward_4)
        self.mainTabLayout_3.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.mainTab, _fromUtf8(""))
        self.toolboxTab = QtGui.QWidget()
        self.toolboxTab.setStyleSheet(_fromUtf8(""))
        self.toolboxTab.setObjectName(_fromUtf8("toolboxTab"))
        self.voronoiButton = QtGui.QPushButton(self.toolboxTab)
        self.voronoiButton.setGeometry(QtCore.QRect(30, 30, 321, 101))
        self.voronoiButton.setStyleSheet(_fromUtf8(""))
        self.voronoiButton.setObjectName(_fromUtf8("voronoiButton"))
        self.triangledey = QtGui.QPushButton(self.toolboxTab)
        self.triangledey.setGeometry(QtCore.QRect(30, 150, 321, 101))
        self.triangledey.setStyleSheet(_fromUtf8(""))
        self.triangledey.setObjectName(_fromUtf8("triangledey"))
        self.convex = QtGui.QPushButton(self.toolboxTab)
        self.convex.setGeometry(QtCore.QRect(30, 270, 321, 101))
        self.convex.setStyleSheet(_fromUtf8(""))
        self.convex.setObjectName(_fromUtf8("convex"))
        self.tabWidget.addTab(self.toolboxTab, _fromUtf8(""))
        self.statsTab = QtGui.QWidget()
        self.statsTab.setObjectName(_fromUtf8("statsTab"))
        self.scrollArea = QtGui.QScrollArea(self.statsTab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 641, 711))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 2204))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.NNbutton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.NNbutton.setPalette(palette)
        self.NNbutton.setAutoFillBackground(False)
        self.NNbutton.setStyleSheet(_fromUtf8("background-color: rgb(235, 235, 235);"))
        self.NNbutton.setObjectName(_fromUtf8("NNbutton"))
        self.verticalLayout_2.addWidget(self.NNbutton)
        self.mplwindow = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl_3 = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl_3.setMargin(0)
        self.mplvl_3.setSpacing(0)
        self.mplvl_3.setObjectName(_fromUtf8("mplvl_3"))
        self.verticalLayout_2.addWidget(self.mplwindow)
        self.mplwindow_2 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_2.sizePolicy().hasHeightForWidth())
        self.mplwindow_2.setSizePolicy(sizePolicy)
        self.mplwindow_2.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_2.setObjectName(_fromUtf8("mplwindow_2"))
        self.mplvl_4 = QtGui.QVBoxLayout(self.mplwindow_2)
        self.mplvl_4.setMargin(0)
        self.mplvl_4.setSpacing(0)
        self.mplvl_4.setObjectName(_fromUtf8("mplvl_4"))
        self.verticalLayout_2.addWidget(self.mplwindow_2)
        self.mplwindow_3 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_3.sizePolicy().hasHeightForWidth())
        self.mplwindow_3.setSizePolicy(sizePolicy)
        self.mplwindow_3.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_3.setObjectName(_fromUtf8("mplwindow_3"))
        self.mplvl_5 = QtGui.QVBoxLayout(self.mplwindow_3)
        self.mplvl_5.setMargin(0)
        self.mplvl_5.setSpacing(6)
        self.mplvl_5.setObjectName(_fromUtf8("mplvl_5"))
        self.verticalLayout_2.addWidget(self.mplwindow_3)
        self.mplwindow_4 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_4.sizePolicy().hasHeightForWidth())
        self.mplwindow_4.setSizePolicy(sizePolicy)
        self.mplwindow_4.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_4.setObjectName(_fromUtf8("mplwindow_4"))
        self.mplvl_6 = QtGui.QVBoxLayout(self.mplwindow_4)
        self.mplvl_6.setMargin(0)
        self.mplvl_6.setSpacing(6)
        self.mplvl_6.setObjectName(_fromUtf8("mplvl_6"))
        self.verticalLayout_2.addWidget(self.mplwindow_4)
        self.mplwindow_5 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_5.sizePolicy().hasHeightForWidth())
        self.mplwindow_5.setSizePolicy(sizePolicy)
        self.mplwindow_5.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_5.setObjectName(_fromUtf8("mplwindow_5"))
        self.mplvl_7 = QtGui.QVBoxLayout(self.mplwindow_5)
        self.mplvl_7.setMargin(0)
        self.mplvl_7.setSpacing(6)
        self.mplvl_7.setObjectName(_fromUtf8("mplvl_7"))
        self.verticalLayout_2.addWidget(self.mplwindow_5)
        self.mplwindow_6 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_6.sizePolicy().hasHeightForWidth())
        self.mplwindow_6.setSizePolicy(sizePolicy)
        self.mplwindow_6.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_6.setObjectName(_fromUtf8("mplwindow_6"))
        self.mplvl_8 = QtGui.QVBoxLayout(self.mplwindow_6)
        self.mplvl_8.setMargin(0)
        self.mplvl_8.setSpacing(6)
        self.mplvl_8.setObjectName(_fromUtf8("mplvl_8"))
        self.verticalLayout_2.addWidget(self.mplwindow_6)
        self.mplwindow_7 = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_7.sizePolicy().hasHeightForWidth())
        self.mplwindow_7.setSizePolicy(sizePolicy)
        self.mplwindow_7.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_7.setObjectName(_fromUtf8("mplwindow_7"))
        self.mplvl_9 = QtGui.QVBoxLayout(self.mplwindow_7)
        self.mplvl_9.setMargin(0)
        self.mplvl_9.setSpacing(6)
        self.mplvl_9.setObjectName(_fromUtf8("mplvl_9"))
        self.verticalLayout_2.addWidget(self.mplwindow_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.statsTab, _fromUtf8(""))
        self.syncTab = QtGui.QWidget()
        self.syncTab.setObjectName(_fromUtf8("syncTab"))
        self.scrollArea_2 = QtGui.QScrollArea(self.syncTab)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 641, 711))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 618, 2204))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.NNbutton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.NNbutton_2.setPalette(palette)
        self.NNbutton_2.setAutoFillBackground(False)
        self.NNbutton_2.setStyleSheet(_fromUtf8("background-color: rgb(235, 235, 235);"))
        self.NNbutton_2.setObjectName(_fromUtf8("NNbutton_2"))
        self.verticalLayout_3.addWidget(self.NNbutton_2)
        self.mplwindow_8 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_8.sizePolicy().hasHeightForWidth())
        self.mplwindow_8.setSizePolicy(sizePolicy)
        self.mplwindow_8.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_8.setObjectName(_fromUtf8("mplwindow_8"))
        self.mplvl_10 = QtGui.QVBoxLayout(self.mplwindow_8)
        self.mplvl_10.setMargin(0)
        self.mplvl_10.setSpacing(0)
        self.mplvl_10.setObjectName(_fromUtf8("mplvl_10"))
        self.verticalLayout_3.addWidget(self.mplwindow_8)
        self.mplwindow_9 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_9.sizePolicy().hasHeightForWidth())
        self.mplwindow_9.setSizePolicy(sizePolicy)
        self.mplwindow_9.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_9.setObjectName(_fromUtf8("mplwindow_9"))
        self.mplvl_11 = QtGui.QVBoxLayout(self.mplwindow_9)
        self.mplvl_11.setMargin(0)
        self.mplvl_11.setSpacing(0)
        self.mplvl_11.setObjectName(_fromUtf8("mplvl_11"))
        self.verticalLayout_3.addWidget(self.mplwindow_9)
        self.mplwindow_10 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_10.sizePolicy().hasHeightForWidth())
        self.mplwindow_10.setSizePolicy(sizePolicy)
        self.mplwindow_10.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_10.setObjectName(_fromUtf8("mplwindow_10"))
        self.mplvl_12 = QtGui.QVBoxLayout(self.mplwindow_10)
        self.mplvl_12.setMargin(0)
        self.mplvl_12.setSpacing(6)
        self.mplvl_12.setObjectName(_fromUtf8("mplvl_12"))
        self.verticalLayout_3.addWidget(self.mplwindow_10)
        self.mplwindow_11 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_11.sizePolicy().hasHeightForWidth())
        self.mplwindow_11.setSizePolicy(sizePolicy)
        self.mplwindow_11.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_11.setObjectName(_fromUtf8("mplwindow_11"))
        self.mplvl_13 = QtGui.QVBoxLayout(self.mplwindow_11)
        self.mplvl_13.setMargin(0)
        self.mplvl_13.setSpacing(6)
        self.mplvl_13.setObjectName(_fromUtf8("mplvl_13"))
        self.verticalLayout_3.addWidget(self.mplwindow_11)
        self.mplwindow_12 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_12.sizePolicy().hasHeightForWidth())
        self.mplwindow_12.setSizePolicy(sizePolicy)
        self.mplwindow_12.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_12.setObjectName(_fromUtf8("mplwindow_12"))
        self.mplvl_14 = QtGui.QVBoxLayout(self.mplwindow_12)
        self.mplvl_14.setMargin(0)
        self.mplvl_14.setSpacing(6)
        self.mplvl_14.setObjectName(_fromUtf8("mplvl_14"))
        self.verticalLayout_3.addWidget(self.mplwindow_12)
        self.mplwindow_13 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_13.sizePolicy().hasHeightForWidth())
        self.mplwindow_13.setSizePolicy(sizePolicy)
        self.mplwindow_13.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_13.setObjectName(_fromUtf8("mplwindow_13"))
        self.mplvl_15 = QtGui.QVBoxLayout(self.mplwindow_13)
        self.mplvl_15.setMargin(0)
        self.mplvl_15.setSpacing(6)
        self.mplvl_15.setObjectName(_fromUtf8("mplvl_15"))
        self.verticalLayout_3.addWidget(self.mplwindow_13)
        self.mplwindow_14 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow_14.sizePolicy().hasHeightForWidth())
        self.mplwindow_14.setSizePolicy(sizePolicy)
        self.mplwindow_14.setMinimumSize(QtCore.QSize(400, 300))
        self.mplwindow_14.setObjectName(_fromUtf8("mplwindow_14"))
        self.mplvl_16 = QtGui.QVBoxLayout(self.mplwindow_14)
        self.mplvl_16.setMargin(0)
        self.mplvl_16.setSpacing(6)
        self.mplvl_16.setObjectName(_fromUtf8("mplvl_16"))
        self.verticalLayout_3.addWidget(self.mplwindow_14)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.syncTab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.layoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(320, 750, 372, 81))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.mainTabLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.mainTabLayout_5.setMargin(6)
        self.mainTabLayout_5.setSpacing(6)
        self.mainTabLayout_5.setObjectName(_fromUtf8("mainTabLayout_5"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setMargin(5)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.tenSecBack_9 = QtGui.QPushButton(self.layoutWidget_3)
        self.tenSecBack_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tenSecBack_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tenSecBack_9.setObjectName(_fromUtf8("tenSecBack_9"))
        self.horizontalLayout_12.addWidget(self.tenSecBack_9)
        self.fiveSecBack_9 = QtGui.QPushButton(self.layoutWidget_3)
        self.fiveSecBack_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fiveSecBack_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fiveSecBack_9.setObjectName(_fromUtf8("fiveSecBack_9"))
        self.horizontalLayout_12.addWidget(self.fiveSecBack_9)
        self.pauseButton_9 = QtGui.QPushButton(self.layoutWidget_3)
        self.pauseButton_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pauseButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseButton_9.setObjectName(_fromUtf8("pauseButton_9"))
        self.horizontalLayout_12.addWidget(self.pauseButton_9)
        self.fiveSecForward_9 = QtGui.QPushButton(self.layoutWidget_3)
        self.fiveSecForward_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fiveSecForward_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fiveSecForward_9.setObjectName(_fromUtf8("fiveSecForward_9"))
        self.horizontalLayout_12.addWidget(self.fiveSecForward_9)
        self.tenSecForward_9 = QtGui.QPushButton(self.layoutWidget_3)
        self.tenSecForward_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tenSecForward_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tenSecForward_9.setObjectName(_fromUtf8("tenSecForward_9"))
        self.horizontalLayout_12.addWidget(self.tenSecForward_9)
        self.mainTabLayout_5.addLayout(self.horizontalLayout_12)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 830, 1031, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1911, 30))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tenSecBack_4.setText(_translate("MainWindow", "<<", None))
        self.fiveSecBack_4.setText(_translate("MainWindow", "<", None))
        self.pauseButton_4.setText(_translate("MainWindow", "||", None))
        self.fiveSecForward_4.setText(_translate("MainWindow", ">", None))
        self.tenSecForward_4.setText(_translate("MainWindow", ">>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("MainWindow", "Video", None))
        self.voronoiButton.setText(_translate("MainWindow", "Voronoi", None))
        self.triangledey.setText(_translate("MainWindow", "Delauney Triangulation", None))
        self.convex.setText(_translate("MainWindow", "Convex Hull", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolboxTab), _translate("MainWindow", "Toolbox", None))
        self.NNbutton.setText(_translate("MainWindow", "Find lignende situation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statsTab), _translate("MainWindow", "Find situation - BIF", None))
        self.NNbutton_2.setText(_translate("MainWindow", "Find lignende situation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.syncTab), _translate("MainWindow", "Find situation - Modstander", None))
        self.tenSecBack_9.setText(_translate("MainWindow", "<<", None))
        self.fiveSecBack_9.setText(_translate("MainWindow", "<", None))
        self.pauseButton_9.setText(_translate("MainWindow", "||", None))
        self.fiveSecForward_9.setText(_translate("MainWindow", ">", None))
        self.tenSecForward_9.setText(_translate("MainWindow", ">>", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))

