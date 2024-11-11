from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
from data import Packet


class Signal_s(QObject):
    update_table = pyqtSignal(Packet)
    update_reassemble_table = pyqtSignal(Packet)