# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_form.ui'
#
# Created: Mon Dec 30 16:52:19 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1007, 264)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gainGroupBox = QtGui.QGroupBox(self.widget)
        self.gainGroupBox.setFlat(False)
        self.gainGroupBox.setObjectName(_fromUtf8("gainGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gainGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.gainGroupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.gainMasterDoubleSpinBox = QtGui.QDoubleSpinBox(self.gainGroupBox)
        self.gainMasterDoubleSpinBox.setDecimals(2)
        self.gainMasterDoubleSpinBox.setMinimum(-99.0)
        self.gainMasterDoubleSpinBox.setProperty("value", 0.0)
        self.gainMasterDoubleSpinBox.setObjectName(_fromUtf8("gainMasterDoubleSpinBox"))
        self.gridLayout.addWidget(self.gainMasterDoubleSpinBox, 0, 1, 1, 1)
        self.gainMasterHorizontalSlider = QtGui.QSlider(self.gainGroupBox)
        self.gainMasterHorizontalSlider.setMinimum(-16)
        self.gainMasterHorizontalSlider.setMaximum(16)
        self.gainMasterHorizontalSlider.setProperty("value", 0)
        self.gainMasterHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gainMasterHorizontalSlider.setObjectName(_fromUtf8("gainMasterHorizontalSlider"))
        self.gridLayout.addWidget(self.gainMasterHorizontalSlider, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gainGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gainRedDoubleSpinBox = QtGui.QDoubleSpinBox(self.gainGroupBox)
        self.gainRedDoubleSpinBox.setDecimals(2)
        self.gainRedDoubleSpinBox.setMinimum(-99.0)
        self.gainRedDoubleSpinBox.setProperty("value", 0.0)
        self.gainRedDoubleSpinBox.setObjectName(_fromUtf8("gainRedDoubleSpinBox"))
        self.gridLayout.addWidget(self.gainRedDoubleSpinBox, 1, 1, 1, 1)
        self.gainRedHorizontalSlider = QtGui.QSlider(self.gainGroupBox)
        self.gainRedHorizontalSlider.setMinimum(-16)
        self.gainRedHorizontalSlider.setMaximum(16)
        self.gainRedHorizontalSlider.setProperty("value", 0)
        self.gainRedHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gainRedHorizontalSlider.setObjectName(_fromUtf8("gainRedHorizontalSlider"))
        self.gridLayout.addWidget(self.gainRedHorizontalSlider, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gainGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gainGreenDoubleSpinBox = QtGui.QDoubleSpinBox(self.gainGroupBox)
        self.gainGreenDoubleSpinBox.setDecimals(2)
        self.gainGreenDoubleSpinBox.setMinimum(-99.0)
        self.gainGreenDoubleSpinBox.setProperty("value", 0.0)
        self.gainGreenDoubleSpinBox.setObjectName(_fromUtf8("gainGreenDoubleSpinBox"))
        self.gridLayout.addWidget(self.gainGreenDoubleSpinBox, 2, 1, 1, 1)
        self.gainGreenHorizontalSlider = QtGui.QSlider(self.gainGroupBox)
        self.gainGreenHorizontalSlider.setMinimum(-16)
        self.gainGreenHorizontalSlider.setMaximum(16)
        self.gainGreenHorizontalSlider.setProperty("value", 0)
        self.gainGreenHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gainGreenHorizontalSlider.setObjectName(_fromUtf8("gainGreenHorizontalSlider"))
        self.gridLayout.addWidget(self.gainGreenHorizontalSlider, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gainGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.gainBlueDoubleSpinBox = QtGui.QDoubleSpinBox(self.gainGroupBox)
        self.gainBlueDoubleSpinBox.setDecimals(2)
        self.gainBlueDoubleSpinBox.setMinimum(-99.0)
        self.gainBlueDoubleSpinBox.setProperty("value", 0.0)
        self.gainBlueDoubleSpinBox.setObjectName(_fromUtf8("gainBlueDoubleSpinBox"))
        self.gridLayout.addWidget(self.gainBlueDoubleSpinBox, 3, 1, 1, 1)
        self.gainBlueHorizontalSlider = QtGui.QSlider(self.gainGroupBox)
        self.gainBlueHorizontalSlider.setMinimum(-16)
        self.gainBlueHorizontalSlider.setMaximum(16)
        self.gainBlueHorizontalSlider.setProperty("value", 0)
        self.gainBlueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gainBlueHorizontalSlider.setObjectName(_fromUtf8("gainBlueHorizontalSlider"))
        self.gridLayout.addWidget(self.gainBlueHorizontalSlider, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.gainGroupBox)
        self.gammaGroupBox = QtGui.QGroupBox(self.widget)
        self.gammaGroupBox.setFlat(False)
        self.gammaGroupBox.setObjectName(_fromUtf8("gammaGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gammaGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_10 = QtGui.QLabel(self.gammaGroupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.gainRedDoubleSpinBox_4 = QtGui.QDoubleSpinBox(self.gammaGroupBox)
        self.gainRedDoubleSpinBox_4.setDecimals(2)
        self.gainRedDoubleSpinBox_4.setMinimum(-99.0)
        self.gainRedDoubleSpinBox_4.setProperty("value", 0.0)
        self.gainRedDoubleSpinBox_4.setObjectName(_fromUtf8("gainRedDoubleSpinBox_4"))
        self.gridLayout_2.addWidget(self.gainRedDoubleSpinBox_4, 0, 1, 1, 1)
        self.gainRedHorizontalSlider_4 = QtGui.QSlider(self.gammaGroupBox)
        self.gainRedHorizontalSlider_4.setMinimum(-16)
        self.gainRedHorizontalSlider_4.setMaximum(16)
        self.gainRedHorizontalSlider_4.setProperty("value", 0)
        self.gainRedHorizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.gainRedHorizontalSlider_4.setObjectName(_fromUtf8("gainRedHorizontalSlider_4"))
        self.gridLayout_2.addWidget(self.gainRedHorizontalSlider_4, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gammaGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.gainRedDoubleSpinBox_2 = QtGui.QDoubleSpinBox(self.gammaGroupBox)
        self.gainRedDoubleSpinBox_2.setDecimals(2)
        self.gainRedDoubleSpinBox_2.setMinimum(-99.0)
        self.gainRedDoubleSpinBox_2.setProperty("value", 0.0)
        self.gainRedDoubleSpinBox_2.setObjectName(_fromUtf8("gainRedDoubleSpinBox_2"))
        self.gridLayout_2.addWidget(self.gainRedDoubleSpinBox_2, 1, 1, 1, 1)
        self.gainRedHorizontalSlider_2 = QtGui.QSlider(self.gammaGroupBox)
        self.gainRedHorizontalSlider_2.setMinimum(-16)
        self.gainRedHorizontalSlider_2.setMaximum(16)
        self.gainRedHorizontalSlider_2.setProperty("value", 0)
        self.gainRedHorizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.gainRedHorizontalSlider_2.setObjectName(_fromUtf8("gainRedHorizontalSlider_2"))
        self.gridLayout_2.addWidget(self.gainRedHorizontalSlider_2, 1, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gammaGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.gainGreenDoubleSpinBox_2 = QtGui.QDoubleSpinBox(self.gammaGroupBox)
        self.gainGreenDoubleSpinBox_2.setDecimals(2)
        self.gainGreenDoubleSpinBox_2.setMinimum(-99.0)
        self.gainGreenDoubleSpinBox_2.setProperty("value", 0.0)
        self.gainGreenDoubleSpinBox_2.setObjectName(_fromUtf8("gainGreenDoubleSpinBox_2"))
        self.gridLayout_2.addWidget(self.gainGreenDoubleSpinBox_2, 2, 1, 1, 1)
        self.gainGreenHorizontalSlider_2 = QtGui.QSlider(self.gammaGroupBox)
        self.gainGreenHorizontalSlider_2.setMinimum(-16)
        self.gainGreenHorizontalSlider_2.setMaximum(16)
        self.gainGreenHorizontalSlider_2.setProperty("value", 0)
        self.gainGreenHorizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.gainGreenHorizontalSlider_2.setObjectName(_fromUtf8("gainGreenHorizontalSlider_2"))
        self.gridLayout_2.addWidget(self.gainGreenHorizontalSlider_2, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.gammaGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.gainBlueDoubleSpinBox_2 = QtGui.QDoubleSpinBox(self.gammaGroupBox)
        self.gainBlueDoubleSpinBox_2.setDecimals(2)
        self.gainBlueDoubleSpinBox_2.setMinimum(-99.0)
        self.gainBlueDoubleSpinBox_2.setProperty("value", 0.0)
        self.gainBlueDoubleSpinBox_2.setObjectName(_fromUtf8("gainBlueDoubleSpinBox_2"))
        self.gridLayout_2.addWidget(self.gainBlueDoubleSpinBox_2, 3, 1, 1, 1)
        self.gainBlueHorizontalSlider_2 = QtGui.QSlider(self.gammaGroupBox)
        self.gainBlueHorizontalSlider_2.setMinimum(-16)
        self.gainBlueHorizontalSlider_2.setMaximum(16)
        self.gainBlueHorizontalSlider_2.setProperty("value", 0)
        self.gainBlueHorizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.gainBlueHorizontalSlider_2.setObjectName(_fromUtf8("gainBlueHorizontalSlider_2"))
        self.gridLayout_2.addWidget(self.gainBlueHorizontalSlider_2, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout.addWidget(self.gammaGroupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeView = QtGui.QTreeView(self.widget1)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_4.addWidget(self.treeView)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_4.addWidget(self.label_8)
        self.verticalLayout_5.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.gainGroupBox.setTitle(_translate("Form", "Exposure", None))
        self.label_9.setText(_translate("Form", "Master:", None))
        self.label.setText(_translate("Form", "Red:", None))
        self.label_3.setText(_translate("Form", "Green:", None))
        self.label_4.setText(_translate("Form", "Blue:", None))
        self.gammaGroupBox.setTitle(_translate("Form", "Gamma", None))
        self.label_10.setText(_translate("Form", "Master:", None))
        self.label_5.setText(_translate("Form", "Red:", None))
        self.label_6.setText(_translate("Form", "Green:", None))
        self.label_7.setText(_translate("Form", "Blue:", None))
        self.pushButton_3.setText(_translate("Form", "Load", None))
        self.pushButton.setText(_translate("Form", "Save", None))
        self.pushButton_2.setText(_translate("Form", "Reset", None))
        self.label_8.setText(_translate("Form", "TextLabel", None))
