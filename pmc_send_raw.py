import zerorpc
import serial
import io
import time

def serial_read():
    ser = serial.Serial('/dev/ttyS2',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_ODD,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1)

    sio = io.TextIOWrapper(io.BufferedReader(ser))
    while True:
            try:
                serial_data = sio.readline()
                data = serial_data.strip()
                data = serial_data           
                return data
            except:
                print("serial error")
                continue


class rawser(object):
    def read(self, name): 
        seconds = int(time.time())
        data = ("%d," % seconds)  + serial_read()
        
        return data
        



s = zerorpc.Server(rawser())
s.bind("tcp://0.0.0.0:4503")
s.run()
