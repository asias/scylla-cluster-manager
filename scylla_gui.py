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

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cluster_table = QTableWidget(self.tab)
        self.cluster_table.setObjectName(u"cluster_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cluster_table.sizePolicy().hasHeightForWidth())
        self.cluster_table.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.cluster_table)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.scylla_list = QComboBox(self.tab)
        self.scylla_list.setObjectName(u"scylla_list")
        sizePolicy.setHeightForWidth(self.scylla_list.sizePolicy().hasHeightForWidth())
        self.scylla_list.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.scylla_list)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.node_table = QTableWidget(self.tab)
        self.node_table.setObjectName(u"node_table")
        sizePolicy.setHeightForWidth(self.node_table.sizePolicy().hasHeightForWidth())
        self.node_table.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.node_table)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.log_table = QTextEdit(self.tab)
        self.log_table.setObjectName(u"log_table")
        self.log_table.setReadOnly(True)

        self.verticalLayout.addWidget(self.log_table)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.addnode_button = QPushButton(self.tab)
        self.addnode_button.setObjectName(u"addnode_button")
        self.addnode_button.setMaximumSize(QSize(100, 35))

        self.gridLayout.addWidget(self.addnode_button, 0, 0, 1, 1)

        self.delnode_button = QPushButton(self.tab)
        self.delnode_button.setObjectName(u"delnode_button")
        self.delnode_button.setMaximumSize(QSize(100, 35))
        self.delnode_button.setFlat(False)

        self.gridLayout.addWidget(self.delnode_button, 0, 1, 1, 1)

        self.depoly_button = QPushButton(self.tab)
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


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.manage_select_node = QComboBox(self.tab_2)
        self.manage_select_node.setObjectName(u"manage_select_node")

        self.verticalLayout_3.addWidget(self.manage_select_node)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 6, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_6.addWidget(self.pushButton_6, 4, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_6.addWidget(self.pushButton_5, 10, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_6.addWidget(self.pushButton_4, 5, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_6.addWidget(self.pushButton_10, 14, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_6.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 7, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_6.addWidget(self.pushButton_9, 12, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_6.addWidget(self.pushButton_7, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cluster Config:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scylla Version:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nodes Config:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs:", None))
        self.addnode_button.setText(QCoreApplication.translate("MainWindow", u"Add Node", None))
        self.delnode_button.setText(QCoreApplication.translate("MainWindow", u"Del Node", None))
        self.depoly_button.setText(QCoreApplication.translate("MainWindow", u"Deploy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Deploy", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select node:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Logs:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Repair", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Snapshot", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Rebuild", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Drain", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Decommission", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Cleardata", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Manage", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Status", None))
    # retranslateUi

