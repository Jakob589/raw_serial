#!/usr/bin/env python3

import zerorpc
import serial
import time
import os


def serial_read():
    ser = serial.Serial('/dev/ttyS2',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_ODD,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1)
    for x in range(5):
        try:
            serial_data = ser.readline().decode('utf-8')

            length = serial_data.split(",")
            if length != 54:
                raise ValueError("len err") 

            return serial_data
            
        except:
            print("serial error")
            time.sleep(.1)
            continue

  

class rawser(object):
    def read(self, name): 
        
        seconds = int(round(time.time()*1000))
        data = ("%d," % seconds)  + serial_read()
        
        return data
    
    def NILMoff(self,name):
        os.system('systemctl stop saam-comread.service ')
        os.system('sleep 50000 && systemctl start saam-comread.service &')
        

    def NILMon(self,name):
        os.system('timeout 1 sudo getty -L -f 115200 ttyS2 vt100')
        os.system('systemctl start saam-comread.service')


s = zerorpc.Server(rawser())
s.bind("tcp://0.0.0.0:4503")
s.run()
