# -*- coding: UTF-8 -*-
import serial
import time
import serial.tools.list_ports
import re
import json
import redis

config = dict(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(**config)

prog = re.compile(r'{("\w+":-*\d*.*\d*,*){1,10}}')

dev_ls = serial.tools.list_ports.comports()
dev = dev_ls[0].device
ser = serial.Serial(dev, 9600, timeout=1)

# ser.write(str.encode("hello, I am hick, the time is : " + time.strftime("%Y-%m-%d %X\n")))


if __name__ == '__main__':
    while True:
        data = ser.readline().decode("utf-8")
        # data_from_json = json.loads(data)
        result = prog.match(data)
        if result is not None:
            # print(data)
            data_from_json = json.loads(data)
            r.set('I0T', data_from_json["a"])
            print(data_from_json)
