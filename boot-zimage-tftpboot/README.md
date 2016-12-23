# Boot Zimage Script

* The main purpose of the script is to avoid repeated
Job during Flashing.

* This script helps to boot `zimage` with out opening
a serial terminal software like minicom.

* This script can be used with Robot Frame Work in future
During flashing.

## Setup
Make sure following is right in your system.

 * Check network connection is established between
 host and target, properly configured with IP.
 * Check TFTP server is running properly
 * Check you have correct zImage file name in the tftp folder and
 boot-zimage.py.

## Usage

Linux:

By default inside the code `SERIAL_PORT` variable is set to /dev/ttyS0.
You can modify based on your system serial port connection.

 * Open a terminal go to the folder in which `boot-zimage.py` is located
 * Before reseting the board make sure you ready with the command
 
------
$ python boot-zimage.py
------
 * Once you give reset immediately you run the above command.
 * If all the setup is correct then you will see succesfull login in to
 Linux Zimage.
 
Windows:

The procedure is same. Instead of terminal open windows command prompt.

## Software Dependencies 

Make sure you have following software installed

 * Python 2.7+
 * Pyserial 3.2.1 

## Lmitations 

 * Error Handling is not yet matured.
 * You can use that by only with proper setup.
 
