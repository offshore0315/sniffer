import scapy.utils
from scapy.all import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from data import Packet
import time
import re
import signal

class PacketSniff:

    def __init__(sniffer_s, gui_interface: QWidget):
        sniffer_s.signal_triggers = signal.Signal_s()
        sniffer_s.gui: QWidget = gui_interface
        sniffer_s.network_interface = ''
        sniffer_s.filter_criteria = ''
        sniffer_s.packet_count = 0
        sniffer_s.capture_time = 0
        sniffer_s.sniffer_instance = None
        sniffer_s.capture_active = False
        sniffer_s.current_packet_data = None
        sniffer_s.packet_list = []

    def activate(sniffer_s):
        sniffer_s.network_interface = sniffer_s.gui.if_box.currentText()
        if sniffer_s.network_interface == '网卡':
            return
        sniffer_s.reset_data()  # Reset data before activating
        sniffer_s.capture_active = True
        sniffer_s.sniffer_instance = AsyncSniffer(
            iface=sniffer_s.network_interface, prn=sniffer_s.process_packet,
            filter=sniffer_s.filter_criteria
        )
        sniffer_s.capture_time = time.time()
        sniffer_s.sniffer_instance.start()

    def deactivate(sniffer_s):
        sniffer_s.sniffer_instance.stop()
        sniffer_s.capture_active = False

    def reset_data(sniffer_s):
        sniffer_s.packet_count = 0
        sniffer_s.packet_list.clear()

    def update_filter(sniffer_s, filter_string):
        sniffer_s.filter_criteria = filter_string


    def identify_protocol(sniffer_s):
        protocol_chain = sniffer_s.current_packet_data.summary().split('/')
        arp_protocol_list = ['ARP', 'RARP', 'DHCP']
        for protocol in arp_protocol_list:
            if protocol in protocol_chain[1]:
                return protocol
        if 'IP' in protocol_chain[1]:
            if 'Raw' in protocol_chain[-1] or 'Padding' in protocol_chain[-1]:
                upper_protocol = protocol_chain[-2]
            else:
                upper_protocol = protocol_chain[-1]
            return upper_protocol.strip().split(' ')[0]
        elif 'IPv6' in protocol_chain[1]:
            return 'IPv6/' + protocol_chain[2].strip().split(' ')[0]
        else:
            protocol = protocol_chain[2].strip().split(' ')[0]
            if protocol != '':
                protocol += '/'
            protocol += protocol_chain[2].split(' ')[1]
            return protocol

    def fetch_packet_info(sniffer_s, protocol):
        protocol_chain = sniffer_s.current_packet_data.summary().split("/")
        if "Ether" in protocol_chain[0]:
            if 'ARP' in protocol:
                arp_info = protocol_chain[1].strip()
                pattern_request = r'ARP who has (\S+) says (\S+)'
                pattern_reply = r'ARP is at (\S+) says (\S+)'
                if match := re.match(pattern_request, arp_info):
                    target = match.group(1)
                    sender = match.group(2)
                    info = f'Who has {target}? Tell {sender}'
                elif match := re.match(pattern_reply, arp_info):
                    mac = match.group(1)
                    sender = match.group(2)
                    info = f'{sender} is at {mac}'
                else:
                    info = protocol_chain[1].strip()
            elif 'DNS' in protocol:
                info = protocol_chain[-1].strip()
            elif 'TCP' in protocol or 'UDP' in protocol:
                info = ' '.join(protocol_chain[2:]).strip()
            else:
                info = ' '.join(protocol_chain[1:]).strip()
            return info
        else:
            return sniffer_s.current_packet_data.summary()

    def extract_src_and_dst(sniffer_s):
        if sniffer_s.current_packet_data.haslayer('IP'):
            src = sniffer_s.current_packet_data['IP'].src
            dst = sniffer_s.current_packet_data['IP'].dst
        else:
            src = sniffer_s.current_packet_data[0].src
            dst = sniffer_s.current_packet_data[0].dst
            if dst == 'ff:ff:ff:ff:ff:ff':
                dst = 'Broadcast'
        return src, dst

    def process_packet(sniffer_s, pkt: Packet):
        sniffer_s.packet_count += 1
        sniffer_s.current_packet_data = pkt
        raw_output = pkt.show(dump=True)
        hex_output = scapy.utils.hexdump(pkt, dump=True)
        packet_timestamp = str(pkt.time - sniffer_s.capture_time)[0:9]
        src, dst = sniffer_s.extract_src_and_dst()
        protocol = sniffer_s.identify_protocol()
        packet_length = len(pkt)
        info = sniffer_s.fetch_packet_info(protocol)
        packet_detail = Packet()
        payload_output = str(bytes(pkt.payload.payload.payload))
        packet_detail.from_args(
            sniffer_s.packet_count, packet_timestamp, src, dst,
            protocol, packet_length, info, raw_output, hex_output, payload_output
        )
        sniffer_s.packet_list.append(packet_detail)
        sniffer_s.signal_triggers.update_table.emit(packet_detail)

    def reset_data(sniffer_s):
        sniffer_s.packet_count = 0
        sniffer_s.packet_list.clear()
