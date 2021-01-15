# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scylla.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cluster_table = QTableWidget(self.centralwidget)
        self.cluster_table.setObjectName(u"cluster_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cluster_table.sizePolicy().hasHeightForWidth())
        self.cluster_table.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.cluster_table)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.node_table = QTableWidget(self.centralwidget)
        self.node_table.setObjectName(u"node_table")
        sizePolicy.setHeightForWidth(self.node_table.sizePolicy().hasHeightForWidth())
        self.node_table.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.node_table)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.log_table = QTextEdit(self.centralwidget, readOnly=True)
        self.log_table.setObjectName(u"log_table")

        self.verticalLayout.addWidget(self.log_table)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.addnode_button = QPushButton(self.centralwidget)
        self.addnode_button.setObjectName(u"addnode_button")
        self.addnode_button.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.addnode_button, 0, 0, 1, 1)

        self.delnode_button = QPushButton(self.centralwidget)
        self.delnode_button.setObjectName(u"delnode_button")
        self.delnode_button.setMaximumSize(QSize(100, 35))
        self.delnode_button.setFlat(False)

        self.gridLayout.addWidget(self.delnode_button, 0, 1, 1, 1)

        self.depoly_button = QPushButton(self.centralwidget)
        self.depoly_button.setObjectName(u"depoly_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.depoly_button.sizePolicy().hasHeightForWidth())
        self.depoly_button.setSizePolicy(sizePolicy1)
        self.depoly_button.setMaximumSize(QSize(120, 50))
        font = QFont()
        font.setPointSize(13)
        self.depoly_button.setFont(font)
        self.depoly_button.setAutoFillBackground(False)
        self.depoly_button.setStyleSheet(u"background-color: rgb(46, 194, 126);")

        self.gridLayout.addWidget(self.depoly_button, 5, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cluster Config:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nodes Config:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs:", None))
        self.addnode_button.setText(QCoreApplication.translate("MainWindow", u"Add Node", None))
        self.delnode_button.setText(QCoreApplication.translate("MainWindow", u"Del Node", None))
        self.depoly_button.setText(QCoreApplication.translate("MainWindow", u"Deploy", None))
    # retranslateUi

