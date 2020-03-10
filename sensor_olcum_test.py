import serial
from PIL import Image
import codecs
import time
import array
import matplotlib.pyplot as plt
import numpy as np
from serial.tools import list_ports
from numpy import unicode
g_measuring_val_3 = ":01R023;69F5\r\n"
make_highest_baud_rate = ":01W006;4;61FC\r\n"
make_baud_rate_921600 = ":01W006;3;51FE\r\n"
rs485_unlock = ":01W010;0;E9C3\r\n"
baud_rates = [38400, 57600, 115200, 921600, 1843200]

print(g_measuring_val_3.encode('utf-8'))
img = Image.new('L', (227,227))  #default color = 0
img_pixels = img.load()
#for j in range(227):
#    for i in range(227):
#        img_pixels[j, i] = 150

def serial_ports():
    # produce a list of all serial ports. The list contains a tuple with the port number,
    # description and hardware address
    #
    ports = list(serial.tools.list_ports.comports())

    # return the port if 'USB' is in the description
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no
ser = serial.Serial(
    port=serial_ports(),
    baudrate=57600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


print(ser.isOpen())
print(ser.name)

#chekcking baud rate of the device
#and making the baud rate of the software is the same with the device
for i in range(5):
    print(baud_rates[i])
    ser.baudrate = baud_rates[i]
    ser.write(rs485_unlock.encode('utf-8'))
    time.sleep(3)
    if(ser.inWaiting()):
        print("Sensörün Baud Oranı:")
        print(baud_rates[i])
        break
    #print(veri)


ser.write(make_baud_rate_921600.encode('utf-8'))
#ser.write(make_baud_rate_921600.encode('utf-8'))
time.sleep(3)
#ser.baudrate = 921600
ser.baudrate = 921600
#
##onceki_data = []



data = []

#
for j in range(25):

    ac = ser.write(g_measuring_val_3.encode('utf-8'))
    # print(ac)
    data.append(ser.readline())
    print(data)
    #if (data != onceki_data):
    #    print(data)
#
    #onceki_data = data

ser.close()