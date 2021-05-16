# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomedialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 382)
        Dialog.setStyleSheet(_fromUtf8("\n"
"font: 12pt \"Roboto\";\n"
"/*background-color: rgb(255, 255, 255);\n"
"\n"
"QPushButton, QDialogButtonBox:Ok {\n"
"            margin: 1px;\n"
"            background-color:#cafbfc;\n"
"            border-color: #0c457e;\n"
"            border-style: outset;\n"
"            border-radius: 3px;\n"
"           border-width: 1px;\n"
"           color: black;\n"
"        }"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 330, 341, 41))
        self.buttonBox.setStyleSheet(_fromUtf8("/*\n"
"QPushButton {\n"
"            margin: 1px;\n"
"            border-color: #0c457e;\n"
"            border-style: outset;\n"
"            border-radius: 3px;\n"
"           border-width: 1px;\n"
"           color: black;\n"
"min-width:70;\n"
"min-height:24;\n"
"        }"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.selectButton = QtGui.QPushButton(Dialog)
        self.selectButton.setGeometry(QtCore.QRect(100, 10, 211, 31))
        self.selectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectButton.setStyleSheet(_fromUtf8("/*\n"
"\n"
"QPushButton {\n"
"            margin: 1px;\n"
"            border-color: #0c457e;\n"
"            border-style: outset;\n"
"            border-radius: 3px;\n"
"           border-width: 1px;\n"
"           color: black;\n"
"        }"))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gameLabel = QtGui.QLabel(Dialog)
        self.gameLabel.setGeometry(QtCore.QRect(0, 90, 401, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet(_fromUtf8("font: 13pt \"Roboto\";"))
        self.gameLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gameLabel.setObjectName(_fromUtf8("gameLabel"))
        self.icon_label = QtGui.QLabel(Dialog)
        self.icon_label.setGeometry(QtCore.QRect(116, 227, 51, 51))
        self.icon_label.setText(_fromUtf8(""))
        self.icon_label.setObjectName(_fromUtf8("icon_label"))
        self.synced_label = QtGui.QLabel(Dialog)
        self.synced_label.setGeometry(QtCore.QRect(180, 240, 191, 21))
        self.synced_label.setStyleSheet(_fromUtf8("font: 13pt \"Roboto\";"))
        self.synced_label.setText(_fromUtf8(""))
        self.synced_label.setObjectName(_fromUtf8("synced_label"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(70, 310, 271, 20))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.wait_label = QtGui.QLabel(Dialog)
        self.wait_label.setGeometry(QtCore.QRect(66, 289, 281, 21))
        self.wait_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wait_label.setObjectName(_fromUtf8("wait_label"))
        self.loadButton = QtGui.QPushButton(Dialog)
        self.loadButton.setEnabled(False)
        self.loadButton.setGeometry(QtCore.QRect(100, 50, 211, 31))
        self.loadButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loadButton.setStyleSheet(_fromUtf8("/*\n"
"\n"
"QPushButton {\n"
"            margin: 1px;\n"
"            border-color: #0c457e;\n"
"            border-style: outset;\n"
"            border-radius: 3px;\n"
"           border-width: 1px;\n"
"           color: black;\n"
"        }"))
        self.loadButton.setCheckable(False)
        self.loadButton.setChecked(False)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectButton.setText(_translate("Dialog", "Select Game", None))
        self.gameLabel.setText(_translate("Dialog", "No game selected", None))
        self.wait_label.setText(_translate("Dialog", "Loading a game, this may take a while", None))
        self.loadButton.setToolTip(_translate("Dialog", "First select a game to load", None))
        self.loadButton.setText(_translate("Dialog", "Load Game", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

