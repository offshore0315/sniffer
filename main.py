from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from scapy.all import get_working_ifaces
from data import Packet
from find import PacketFind
import catch
import json
from main_window import Window_ui
import sys


class M_window(QMainWindow):
    def __init__(sniffer_s):
        super().__init__()
        sniffer_s.ui = Window_ui()
        sniffer_s.ui.design(sniffer_s)
        sniffer_s.s = catch.PacketSniff(sniffer_s.ui)
        sniffer_s.show_table()
        sniffer_s.get_nif(sniffer_s.ui.if_box)
        sniffer_s.initialize()
        sniffer_s.design_toolbar()
        sniffer_s.choose_if_box()
        sniffer_s.design_signal()
        sniffer_s.searcher()

    def initialize(sniffer_s):
        sniffer_s.ui.action_start.setEnabled(False)
        sniffer_s.ui.action_stop.setEnabled(False)
        sniffer_s.ui.action_restart.setEnabled(False)
        sniffer_s.ui.action_clean_all.setEnabled(False)
        sniffer_s.ui.action_save_as.setEnabled(False)

    def get_nif(sniffer_s, if_box: QComboBox):
        if_list = [nif.name for nif in get_working_ifaces() if nif.mac]
        if_box.addItems(if_list)
        return if_list



    # 设置信息展示表格
    def show_table(sniffer_s):
        sniffer_s.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        sniffer_s.ui.table.setColumnWidth(0, 50)
        sniffer_s.ui.table.setColumnWidth(2, 150)
        sniffer_s.ui.table.setColumnWidth(3, 150)
        sniffer_s.ui.table.setColumnWidth(4, 100)
        sniffer_s.ui.table.setColumnWidth(5, 50)
        sniffer_s.ui.table.horizontalHeader().setStretchLastSection(True)
        sniffer_s.ui.table.setStyleSheet('QTableWidget::item:selected{background-color: #ACACAC}')
        sniffer_s.ui.table.itemClicked.connect(sniffer_s.show_detail)
        sniffer_s.ui.table.itemClicked.connect(sniffer_s.hex)

    # 设置工具栏操作
    def design_toolbar(sniffer_s):
        sniffer_s.ui.action_exit.triggered.connect(exit)
        sniffer_s.ui.action_start.triggered.connect(sniffer_s.start)
        sniffer_s.ui.action_stop.triggered.connect(sniffer_s.stop)
        sniffer_s.ui.action_clean_all.triggered.connect(sniffer_s.clean)
        sniffer_s.ui.action_restart.triggered.connect(sniffer_s.restart)
        sniffer_s.ui.action_save_as.triggered.connect(sniffer_s.save)
        sniffer_s.ui.action_open_file.triggered.connect(sniffer_s.read)
        sniffer_s.ui.action_show_details.triggered.connect(lambda: sniffer_s.ui.tab.setCurrentIndex(0))

    def searcher(sniffer_s):
        search_button = sniffer_s.ui.search_button
        search_button.clicked.connect(sniffer_s.look_up_combined)
        search_button.setShortcut('Return')

        address_button = sniffer_s.ui.address_button
        address_button.clicked.connect(sniffer_s.look_up_combined)
        address_button.setShortcut('Return')

        address_button1 = sniffer_s.ui.address_button1
        address_button1.clicked.connect(sniffer_s.look_up_combined)
        address_button1.setShortcut('Return')

    def choose_if_box(sniffer_s):
        sniffer_s.ui.if_box.currentIndexChanged.connect(sniffer_s.checknet)

    def look_up_combined(sniffer_s):
        try:
            # 获取搜索框的文本
            search_text: QLineEdit = sniffer_s.ui.search_text
            protocol_text = search_text.text().strip()

            # 获取源地址输入框的文本
            address_input: QLineEdit = sniffer_s.ui.address_input
            src_address_text = address_input.text().strip()

            # 获取目的地址输入框的文本
            address_input1: QLineEdit = sniffer_s.ui.address_input1
            dst_address_text = address_input1.text().strip()

            # 清空表格
            sniffer_s.clear_table()

            # 如果三个输入框都为空，显示所有数据包
            if protocol_text == '' and src_address_text == '' and dst_address_text == '':
                for p in sniffer_s.s.packet_list:
                    sniffer_s.contiue(p)
            else:
                # 按顺序应用筛选条件

                # 先根据协议进行筛选（如果有输入）
                filtered_packets = sniffer_s.s.packet_list
                if protocol_text != '':
                    searcher = PacketFind(filtered_packets, protocol_text)
                    filtered_packets = searcher.find_packet()

                # 再根据源地址进行筛选（如果有输入）
                if src_address_text != '':
                    filtered_packets = [
                        p for p in filtered_packets if src_address_text.lower() in p.src.lower()
                    ]

                # 最后根据目的地址进行筛选（如果有输入）
                if dst_address_text != '':
                    filtered_packets = [
                        p for p in filtered_packets if dst_address_text.lower() in p.dst.lower()
                    ]

                # 显示筛选后的结果
                for p in filtered_packets:
                    sniffer_s.contiue(p)

        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            traceback.print_exc()

    # def look_up_with_saddress(sniffer_s):
    #     try:
    #         # 获取地址输入框的文本
    #         address_input: QLineEdit = sniffer_s.ui.address_input
    #         address_text = address_input.text().strip()  # 去除前后空格
    #         sniffer_s.clear_table()  # 清空表格
    #
    #         if address_text == '':
    #             # 如果地址输入框为空，显示所有数据包
    #             for p in sniffer_s.s.packet_list:
    #                 sniffer_s.contiue(p)
    #         else:
    #
    #             # 根据地址文本进行筛选
    #             filtered_packets = [
    #                 p for p in sniffer_s.s.packet_list if address_text.lower() in p.src.lower()
    #             ]
    #
    #             # 显示筛选后的结果
    #             for p in filtered_packets:
    #                 sniffer_s.contiue(p)
    #
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         import traceback
    #         traceback.print_exc()
    #
    # def look_up_with_maddress(sniffer_s):
    #     try:
    #         # 获取地址输入框的文本
    #         address_input: QLineEdit = sniffer_s.ui.address_input1
    #         address_text = address_input.text().strip()  # 去除前后空格
    #         sniffer_s.clear_table()  # 清空表格
    #
    #         if address_text == '':
    #             # 如果地址输入框为空，显示所有数据包
    #             for p in sniffer_s.s.packet_list:
    #                 sniffer_s.contiue(p)
    #         else:
    #
    #             # 根据地址文本进行筛选
    #             filtered_packets = [
    #                 p for p in sniffer_s.s.packet_list if address_text.lower() in p.dst.lower()
    #             ]
    #
    #             # 显示筛选后的结果
    #             for p in filtered_packets:
    #                 sniffer_s.contiue(p)
    #
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         import traceback
    #         traceback.print_exc()

    # 设置信号
    def design_signal(sniffer_s):
        sniffer_s.s.signal_triggers.update_table.connect(sniffer_s.contiue)

    # 检测网卡
    def checknet(sniffer_s, index):
        if index != 0 and not sniffer_s.s.capture_active:
            sniffer_s.ui.action_start.setEnabled(True)
            sniffer_s.ui.action_restart.setEnabled(True)
        else:
            sniffer_s.ui.action_start.setEnabled(False)
            sniffer_s.ui.action_restart.setEnabled(False)


    # 退出界面
    def exit(sniffer_s):
        reply = QMessageBox.question(sniffer_s, '温馨提示',
                                     "确定退出吗?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sniffer_s.ui.close()



    # 添加行
    def contiue(sniffer_s, packet_info: Packet):
        table: QTableWidget = sniffer_s.ui.table
        rows = table.rowCount()
        table.insertRow(rows)
        headers = ['number', 'time', 'src', 'dst', 'protocol', 'length', 'info']

        # 根据协议类型设置颜色
        color_dict = {
            'UDP': QColor('#E0F7FA'),
            'TCP': QColor('#E8F5E9'),
            'DNS': QColor('#FFF9C4'),
            'ICMPv6': QColor('#F3E5F5'),
            'ARP': QColor('#FFECB3')
        }
        color = color_dict.get(packet_info.protocol, QColor('#FFFFFF'))  # 默认为白色

        for i, header in enumerate(headers):
            item = QTableWidgetItem(str(packet_info.__dict__[header]))
            item.setBackground(color)
            table.setItem(rows, i, item)

        table.scrollToBottom()

    # 清除信息
    def clear(sniffer_s):
        sniffer_s.clear_table()
        sniffer_s.s.reset_data()

    # 清除数据包显示表
    def clear_table(sniffer_s):
        sniffer_s.ui.table.clearContents()
        sniffer_s.ui.table.setRowCount(0)
        sniffer_s.ui.detail_tree.clear()
        sniffer_s.ui.hex_text.clear()

    # 开始嗅探
    def start(sniffer_s):
        try:
            sniffer_s.s.activate()
            sniffer_s.ui.action_stop.setEnabled(True)
            sniffer_s.ui.action_start.setEnabled(False)
            sniffer_s.ui.action_restart.setEnabled(False)
            sniffer_s.ui.action_clean_all.setEnabled(False)
            sniffer_s.ui.action_save_as.setEnabled(False)
            sniffer_s.ui.action_exit.setEnabled(False)
            sniffer_s.ui.action_open_file.setEnabled(False)
        except Exception as e:
            # 打印异常信息到控制台
            print(f"An error occurred: {e}")

    # 重新开始
    def restart(sniffer_s):
        sniffer_s.clear()
        sniffer_s.start()

    # 停止嗅探
    def stop(sniffer_s):
        sniffer_s.s.deactivate()
        sniffer_s.ui.action_stop.setEnabled(False)
        sniffer_s.ui.action_restart.setEnabled(True)
        sniffer_s.ui.action_start.setEnabled(True)
        sniffer_s.ui.action_clean_all.setEnabled(True)
        sniffer_s.ui.action_save_as.setEnabled(True)
        sniffer_s.ui.action_open_file.setEnabled(True)
        sniffer_s.ui.action_exit.setEnabled(True)

    # 清除内容
    def clean(sniffer_s):
        reply = QMessageBox.question(sniffer_s, '温馨提示',
                                     "该操作将会清除所有内容！",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sniffer_s.clear()
            sniffer_s.ui.action_save_as.setEnabled(False)

    # 展示详细信息

    class CustomTreeWidgetItem(QTreeWidgetItem):
        def __init__(sniffer_s, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def show_detail(sniffer_s, item: QTableWidgetItem):
        tree: QTreeWidget = sniffer_s.ui.detail_tree
        tab: QTabWidget = sniffer_s.ui.tab

        # 设置树的样式表
        tree.setStyleSheet("""
            QTreeWidget {
                border: 1px solid #ccc;
                background-color: #f9f9f9;
            }
            QTreeWidget::item {
                border-bottom: 1px solid #ccc;
            }
        """)

        # 清除旧的项
        tree.clear()

        # 获取行号和相关信息
        row = item.row()
        number = int(sniffer_s.ui.table.item(row, 0).text()) - 1
        info = sniffer_s.s.packet_list[number].detail_info

        # 设置字体和图标
        font = QFont()
        font.setBold(True)

        for layer, layer_info in info.items():
            root = sniffer_s.CustomTreeWidgetItem(tree)
            root.setText(0, layer)
            root.setFont(0, font)  # 设置粗体字

            if layer_info:
                for key, value in layer_info.items():
                    if value is None:
                        value = ''
                    node = sniffer_s.CustomTreeWidgetItem(root)
                    node.setText(0, key)
                    node.setText(1, value)
                    root.addChild(node)

        tree.expandAll()
        tab.setCurrentIndex(0)

    # 展示hex信息
    def hex(sniffer_s, item: QTableWidgetItem):
        row = item.row()
        number = int(sniffer_s.ui.table.item(row, 0).text()) - 1
        text: QTextBrowser = sniffer_s.ui.hex_text
        text.clear()
        hex_info = sniffer_s.s.packet_list[number].hex_info
        text.setText(hex_info)

    # def look_up(sniffer_s):
    #     try:
    #         search_text: QLineEdit = sniffer_s.ui.search_text
    #         text = search_text.text()
    #         sniffer_s.clear_table()
    #         if text == '':
    #             for p in sniffer_s.s.packet_list:
    #                 sniffer_s.contiue(p)
    #         else:
    #             searcher = PacketFind(sniffer_s.s.packet_list, text)
    #             result = searcher.find_packet()
    #             for p in result:
    #                 sniffer_s.contiue(p)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         import traceback
    #         traceback.print_exc()

    def save(sniffer_s):
        try:
            save_list = []
            assemble_rows = sniffer_s.ui.table.selectedIndexes()
            rows = set(tmp_row.row() for tmp_row in assemble_rows)
            if len(rows) > 0:
                for row in rows:
                    number = int(sniffer_s.ui.table.item(row, 0).text()) - 1
                    save_list.append(sniffer_s.s.packet_list[number].to_dict())
                for i, save_dict in enumerate(sorted(save_list, key=lambda x: x['time'])):
                    save_dict['number'] = i + 1
                filepath, _ = QFileDialog.getSaveFileName(
                    sniffer_s,  # 父窗口对象
                    "保存文件",  # 标题
                    "./save/",  # 起始目录
                    "json类型 (*.json);;All Files (*)"
                )
                if filepath:
                    with open(filepath, 'w') as f:
                        f.write(json.dumps(save_list))
                        f.close()
                    QMessageBox.information(sniffer_s, '提示', '保存成功', QMessageBox.Yes)
            else:
                QMessageBox.warning(sniffer_s, "警告", "至少选择一个包。", QMessageBox.Yes)
        except Exception as e:
            print(e)

    def read(sniffer_s):
        file, _ = QFileDialog.getOpenFileName(sniffer_s, "选择已保存的文件", '', '(*.json)')
        if file:
            try:
                sniffer_s.clear()
                packet_list1 = []
                with open(file, 'r') as f:
                    save_list = json.loads(f.read())
                    for packet_dict in save_list:
                        p = Packet()
                        p.from_dict(packet_dict)
                        packet_list1.append(p)
                    sniffer_s.s.packet_list = packet_list1
                    f.close()
                for p in sniffer_s.s.packet_list:
                    sniffer_s.contiue(p)
                QMessageBox.information(sniffer_s, '提示', '读取成功', QMessageBox.Yes)
            except Exception as e:
                QMessageBox.warning(sniffer_s, "警告", "读取出现异常", QMessageBox.Yes)
                print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象
    window = M_window()  # 创建MainWindow对象
    window.showMaximized()  # 显示最大化的窗口
    window.ui.table.setColumnWidth(4, 150)
    window.ui.table.setColumnWidth(5, 150)
    window.ui.table.setColumnWidth(6, 170)
    sys.exit(app.exec_())  # 运行事件循环
