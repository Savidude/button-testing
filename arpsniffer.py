import socket
import struct
import binascii

import configparser

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))


config = configparser.ConfigParser()
config.read('config.ini')

address = config['ADDRESS']
dash_mac = address['DashAddress']
dialog_mac = address['DialogAddress']

while True:

    packet = rawSocket.recvfrom(2048)

    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue


    source_mac = binascii.hexlify(arp_detailed[5])

    if dialog_mac==source_mac:
        print "Dialog button pressed! Souce: ", source_mac
    if dash_mac==source_mac:
        print "Amazon Dash button pressed! Souce: ", source_mac
