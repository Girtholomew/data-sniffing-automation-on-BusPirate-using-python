'''
Pins used:
Arduino 1 | Arduino 2 | Buspirate
A4       --> A4       --> MOSI
A5       --> A5       --> CLK
5V       --> Vin      --> Vp
GND      --> GND      --> GND
'''

import time
import serial
ser=serial.Serial('COM9',115200,timeout=1)
ser.write(str('#' + '\n').encode('ascii'))
time.sleep(0.3)

ser.write(str('m' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())
time.sleep(0.3)
ser.write(str('4' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('W' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('P' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
print('Sniffing Traffic....',end='')
ser.write(str('(2)' + '\n').encode('ascii'))
time.sleep(6)
print('..')
ser.write(str('q' + '\n').encode('ascii'))
x = ser.readlines(1000)
print((str(x[3])[2::])[:-5:])

ser.write(str('#' + '\n').encode('ascii'))
ser.close()
