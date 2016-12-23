'''
This program is to boot Linux zImage from
a tftp server at uBoot prompt.
'''

import serial
import time

RAM_MEM = '0x40008000'
ZIMAGE = 'zImage'
SPACE = ' '
IP = '192.168.0.1'
SERIAL_PORT = '/dev/ttyS0'
dev = serial.Serial(SERIAL_PORT, 115200)
dev.timeout = 2


def enter_in_to_uboot(ser_device):
    ser_device.write('\r')
    time.sleep(1)
    ser_device.write('\r')
    output = ser_device.readlines()
    return output


def print_output(ser_device):
    for line in ser_device.readlines():
        print line


def check_nw_connection(ser_device):
    '''
    Note: This function is not used in main()
    This function is for checking network connection
    from target to host.
    '''
    ser_device.write("ping" + SPACE + IP + '\r')
    ser_device.timeout = 6
    out = ser_device.readlines()
    for value in out:
        if 'ping' in value:
            return 0
        else:
            return -1


def boot_image(ser_device, ser_output, zimage):

    if ser_output[-1] == '=> ':
        print ser_output[-1]
        time.sleep(1)
        ser_device.write('tftp' + SPACE + RAM_MEM + SPACE + zimage)
        ser_device.write('\r')
        print_output(ser_device)
        ser_device.write('bootz' + SPACE + RAM_MEM)
        ser_device.write('\r')
        time.sleep(1)
        print_output(ser_device)
    else:
        return 0


def main(dev):
    console_out = enter_in_to_uboot(dev)
    if console_out == []:
        print "Warning:\n"
        print SERIAL_PORT + " has no data"
        print "Check your serial connection"
        return
    
    ret = boot_image(dev, console_out, ZIMAGE)

    if ret == 0:
        print "Check 1. Network Connection \n, 2. Tftp server status \n \
        3.Check Image is correct \n"

    dev.write("\r")
    console_out = dev.readlines()

    for value in console_out:
        if '#' in value:
            print "There you are!!!\nzimage is booted\n"
        elif '=>' in value:
            print "Still you are in uboot prompt Keep try one more time"


if __name__ == "__main__":
    main(dev)

dev.close()
