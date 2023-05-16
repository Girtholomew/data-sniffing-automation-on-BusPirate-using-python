'''
Pins used:
D13 --> D13 --> CLK
D12 --> D12 --> MISO
D11 --> D11 --> MOSI
D10 --> D10 --> CS
GND --> GND --> GND
Vin --> Vin 
'''

import time
import serial
ser=serial.Serial('COM9',115200,timeout=1)
ser.write(str('#' + '\n').encode('ascii'))
time.sleep(0.3)

ser.write(str('m' + '\n').encode('ascii'))
for i in ser.readlines():
    print((str(i.strip())))
time.sleep(0.3)

ser.write(str('5' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('4'+'\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('2' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())
    
time.sleep(0.3)
ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('2' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('1' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('W' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.5)
ser.write(str('W' + '\n').encode('ascii'))
for i in ser.readlines():
    print(i.strip())

time.sleep(0.3)
ser.write(str('(2)' + '\n').encode('ascii'))
print("Capturing Packets....",end='')
time.sleep(15)
print('..',end='')
print('..')
ser.write(str('q' + '\n').encode('ascii'))
x = ser.readlines(1000)

print(str(x[3])[3::][:-5:])

ser.write(str('#' + '\n').encode('ascii'))
ser.close()