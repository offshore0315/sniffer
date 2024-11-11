from PyQt5 import QtCore, QtGui, QtWidgets

class Window_ui(object):
    def design(sniffer_s, MainWindow):
        MainWindow.setObjectName("M_window")
        MainWindow.resize(1250, 800)
        MainWindow.setWindowTitle("Sniffer_zgl")  # 设置窗口标题

        sniffer_s.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        sniffer_s.centralwidget.setFont(font)
        sniffer_s.centralwidget.setObjectName("centralwidget")
        sniffer_s.verticalLayout = QtWidgets.QVBoxLayout(sniffer_s.centralwidget)
        sniffer_s.verticalLayout.setObjectName("verticalLayout")
        sniffer_s.splitter = QtWidgets.QSplitter(sniffer_s.centralwidget)
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        sniffer_s.splitter.setFont(font)
        sniffer_s.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)  # 修改为StyledPanel可以为Splitter添加一些样式
        sniffer_s.splitter.setFrameShadow(QtWidgets.QFrame.Raised)  # 设置阴影效果
        sniffer_s.splitter.setMidLineWidth(1)
        sniffer_s.splitter.setOrientation(QtCore.Qt.Horizontal)
        sniffer_s.splitter.setOpaqueResize(True)
        sniffer_s.splitter.setHandleWidth(15)
        sniffer_s.splitter.setChildrenCollapsible(True)
        sniffer_s.splitter.setObjectName("splitter")
        sniffer_s.table_wrapper = QtWidgets.QWidget(sniffer_s.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)  # 修改为Expanding以使组件能够更好地填充空间
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sniffer_s.table_wrapper.sizePolicy().hasHeightForWidth())
        sniffer_s.table_wrapper.setSizePolicy(sizePolicy)
        font.setFamily("Arial")
        sniffer_s.table_wrapper.setFont(font)
        sniffer_s.table_wrapper.setObjectName("table_wrapper")
        sniffer_s.gridLayout = QtWidgets.QGridLayout(sniffer_s.table_wrapper)
        sniffer_s.gridLayout.setContentsMargins(10, 10, 10, 10)  # 添加一些边距
        sniffer_s.gridLayout.setObjectName("gridLayout")
        sniffer_s.if_box = QtWidgets.QComboBox(sniffer_s.table_wrapper)
        sniffer_s.if_box.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.if_box.setMaximumSize(QtCore.QSize(250, 16777215))
        sniffer_s.if_box.setFont(font)
        sniffer_s.if_box.setObjectName("if_box")
        sniffer_s.if_box.addItem("")
        sniffer_s.gridLayout.addWidget(sniffer_s.if_box, 0, 0, 1, 1)

        # 更新源搜索按钮和地址输入框的布局
        sniffer_s.address_input = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.address_input.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.address_input.setFont(font)
        sniffer_s.address_input.setObjectName("address_input")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input, 1, 0, 1, 1)

        # 更新源地址按钮
        sniffer_s.address_button = QtWidgets.QPushButton(sniffer_s.table_wrapper)
        sniffer_s.address_button.setMaximumSize(QtCore.QSize(110, 30))  # 调整大小
        sniffer_s.address_button.setFont(font)
        sniffer_s.address_button.setObjectName("address_button")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button, 1, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sniffer_s.address_button.sizePolicy().hasHeightForWidth())
        sniffer_s.address_button.setSizePolicy(sizePolicy)

        sniffer_s.address_input1 = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.address_input1.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.address_input1.setFont(font)
        sniffer_s.address_input1.setObjectName("address_input")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input1, 1, 0, 1, 1)

        # 更新源地址按钮
        sniffer_s.address_button1 = QtWidgets.QPushButton(sniffer_s.table_wrapper)
        sniffer_s.address_button1.setMaximumSize(QtCore.QSize(110, 30))  # 调整大小
        sniffer_s.address_button1.setFont(font)
        sniffer_s.address_button1.setObjectName("address_button")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button1, 1, 1, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sniffer_s.address_button1.sizePolicy().hasHeightForWidth())
        sniffer_s.address_button1.setSizePolicy(sizePolicy)

        sniffer_s.widget_2 = QtWidgets.QWidget(sniffer_s.table_wrapper)
        sniffer_s.widget_2.setFont(font)
        sniffer_s.widget_2.setObjectName("widget_2")
        sniffer_s.horizontalLayout_3 = QtWidgets.QHBoxLayout(sniffer_s.widget_2)
        sniffer_s.horizontalLayout_3.setObjectName("horizontalLayout_3")
        sniffer_s.gridLayout.addWidget(sniffer_s.widget_2, 0, 2, 1, 1)
        sniffer_s.search_text = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.search_text.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.search_text.setFont(font)
        sniffer_s.search_text.setObjectName("search_text")
        sniffer_s.gridLayout.addWidget(sniffer_s.search_text, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sniffer_s.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        sniffer_s.search_button = QtWidgets.QPushButton(sniffer_s.table_wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sniffer_s.search_button.sizePolicy().hasHeightForWidth())
        sniffer_s.search_button.setSizePolicy(sizePolicy)
        sniffer_s.search_button.setMinimumSize(QtCore.QSize(80, 30))  # 调整大小
        font.setPointSize(10)
        sniffer_s.search_button.setFont(font)
        sniffer_s.search_button.setObjectName("search_button")
        sniffer_s.gridLayout.addWidget(sniffer_s.search_button, 2, 1, 1, 1)
        sniffer_s.table = QtWidgets.QTableWidget(sniffer_s.table_wrapper)
        font.setFamily("Arial")
        sniffer_s.table.setFont(font)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        sniffer_s.table.setFont(font)
        sniffer_s.table.setMidLineWidth(2)
        sniffer_s.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        sniffer_s.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        sniffer_s.table.setRowCount(0)
        sniffer_s.table.setObjectName("table")
        sniffer_s.table.setColumnCount(7)

        # 新增地址输入框
        sniffer_s.address_input = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.address_input.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.address_input.setFont(font)
        sniffer_s.address_input.setObjectName("address_input")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input, 1, 0, 1, 1)  # 将地址输入框添加到布局中

        # 新增搜索按钮
        sniffer_s.address_button = QtWidgets.QPushButton(sniffer_s.table_wrapper)
        sniffer_s.address_button.setMaximumSize(QtCore.QSize(110, 30))  # 调整大小
        sniffer_s.address_button.setFont(font)
        sniffer_s.address_button.setObjectName("address_button")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button, 1, 1, 1, 1)  # 将地址按钮添加到布局中

        sniffer_s.address_input1 = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.address_input1.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.address_input1.setFont(font)
        sniffer_s.address_input1.setObjectName("address_input")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input1, 1, 2, 1, 1)  # 将地址输入框添加到布局中

        # 新增搜索按钮
        sniffer_s.address_button1 = QtWidgets.QPushButton(sniffer_s.table_wrapper)
        sniffer_s.address_button1.setMaximumSize(QtCore.QSize(110, 30))  # 调整大小
        sniffer_s.address_button1.setFont(font)
        sniffer_s.address_button1.setObjectName("address_button")
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button1, 1, 3, 1, 1)  # 将地址按钮添加到布局中

        # 更新搜索框的布局
        sniffer_s.search_text = QtWidgets.QLineEdit(sniffer_s.table_wrapper)
        sniffer_s.search_text.setMinimumSize(QtCore.QSize(150, 30))  # 调整大小
        sniffer_s.search_text.setFont(font)
        sniffer_s.search_text.setObjectName("search_text")

        sniffer_s.gridLayout.addWidget(sniffer_s.search_text, 2, 0, 1, 1)
        sniffer_s.gridLayout.addWidget(sniffer_s.search_button, 2, 1, 1, 1)
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input, 1, 0, 1, 1)
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button, 1, 1, 1, 1)
        sniffer_s.gridLayout.addWidget(sniffer_s.address_input1, 1, 2, 1, 1)
        sniffer_s.gridLayout.addWidget(sniffer_s.address_button1, 1, 3, 1, 1)

        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        sniffer_s.table.setHorizontalHeaderItem(6, item)
        sniffer_s.table.horizontalHeader().setVisible(True)
        sniffer_s.table.horizontalHeader().setDefaultSectionSize(100)
        sniffer_s.table.horizontalHeader().setMinimumSectionSize(50)
        sniffer_s.table.horizontalHeader().setSortIndicatorShown(False)
        sniffer_s.table.horizontalHeader().setStretchLastSection(True)  # 修改为True以使最后一列填充剩余空间
        sniffer_s.table.verticalHeader().setVisible(False)
        sniffer_s.gridLayout.addWidget(sniffer_s.table, 3, 0, 1, 3)
        sniffer_s.tab_wrapper = QtWidgets.QWidget(sniffer_s.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sniffer_s.tab_wrapper.sizePolicy().hasHeightForWidth())
        sniffer_s.tab_wrapper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        sniffer_s.tab_wrapper.setFont(font)
        sniffer_s.tab_wrapper.setObjectName("tab_wrapper")
        sniffer_s.gridLayout_2 = QtWidgets.QGridLayout(sniffer_s.tab_wrapper)
        sniffer_s.gridLayout_2.setContentsMargins(5, 5, 5, 5)  # 添加一些边距以改善布局
        sniffer_s.gridLayout_2.setObjectName("gridLayout_2")
        sniffer_s.tab = QtWidgets.QTabWidget(sniffer_s.tab_wrapper)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        sniffer_s.tab.setFont(font)
        sniffer_s.tab.setStyleSheet("QTabWidget::pane\n"
                               "\n"
                               "{\n"
                               "\n"
                               "border-width: 2px;\n"  # 将边框宽度修改为2px
                                    "\n"
                               "border-color:#2d2d2d;\n"  # 修改边框颜色为深灰色
                                    "\n"
                               "border-style:outset;\n"
                               "\n"
                               "border-radius: 3px;\n"
                               "\n"
                               "background-color: rgb(230, 230, 230);\n"  # 修改背景颜色为浅灰色
                                    "\n"
                               "}\n"
                               "")
        sniffer_s.tab.setIconSize(QtCore.QSize(20, 20))
        sniffer_s.tab.setElideMode(QtCore.Qt.ElideNone)
        sniffer_s.tab.setDocumentMode(False)
        sniffer_s.tab.setTabsClosable(False)
        sniffer_s.tab.setMovable(False)
        sniffer_s.tab.setTabBarAutoHide(False)
        sniffer_s.tab.setObjectName("tab")
        sniffer_s.detail = QtWidgets.QWidget()
        sniffer_s.detail.setMinimumSize(QtCore.QSize(0, 0))
        sniffer_s.detail.setObjectName("detail")
        sniffer_s.gridLayout_3 = QtWidgets.QGridLayout(sniffer_s.detail)
        sniffer_s.gridLayout_3.setContentsMargins(10, 10, 10, 10)  # 添加一些边距以改善布局
        sniffer_s.gridLayout_3.setObjectName("gridLayout_3")
        sniffer_s.detail_tree = QtWidgets.QTreeWidget(sniffer_s.detail)
        sniffer_s.detail_tree.setAutoExpandDelay(-1)
        sniffer_s.detail_tree.setObjectName("detail_tree")
        sniffer_s.detail_tree.header().setDefaultSectionSize(200)
        sniffer_s.detail_tree.header().setMinimumSectionSize(200)
        sniffer_s.gridLayout_3.addWidget(sniffer_s.detail_tree, 0, 0, 1, 1)
        sniffer_s.tab.addTab(sniffer_s.detail, "")
        sniffer_s.hex_info = QtWidgets.QWidget()
        sniffer_s.hex_info.setObjectName("hex_info")
        sniffer_s.verticalLayout_2 = QtWidgets.QVBoxLayout(sniffer_s.hex_info)
        sniffer_s.verticalLayout_2.setObjectName("verticalLayout_2")
        sniffer_s.hex_text = QtWidgets.QTextBrowser(sniffer_s.hex_info)
        font = QtGui.QFont()
        font.setFamily("Courier New")  # 修改字体为Courier New
        font.setPointSize(10)
        sniffer_s.hex_text.setFont(font)
        sniffer_s.hex_text.setStyleSheet(
            "background-color: #f0f0f0;"  # 设置背景色为浅灰色
            "color: #333;"  # 设置文字颜色为深灰色
            "border: 1px solid #ccc;"  # 设置边框
            "padding: 5px;"  # 设置内边距
        )
        sniffer_s.hex_text.setObjectName("hex_text")
        sniffer_s.verticalLayout_2.addWidget(sniffer_s.hex_text)
        sniffer_s.tab.addTab(sniffer_s.hex_info, "")
        sniffer_s.gridLayout_2.addWidget(sniffer_s.tab, 0, 0, 1, 1)
        sniffer_s.verticalLayout.addWidget(sniffer_s.splitter)
        MainWindow.setCentralWidget(sniffer_s.centralwidget)
        font.setFamily("Arial")
        sniffer_s.hex_text.setFont(font)
        sniffer_s.hex_text.setObjectName("hex_text")
        sniffer_s.verticalLayout_2.addWidget(sniffer_s.hex_text)
        sniffer_s.tab.addTab(sniffer_s.hex_info, "")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font = QtGui.QFont()
        font.setFamily("Arial")
        item_font = QtGui.QFont()
        item_font.setFamily("Arial")
        item_font.setPointSize(10)  # 设置字体大小为10
        for column in range(6):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(item_font)

        font = QtGui.QFont()
        font.setPointSize(12)
        sniffer_s.gridLayout_2.addWidget(sniffer_s.tab, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sniffer_s.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        sniffer_s.verticalLayout.addWidget(sniffer_s.splitter)
        MainWindow.setCentralWidget(sniffer_s.centralwidget)
        sniffer_s.menubar = QtWidgets.QMenuBar(MainWindow)
        sniffer_s.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        sniffer_s.menubar.setFont(font)
        sniffer_s.menubar.setObjectName("menubar")
        sniffer_s.menu = QtWidgets.QMenu(sniffer_s.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        sniffer_s.menu.setFont(font)
        sniffer_s.menu.setObjectName("menu")
        sniffer_s.menu_C = QtWidgets.QMenu(sniffer_s.menubar)
        sniffer_s.menu_C.setObjectName("menu_C")
        MainWindow.setMenuBar(sniffer_s.menubar)
        sniffer_s.action_start = QtWidgets.QAction(MainWindow)
        sniffer_s.action_start.setCheckable(False)
        sniffer_s.action_start.setObjectName("action_start")
        sniffer_s.action_about_sniffer = QtWidgets.QAction(MainWindow)
        sniffer_s.action_about_sniffer.setObjectName("action_about_sniffer")
        sniffer_s.action_stop = QtWidgets.QAction(MainWindow)
        sniffer_s.action_stop.setObjectName("action_stop")
        sniffer_s.action_restart = QtWidgets.QAction(MainWindow)
        sniffer_s.action_restart.setObjectName("action_restart")
        sniffer_s.action_clean_all = QtWidgets.QAction(MainWindow)
        sniffer_s.action_clean_all.setObjectName("action_clean_all")
        sniffer_s.action_open_file = QtWidgets.QAction(MainWindow)
        sniffer_s.action_open_file.setEnabled(True)
        sniffer_s.action_open_file.setObjectName("action_open_file")
        sniffer_s.action_save_as = QtWidgets.QAction(MainWindow)
        sniffer_s.action_save_as.setObjectName("action_save_as")
        sniffer_s.action_show_details = QtWidgets.QAction(MainWindow)
        sniffer_s.action_show_details.setObjectName("action_show_details")
        sniffer_s.action_reassemble = QtWidgets.QAction(MainWindow)
        sniffer_s.action_reassemble.setObjectName("action_reassemble")
        sniffer_s.action_tcp_to_file = QtWidgets.QAction(MainWindow)
        sniffer_s.action_tcp_to_file.setObjectName("action_tcp_to_file")
        sniffer_s.action_exit = QtWidgets.QAction(MainWindow)
        sniffer_s.action_exit.setPriority(QtWidgets.QAction.NormalPriority)
        sniffer_s.action_exit.setObjectName("action_exit")
        sniffer_s.menu.addAction(sniffer_s.action_open_file)
        sniffer_s.menu.addAction(sniffer_s.action_save_as)
        sniffer_s.menu.addSeparator()
        sniffer_s.menu.addAction(sniffer_s.action_exit)
        sniffer_s.menu_C.addAction(sniffer_s.action_start)
        sniffer_s.menu_C.addAction(sniffer_s.action_stop)
        sniffer_s.menu_C.addAction(sniffer_s.action_restart)
        sniffer_s.menu_C.addAction(sniffer_s.action_clean_all)
        sniffer_s.menubar.addAction(sniffer_s.menu.menuAction())
        sniffer_s.menubar.addAction(sniffer_s.menu_C.menuAction())
        sniffer_s.name(MainWindow)
        sniffer_s.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        sniffer_s.table.setColumnWidth(5, 100)
        sniffer_s.table.resizeColumnToContents(5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        sniffer_s.table.setFont(font)
        horizontalHeader = sniffer_s.table.horizontalHeader()
        horizontalHeader.setFont(font)


    def name(sniffer_s, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        sniffer_s.if_box.setCurrentText(_translate("M_window", "选择网卡"))
        sniffer_s.if_box.setItemText(0, _translate("M_window", "选择网卡"))

        sniffer_s.address_input.setPlaceholderText(_translate("M_window", "源地址信息"))  # 设置提示文字
        sniffer_s.address_button.setText(_translate("M_window", "搜索"))  # 设置按钮文本

        sniffer_s.address_input1.setPlaceholderText(_translate("M_window", "目的地址信息"))  # 设置提示文字
        sniffer_s.address_button1.setText(_translate("M_window", "搜索"))  # 设置按钮文本

        sniffer_s.search_text.setPlaceholderText(_translate("M_window", "协议类型"))
        sniffer_s.search_button.setText(_translate("M_window", "搜索"))

        item = sniffer_s.table.horizontalHeaderItem(0)
        item.setText(_translate("M_window", "No."))
        item = sniffer_s.table.horizontalHeaderItem(1)
        item.setText(_translate("M_window", "Time"))
        item = sniffer_s.table.horizontalHeaderItem(2)
        item.setText(_translate("M_window", "Source"))
        item = sniffer_s.table.horizontalHeaderItem(3)
        item.setText(_translate("M_window", "Destination"))
        item = sniffer_s.table.horizontalHeaderItem(4)
        item.setText(_translate("M_window", "Protocol"))
        item = sniffer_s.table.horizontalHeaderItem(5)
        item.setText(_translate("M_window", "Length"))
        item = sniffer_s.table.horizontalHeaderItem(6)
        item.setText(_translate("M_window", "Information"))
        sniffer_s.detail_tree.headerItem().setText(0, _translate("M_window", "字段"))
        sniffer_s.detail_tree.headerItem().setText(1, _translate("M_window", "值"))
        sniffer_s.tab.setTabText(sniffer_s.tab.indexOf(sniffer_s.detail), _translate("M_window", "详细信息"))
        sniffer_s.hex_text.setHtml(_translate("M_window",
                                         """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                                         <html>
                                             <head>
                                                 <meta name="qrichtext" content="1" />
                                                 <style type="text/css">
                                                     p, li { white-space: pre-wrap; font-family:'Courier New'; font-size:12pt; }
                                                 </style>
                                             </head>
                                             <body>
                                                 <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                                                     <br />
                                                 </p>
                                             </body>
                                         </html>"""))

        sniffer_s.tab.setTabText(sniffer_s.tab.indexOf(sniffer_s.hex_info), _translate("M_window", "HEX"))
        sniffer_s.menu.setTitle(_translate("M_window", "文件"))
        sniffer_s.menu_C.setTitle(_translate("M_window", "捕获"))
        sniffer_s.action_start.setText(_translate("M_window", "开始捕获"))
        sniffer_s.action_start.setShortcut(_translate("M_window", "Ctrl+E"))
        sniffer_s.action_about_sniffer.setText(_translate("M_window", "关于sniffer"))
        sniffer_s.action_stop.setText(_translate("M_window", "停止捕获"))
        sniffer_s.action_stop.setShortcut(_translate("M_window", "Ctrl+F"))
        sniffer_s.action_restart.setText(_translate("M_window", "重新开始"))
        sniffer_s.action_restart.setShortcut(_translate("M_window", "Ctrl+R"))
        sniffer_s.action_clean_all.setText(_translate("M_window", "清除全部"))
        sniffer_s.action_clean_all.setToolTip(_translate("M_window", "清除全部"))
        sniffer_s.action_clean_all.setShortcut(_translate("M_window", "Ctrl+C"))
        sniffer_s.action_open_file.setText(_translate("M_window", "打开文件"))
        sniffer_s.action_open_file.setShortcut(_translate("M_window", "Ctrl+O"))
        sniffer_s.action_save_as.setText(_translate("M_window", "保存"))
        # sniffer_s.action_save_as.setToolTip(_translate("M_window", "另存为..."))
        sniffer_s.action_save_as.setShortcut(_translate("M_window", "Ctrl+S"))
        sniffer_s.action_exit.setText(_translate("M_window", "退出"))
        sniffer_s.action_exit.setShortcut(_translate("M_window", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window_ui()
    ui.design(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

