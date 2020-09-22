import struct
import socket
import select


def send_one_ping(to='1.1.1.1'):
    ping_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
    checksum = 49410
    header = struct.pack('!BBHHH', 8, 0, checksum, 0x123, 1)
    data = b'BCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwx'
    header = struct.pack('!BBHHH', 8, 0, checksum, 0x123, 1)
    packet = header + data
    ping_socket.sendto(packet, (to, 1))
    inputready, _, _ = select.select([ping_socket], [], [], 1.0)
    if inputready == []:
       raise Exception('NO INTERNET')
    _, address = ping_socket.recvfrom(2048)
    return (address, inputready)

def has_internet():
   try:
      data = send_one_ping()
      return True
   except Exception:
      return False


has_internet('1.1.1.1')