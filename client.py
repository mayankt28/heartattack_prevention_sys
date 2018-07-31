import serial
import time
import asyncio
import websockets

serial_port = '/dev/ttyACM0';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt";

#output_file = open(write_to_file_path, "w+");
ser = serial.Serial(serial_port, baud_rate)
async def hello(uri):
    ws = await websockets.connect('ws://192.168.43.85:8000/dashboard/')
    while(True):
        line = ser.readline();
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line);
        await ws.send(line)
    
asyncio.get_event_loop().run_until_complete(
    hello('ws://192.168.43.85:8000/dashboard/'))
asyncio.get_event_loop().run_forever()

