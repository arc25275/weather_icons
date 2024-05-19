# Weather Icons

This is a small app made to create weather icons in the form of svg files based on input through [ZeroMQ](https://zeromq.org/).

## Requesting Data

To request data, setup a [ZeroMQ Request-Reply Pattern](https://zeromq.org/socket-api/#request-reply-pattern), with the port being 5555. 
Specific examples for most programming languages can be found [here.](https://zeromq.org/get-started/). 

Data needs to be requested with a **_stringified_** json object in the following format:

```json5


{
  "sun": Bool, //True is Day, False is Night
  // For rain, snow, clouds, and wind, 0 means there is none, and 1,2, and 3 are varying levels of intensity.
  "rain": 0-4, // If rain is 4, it means there is lightning.
  "snow": 0-3,
  "clouds": 0-3,
  "wind": 0-3,
}
```

For example, in python, the following format is used.

```py
import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")
data = {
    "sun": False,
    "rain": 2,
    "snow": 0,
    "clouds": 3,
    "wind": 1
}
socket.send_string(json.dumps(data))
```


## Recieving Data
Data is recieved with the same socket, but it will not be a string this time, but instead be a normal message, in the form of a binary encoded string. 
For example in python, it will come in the format `b"..."`.

To recieve this data, all you need to do is call the function to recieve though the socket, like so in python:

```py
data = socket.recv()
```

The data itself will be svg code that you can then use for whatever purposes that you require. You could save it in a file to use for later, or dynamically load the svg depending on what inputs you have.

For the example data above, the output svg will be

```xml
<?xml version='1.0' encoding='ASCII' standalone='yes'?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
  <g>
    <g transform="translate(120, -50) scale(1 1) ">
      <style type="text/css">
        .night{fill:#F9D5A8;stroke:#F9D5A8;stroke-width:0.8035;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:113.3858;}
      </style>
      <path class="night" d="M222.1,194.9c58.1-23.5,124.1,4.5,147.6,62.6c23.5,58.1-4.5,124.1-62.6,147.6c-27.3,11-57.8,11-85,0  c58.1-23.5,86.1-89.6,62.6-147.6C273.1,229,250.6,206.4,222.1,194.9z"/>
    </g>
  </g>
  <g>
    <g transform="translate(0, 200) scale(1 1) ">
      <style type="text/css">
        .windy_rain2{fill:#009AD1;stroke:#009AD1;stroke-width:0.8035;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:113.3858;}
      </style>
      <path class="windy_rain2" d="M376.6,360.3l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C375.4,366.3,376.5,363.4,376.6,360.3z"/>
      <path class="windy_rain2" d="M410.5,432.9l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C409.3,439,410.4,436,410.5,432.9z"/>
      <path class="windy_rain2" d="M209.5,239.1l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C208.4,245.2,209.4,242.2,209.5,239.1z"/>
      <path class="windy_rain2" d="M289.4,268.2l1.1-42.3L264.2,259c-4.9,6.1-3.9,15,2.3,19.9s15,3.9,19.9-2.3  C288.3,274.3,289.4,271.3,289.4,268.2z"/>
      <path class="windy_rain2" d="M255.6,195.6l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C254.4,201.6,255.5,198.6,255.6,195.6z"/>
      <path class="windy_rain2" d="M449.3,326.4l1.1-42.3L424,317.2c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C448.1,332.4,449.2,329.5,449.3,326.4z"/>
      <path class="windy_rain2" d="M335.5,224.6l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C334.3,230.7,335.4,227.7,335.5,224.6z"/>
      <path class="windy_rain2" d="M250.7,374.8l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C249.5,380.8,250.6,377.8,250.7,374.8z"/>
      <path class="windy_rain2" d="M296.7,331.2l1.1-42.3L271.4,322c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C295.5,337.2,296.6,334.3,296.7,331.2z"/>
      <path class="windy_rain2" d="M170.7,345.7l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9s15,3.9,19.9-2.3  C169.6,351.7,170.7,348.8,170.7,345.7z"/>
      <path class="windy_rain2" d="M415.4,253.7l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C414.2,259.8,415.3,256.8,415.4,253.7z"/>
      <path class="windy_rain2" d="M456.5,389.4l1.1-42.3l-26.4,33.1c-4.9,6.1-3.9,15,2.3,19.9c6.1,4.9,15,3.9,19.9-2.3  C455.3,395.4,456.4,392.4,456.5,389.4z"/>
    </g>
  </g>
  <g>
    <g>
      <style type="text/css">
        .cloudy3{fill:#888888;stroke:#888888;stroke-width:0.8035;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:113.3858;}
      </style>
      <path class="cloudy3" d="M118.2,441.7h122.7h240.9c39.1,0,70.9-31.7,70.9-70.9S521,300,481.8,300c0-54.8-44.4-99.2-99.2-99.2  c-11.9,0-23.6,2.1-34.7,6.3C296.6,148,207.1,141.7,148,193c-31.7,27.5-49.5,67.6-48.8,109.6c-37.7,10.5-59.8,49.5-49.3,87.2  C58.4,420.5,86.3,441.7,118.2,441.7z"/>
    </g>
  </g>
</svg>
```

And when rendered, it will look like this:

![Example Weather](./example_weather.svg?raw=true)

## UML
