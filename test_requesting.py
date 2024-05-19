import json
import time

import zmq

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
        "wind": 0
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1
    },
    {
        "sun": True,
        "rain": 0,
        "snow": 0,
        "clouds": 0,
        "wind": 0
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1
    },
    {
        "sun": True,
        "rain": 0,
        "snow": 3,
        "clouds": 3,
        "wind": 0
    },
    {
        "sun": False,
        "rain": 2,
        "snow": 0,
        "clouds": 3,
        "wind": 1
    }
]


def test_weather():
    for i in weather_list:
        print(i)
        socket.send_string(json.dumps(i))
        time.sleep(1)
        response = socket.recv()
        print(response)
        if response != "Invalid Weather":
            assert True
