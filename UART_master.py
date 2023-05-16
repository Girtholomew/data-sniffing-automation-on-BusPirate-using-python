'''
Pins used:
D10 --> D1  --> MOSI
D11 --> D0  --> MISO
GND --> GND --> GND
'''

import time 
import serial
from serial import Serial
ser  = serial.Serial(port = 'COM9',baudrate = 115200,timeout=1)

ser.write(str('#' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)
ser.write(str('m' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('3' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('5' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)

ser.write(str('W' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('(0)' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.1)

ser.write(str('(2)' + '\n').encode('ascii'))
time.sleep(10)
ser.write(str('q' + '\n').encode('ascii'))

l = ser.readlines(1000)
print((str(l))[3::][:-6:])

ser.write(str('#' + '\n').encode('ascii'))
ser.close()