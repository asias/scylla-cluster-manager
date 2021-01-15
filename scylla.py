#!/usr/bin/env python3

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import os
import time
from concurrent.futures import ThreadPoolExecutor
import scylla_gui
import gen_cluster
import scylla_tools
import subprocess
import signal
from utils import *

_VERSION_ = '2021.01'


class MySig(QObject):
    log = Signal(str)


class MyMainWindow(QMainWindow, scylla_gui.Ui_MainWindow):
    def __init__(self, app, parent=None):
        """
        Init function for MyMainWindow class
        """
        super(MyMainWindow, self).__init__(parent)
        self.app = app
        self.nodes = [
            ["192.168.66.222", "192.168.66.222", "DC1", "RACK1", "/tmp/data/scylla", "192.168.66.222", "256", "auto", "auto"],
            ["192.168.66.200", "192.168.66.200", "DC1", "RACK1", "/tmp/data/scylla", "192.168.66.222", "256", "auto", "auto"]]
        self.nodes = [
            ["3.36.115.144", "172.31.6.66", "DC1", "RACK1", "/tmp/data/scylla", "3.36.115.144", "256", "auto", "auto"],
            ["3.36.60.95", "172.31.10.145", "DC1", "RACK1", "/tmp/data/scylla", "3.36.115.144", "256", "auto", "auto"]]
        self.nodes = [
            ["127.0.0.1", "127.0.0.1", "DC1", "RACK1", "/tmp/data/scylla/1", "127.0.0.1", "256", "1", "512"],
            ["127.0.0.2", "127.0.0.2", "DC1", "RACK1", "/tmp/data/scylla/2", "127.0.0.1", "256", "1", "512"],
            ["127.0.0.3", "127.0.0.3", "DC1", "RACK1", "/tmp/data/scylla/3", "127.0.0.1", "256", "1", "512"]]
        self.node_default = self.nodes[0]
        self.setupUi(self)
        title = "Scylla Cluster Manager" + " - " + _VERSION_
        self.setWindowTitle(title)
        self.show_cluster_table()
        self.show_node_table()
        self.depoly_button.clicked.connect(self.deploy_button_callback)
        self.addnode_button.clicked.connect(self.addnode_button_callback)
        self.delnode_button.clicked.connect(self.delnode_button_callback)
        self.executor = ThreadPoolExecutor(max_workers=2)
        self.depoly_threads = []
        self.sig = MySig()
        self.sig.log.connect(self.log_table.append)
        self.display_logo()

    def display_logo(self):
        pixmap = QPixmap('./scylla.png')
        self.logo.setPixmap(pixmap)
        self.logo.show()

    def get_cluster_info(self):
        row = self.cluster_table.rowCount()
        col = self.cluster_table.columnCount()
        self.cluster = [[0 for x in range(col)] for x in range(row)]
        for row in range(self.cluster_table.rowCount()):
            for col in range(self.cluster_table.columnCount()):
                self.cluster[row][col] = self.cluster_table.item(row, col).text()
        return self.cluster[0]

    def get_nodes_info(self):
        for row in range(self.node_table.rowCount()):
            for col in range(self.node_table.columnCount()):
                self.nodes[row][col] = self.node_table.item(row, col).text()
        return self.nodes

    def addnode_button_callback(self):
        self.nodes.append(self.node_default)
        self.show_node_table()

    def delnode_button_callback(self):
        if self.nodes:
            self.nodes.pop(-1)
        self.show_node_table()

    def gen_button_callback(self):
        pass

    def log(self, cmd):
        print(cmd)
        self.sig.log.emit(cmd)

    def run_cmd(self, cmd):
        self.log(cmd)
        os.system(cmd)

    def get_ssh(self, user, ip, key, cmd):
        return f"ssh -i {key} -o StrictHostKeyChecking=no {user}@{ip} {cmd}"

    def get_scp(self, user, ip, key, src, dst):
        return f"scp -i {key} -r -q -o StrictHostKeyChecking=no {src} {user}@{ip}:{dst}"


    def show_cluster_status(self, ip):
        status = scylla_tools.nodetool_status(ip)
        for node in status:
            self.log(f"{node}")

    def deploy_button_callback(self):
        if len(self.depoly_threads) != 0:
            self.log("One running")

        self.log_table.clear()
        t = self.executor.submit(self.do_deploy_button_callback)
        self.depoly_threads.append(t)

    def do_deploy_button_callback(self):

        start_time = time.time()
        if not self.nodes:
            return
        cluster = self.get_cluster_info()
        cluster_name = cluster[0]
        ssh_user = cluster[1]
        ssh_key = cluster[2]

        self.log("=== Step 1: Generate config file ===")
        msgs = gen_cluster.gen_cmds(cluster_name, ssh_user, self.get_nodes_info())
        for msg in msgs:
            self.log(msg)

        self.log("=== Step 2: Copy scylla-package.tar.gz ===")
        for info in self.nodes:
            ip = info[0]
            directory = info[4]
            tarball = "scylla-package.tar.gz"

            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"mkdir -p {directory}")
            self.run_cmd(cmd)

            cmd = self.get_scp(ssh_user, ip, ssh_key, tarball, directory)
            self.run_cmd(cmd)

            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"tar xf {directory}/{tarball} -C {directory}")
            self.run_cmd(cmd)

            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"{directory}/scylla/install.sh --nonroot")
            self.run_cmd(cmd)

            cmd = self.get_scp(ssh_user, ip, ssh_key, f"{CMD_FILE_PREFIX}.{ip}", directory)
            self.run_cmd(cmd)

            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"chmod +x {directory}/{CMD_FILE_PREFIX}.{ip}")
            self.run_cmd(cmd)

        self.log("=== Step 3: Depoly the first node in the cluster ===")
        for info in self.nodes[0:1]:
            ip = info[0]
            directory = info[4]
            node_name = f"{CMD_FILE_PREFIX}.{ip}"
            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"{directory}/{node_name}")
            self.run_cmd(cmd)

        self.log("=== Step 4: Depoly the remaining nodes in the cluster ===")
        threads = []
        for info in self.nodes[1:]:
            ip = info[0]
            directory = info[4]
            node_name = f"{CMD_FILE_PREFIX}.{ip}"
            cmd = self.get_ssh(ssh_user, ip, ssh_key, f"{directory}/{node_name}")
            self.log(cmd)
            p = subprocess.Popen(cmd, shell=True)
            threads.append(p)
        for p in threads:
            p.wait()

        elapsed_time = time.time() - start_time
        msg = f"=== Step 5: Depoly {len(self.nodes)} nodes successfully in {elapsed_time} seconds! ==="
        self.log(msg)

        node = self.nodes[0][0]
        self.show_cluster_status(node)


    def get_cluster_header(self):
        """
        Get the apps header to display on the ui
        """
        headers = [u'Cluster Name', u'SSH User', u'SSH Keys']
        return headers

    def show_cluster_table(self):
        """
        Display all the devices
        """
        headers = self.get_cluster_header()
        _DEFAULT_HEADER_SIZE_ = 25
        devices = [1]
        self.cluster_table.clear()
        self.cluster_table.setSortingEnabled(False)
        self.cluster_table.setRowCount(len(devices))
        self.cluster_table.setColumnCount(len(headers))
        self.cluster_table.setHorizontalHeaderLabels(headers)
        self.cluster_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.cluster_table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.cluster_table.verticalHeader().setDefaultSectionSize(_DEFAULT_HEADER_SIZE_)

        apps = [["MyScyllaCluster", os.getenv('USER', 'asias'), "~/.ssh/id_rsa"]]
        row = 0
        for app in apps:
            col = 0
            for it in app:
                item = QTableWidgetItem(it)
                self.cluster_table.setItem(row, col, item)
                col += 1
            row += 1
        self.cluster_table.resizeColumnsToContents()

    def get_node_header(self):
        """
        Get the apps header to display on the ui
        """
        headers = [u'Public IP', u'Private IP', u'DC', u'RACK',  u'Data Directory', u'Contact Point(Seed)', u'Num Tokens', u'CPU Cores', u'Memory MB']
        return headers

    def show_node_table(self):
        """
        Display all the devices
        """
        headers = self.get_node_header()
        _DEFAULT_HEADER_SIZE_ = 25
        self.node_table.clear()
        self.node_table.setSortingEnabled(False)
        self.node_table.setRowCount(len(self.nodes))
        self.node_table.setColumnCount(len(headers))
        self.node_table.setHorizontalHeaderLabels(headers)
        self.node_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.node_table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.node_table.verticalHeader().setDefaultSectionSize(_DEFAULT_HEADER_SIZE_)
        row = 0
        for node in self.nodes:
            col = 0
            for it in node:
                item = QTableWidgetItem(it)
                self.node_table.setItem(row, col, item)
                col += 1
            row += 1
        #self.node_table.resizeColumnsToContents()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    w = MyMainWindow(app)
    w.show()
    app.exec_()
