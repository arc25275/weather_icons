import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
print("Starting Connection")
socket.connect("tcp://localhost:5555")

weather_list = [
    {
        "sun": True,
        "rain": 0,
        "snow": 0,
        "clouds": 0,
        "wind": 0,
        "temp": 75
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1,
        "temp": 55
    },
    {
        "sun": True,
        "rain": 0,
        "snow": 0,
        "clouds": 0,
        "wind": 0,
        "temp": 75
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1,
        "temp": 55
    },
    {
        "sun": True,
        "rain": 4,
        "snow": 0,
        "clouds": 3,
        "wind": 0,
        "temp": 75
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1,
        "temp": 55
    }
]

for i in weather_list:
    print(i)
    socket.send_string(json.dumps(i))
    time.sleep(1)
    print(socket.recv_string())

