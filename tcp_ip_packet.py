import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

ip_header  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service / Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification / Flags, Fragment Offset
ip_header += b'\x40\x06\xa6\xec'  # TTL, Protocol / Header Checksum
ip_header += b'\x0a\x00\x02\x0F'  # Source Address
ip_header += b'\x5b\x8e\xd6\xb5'  # Destination Address 

tcp_header  = b'\x30\x39\x00\x50' # Source Port / Destination Port
tcp_header += b'\x00\x00\x00\x00' # Sequence Number
tcp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
tcp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags / Window Size
tcp_header += b'\xcf\xf6\x00\x00' # Checksum / Urgent Pointer (YOU MUST CHECK ON WIRESHARK)
                                  # Wireshark -> Edit -> Preferences -> Protocol -> TCP -> Validate Checksum

packet = ip_header + tcp_header
s.sendto(packet, ('91.142.214.181', 0))

"""
Created by 8wat 

  ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄   ▄▀▀▀█▀▀▄ 
 █   █    ▐  █ ▐ ▄▀ ▀▄ █    █  ▐ 
 ▐  █        █   █▄▄▄█ ▐   █     
   █   ▄    █   ▄▀   █    █      
    ▀▄▀ ▀▄ ▄▀  █   ▄▀   ▄▀       
          ▀    ▐   ▐   █         
                       ▐         
"""
