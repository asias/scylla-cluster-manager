# To start the tool
$ python3 scylla.py

# Install runtime dependency
$ sudo dnf install -y python3-pyside2

# Install development dependencies
$ sudo dnf install -y qt5-qtbase-devel python3-pyside2-devel qt5-qttools-devel

# Make gui change with qt designer
$ designer-qt5 scylla.ui

# Convert the .ui created by qt-designer to .py
$ uic-qt5 scylla.ui -o scylla_gui.py -g python

# NOTES
- Development is only tested on Fedora 33.
- It is tested to run on Fedora 31 and 33.
- By default, this tool starts 3 nodes locally.
- Kill the cluster before clicking the deploy again.
  For example:
  ```
  $ killall -9 scylla
  $ rm -rf /tmp/data/scylla
  ```
- Replace the offline installer scylla-package.tar.gz to deploy a different scylla version.
