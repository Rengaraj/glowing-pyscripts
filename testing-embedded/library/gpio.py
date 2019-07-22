from serial import Serial


def init(dev):
    """ Init will initialise serial device with serial properties

    Arguments:
         dev - serial device file name

    Returns:
         device - Serial device object with baudrate 9600 and timeout 2secs
    """
    device = Serial(dev, 9600, timeout = 2)
    return device


def gpio_write(dev, value):
    """ Send commands  via serial port to set GPIO 30
    of launch pad, which is connected to RED_LED of launch pad

    Arguments:
        dev - Serial object
        value - byte string (character) a to ON , b to OFF and c to get the
                state of GPIO 30

    Returns:
        None
    """
    dev.write(bytes(value))


def gpio_read(dev, value):
    """ Read the value of GPIO30 using GPIO10 of launch pad
    when you send character 'c' it will read the o/p of pin30

    Arguments:
        dev - Serial object
        value - character 'c' to read the data from serial port
        which is 1 or 0 (state of GPIO30)

    Returns:
        string - 0 or 1
    """
    dev.write(bytes(value))
    return dev.read()

device = init('/dev/ttyACM0')

gpio_write(device, 'b')
print gpio_read(device, 'c')
