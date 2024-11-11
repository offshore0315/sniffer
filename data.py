import re



class Packet:

    def __init__(sniffer_s):

        sniffer_s.number = None
        sniffer_s.time = None
        sniffer_s.protocol = None
        sniffer_s.src = None
        sniffer_s.dst = None
        sniffer_s.length = None
        sniffer_s.info = None
        sniffer_s.detail_info = {}
        sniffer_s.raw_data = None
        sniffer_s.hex_info = None
        sniffer_s.payload = None
        sniffer_s.color = None

    def from_args(sniffer_s, number, time, src, dst, protocol, length, info, raw_data, hex_info, payload=''):
        sniffer_s.number = number
        sniffer_s.time = time
        sniffer_s.protocol = protocol
        sniffer_s.src = src
        sniffer_s.dst = dst
        sniffer_s.length = length
        sniffer_s.info = info
        sniffer_s.detail_info = {}
        sniffer_s.raw_data = raw_data
        sniffer_s.hex_info = hex_info
        sniffer_s.payload = payload
        sniffer_s.get_detail()

    def from_dict(sniffer_s, packet_dict: dict):
        for key, value in packet_dict.items():
            sniffer_s.__dict__[key] = value


    def get_detail(sniffer_s):
        sniffer_s.detail_info = sniffer_s.extract_layers_info(sniffer_s.raw_data)

    def extract_layers_info(sniffer_s, raw_data):
        pattern = r'###\[ (\w+) \]###'
        layers = re.findall(pattern, raw_data)
        detail_info = {layer: {} for layer in layers}

        for layer in layers:
            extraction_method = getattr(sniffer_s, f"extract_{layer.lower()}_info", None)
            if extraction_method:
                detail_info[layer] = extraction_method(raw_data)
            else:
                print(f"No extraction method found for layer: {layer}")

        return detail_info

    def extract_ethernet_info(sniffer_s, raw_data):
        ethernet_pattern = r'''
         ###[ Ethernet ]###\s+
         dst\s+=\s+(.*)\s+
         src\s+=\s+(.*)\s+
         type\s+=\s+(.*)'''
        match = re.search(ethernet_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '目的地址': match.group(1),
                '源地址': match.group(2),
                '类型': match.group(3)
            }
        return {}

    def extract_ip_info(sniffer_s, raw_data):
        ip_pattern = r'''
         ###[ IP ]###\s+
         version\s+=\s+(.*)\s+
         ihl\s+=\s+(.*)\s+
         tos\s+=\s+(.*)\s+
         len\s+=\s+(.*)\s+
         id\s+=\s+(.*)\s+
         flags\s+=\s+(.*)\s+
         frag\s+=\s+(.*)\s+
         ttl\s+=\s+(.*)\s+
         proto\s+=\s+(.*)\s+
         chksum\s+=\s+(.*)\s+
         src\s+=\s+(.*)\s+
         dst\s+=\s+(.*)\s+
         \\options\s+\\'''
        match = re.search(ip_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '版本': match.group(1),
                '报头长度': match.group(2),
                '服务类型': match.group(3),
                '总长度': match.group(4),
                '标识': match.group(5),
                '分段标志': match.group(6),
                '段偏移': match.group(7),
                '生存期': match.group(8),
                '协议': match.group(9),
                '校验和': match.group(10),
                '源地址': match.group(11),
                '目的地址': match.group(12)
            }
        return {}




    def extract_unknown_layer_info(sniffer_s, raw_data, layer):
        print(f"Unknown layer: {layer}")
        return {}

    def extract_tcp_info(sniffer_s, raw_data):
        tcp_pattern = r'''
           ###[ TCP ]###\s+
           sport\s+=\s+(.*)\s+
           dport\s+=\s+(.*)\s+
           seq\s+=\s+(.*)\s+
           ack\s+=\s+(.*)\s+
           dataofs\s+=\s+(.*)\s+
           reserved\s+=\s+(.*)\s+
           flags\s+=\s+(.*)\s+
           window\s+=\s+(.*)\s+
           chksum\s+=\s+(.*)\s+
           urgptr\s+=\s+(.*)\s+
           options\s+=\s+(.*)'''
        match = re.search(tcp_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '源端口': match.group(1),
                '目的端口': match.group(2),
                '序号': match.group(3),
                '确认号': match.group(4),
                '数据偏移': match.group(5),
                '保留位': match.group(6),
                '标志位': match.group(7),
                '窗口大小': match.group(8),
                '校验和': match.group(9),
                '紧急指针': match.group(10),
                '选项': match.group(11)
            }
        return {}


    def extract_udp_info(sniffer_s, raw_data):
        udp_pattern = r'''
        ###[ UDP ]###\s+
        sport\s+=\s+(.*)\s+
        dport\s+=\s+(.*)\s+
        len\s+=\s+(.*)\s+
        chksum\s+=\s+(.*)'''
        match = re.search(udp_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '源端口': match.group(1),
                '目的端口': match.group(2),
                '长度': match.group(3),
                '校验和': match.group(4)
            }
        return {}


    def extract_ipv6_info(sniffer_s, raw_data):
        ipv6_pattern = r'''
        ###[ IPv6 ]###\s+
        version\s+=\s+(.*)\s+
        tc\s+=\s+(.*)\s+
        fl\s+=\s+(.*)\s+
        plen\s+=\s+(.*)\s+
        nh\s+=\s+(.*)\s+
        hlim\s+=\s+(.*)\s+
        src\s+=\s+(.*)\s+
        dst\s+=\s+(.*)'''
        match = re.search(ipv6_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '版本': match.group(1),
                '流量分类': match.group(2),
                '流标签': match.group(3),
                '有效载荷长度': match.group(4),
                '下一个头类型': match.group(5),
                '最大跳数': match.group(6),
                '源地址': match.group(7),
                '目的地址': match.group(8)
            }
        return {}



    def extract_arp_info(sniffer_s, raw_data):
        arp_pattern = r'''
        ###[ ARP ]###\s+
        hwtype\s+=\s+(.*)\s+
        ptype\s+=\s+(.*)\s+
        hwlen\s+=\s+(.*)\s+
        plen\s+=\s+(.*)\s+
        op\s+=\s+(.*)\s+
        hwsrc\s+=\s+(.*)\s+
        psrc\s+=\s+(.*)\s+
        hwdst\s+=\s+(.*)\s+
        pdst\s+=\s+(.*)'''
        match = re.search(arp_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '硬件类型': match.group(1),
                '协议类型': match.group(2),
                '硬件地址长度': match.group(3),
                '协议长度': match.group(4),
                '操作类型': match.group(5),
                '源MAC地址': match.group(6),
                '源IP地址': match.group(7),
                '目的MAC地址': match.group(8),
                '目的IP地址': match.group(9)
            }
        return {}


    def extract_icmp_info(sniffer_s, raw_data):
        icmp_pattern = r'''
           ###[ ICMP ]###\s+
           type\s+=\s+(.*)\s+
           code\s+=\s+(.*)\s+
           chksum\s+=\s+(.*)\s+
           id\s+=\s+(.*)\s+
           seq\s+=\s+(.*)\s+
           unused\s+=\s+(.*)'''
        match = re.search(icmp_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '类型': match.group(1),
                '代码': match.group(2),
                '校验和': match.group(3),
                '标识': match.group(4),
                '序号': match.group(5),
                '未使用': match.group(6)
            }
        return {}

    def extract_padding_info(sniffer_s, raw_data):
        padding_pattern = r'''
              ###[ Padding ]###\s+
              load\s+=\s+(.*)'''
        match = re.search(padding_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '数据': match.group(1)
            }
        return {}


    def extract_raw_info(sniffer_s, raw_data):
        raw_pattern = r'''
           ###[ Raw ]###\s+
           load\s+=\s+(.*)'''
        match = re.search(raw_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '负载': match.group(1)
            }
        return {}


    def extract_dns_info(sniffer_s, raw_data):
        dns_pattern = r'''
        ###[ DNS ]###\s+
        id\s+=\s+(\d+)\s+
        qr\s+=\s+(\d+)\s+
        opcode\s+=\s+(\w+)\s+
        aa\s+=\s+(\d+)\s+
        tc\s+=\s+(\d+)\s+
        rd\s+=\s+(\d+)\s+
        ra\s+=\s+(\d+)\s+
        z\s+=\s+(\d+)\s+
        ad\s+=\s+(\d+)\s+
        cd\s+=\s+(\d+)\s+
        rcode\s+=\s+(\w+)\s+
        qdcount\s+=\s+(\d+)\s+
        ancount\s+=\s+(\d+)\s+
        nscount\s+=\s+(\d+)\s+
        arcount\s+=\s+(\d+)
        '''
        match = re.search(dns_pattern, raw_data, re.VERBOSE)
        if match:
            return {
                '事务ID': match.group(1),
                '查询/响应标志': match.group(2),
                '操作码': match.group(3),
                '授权应答标志': match.group(4),
                '截断标志': match.group(5),
                '期望递归标志': match.group(6),
                '递归可用标志': match.group(7),
                '保留字段': match.group(8),
                '验证应答标志': match.group(9),
                '检查禁止标志': match.group(10),
                '响应码': match.group(11),
                '问题计数': match.group(12),
                '答案记录计数': match.group(13),
                '授权记录计数': match.group(14),
                '附加记录计数': match.group(15)
            }
        return {}

    def to_dict(sniffer_s):
        return {'number': sniffer_s.number, 'time': sniffer_s.time, 'src': sniffer_s.src, 'dst': sniffer_s.dst,
                'protocol': sniffer_s.protocol, 'length': sniffer_s.length, 'info': sniffer_s.info, 'detail_info': sniffer_s.detail_info,
                'hex_info': sniffer_s.hex_info, 'payload': sniffer_s.payload}