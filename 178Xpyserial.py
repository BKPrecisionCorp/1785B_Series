import serial
import time
comNum = input("COMM port number?")
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM'+comNum
ser.timeout = 1
ser.open()
open = ser.is_open
ser.flush

print("BK178X Command 0x31")
#enable remote mode
cmd=[0xAA,0,0x20,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xcb]
ser.write(cmd)
resp = ser.read(26)

#read the Model, Serial Number, FW, etc... (CMD 0x31)
cmd=[0xAA,0,0x31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xDB]
ser.write(cmd)
resp = ser.read(26)

print("---------------------")
print("byte\tHex\tASCII")
print("---------------------")
for x in range(26):
 print(x,"\t" ,hex(resp[x]), "\t", chr(resp[x]))

print("---------------------")

model = "Model:\t"
for n in range(5):
 index = n+3
 model+=chr(resp[index])

print(model)

sn = "Serial:\t"
for n in range(10):
 index = n+10
 sn += chr(resp[index])

print(sn)

fw = "FW:\tV" + str(resp[9]) + "." + str(resp[8])
print(fw)
ser.close()
input("Hit [enter] to exit?")
