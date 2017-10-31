import serial

ser = serial.Serial('COM3',38400,timeout = 3)

line = ser.readline()
print line.type
#while(line != "Ready"):
#	print line
#	line = ser.readline()

print "requesting pixel"
ser.write(b'512 512 \n')
bytes = ser.read(100)
s  = bytes.decode("utf-8")

ser.close()