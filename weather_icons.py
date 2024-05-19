import json

import svgutils.transform as sg
import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    print("Starting Server")
    socket.bind("tcp://*:5555")

    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        print(f"Received request: {message}")
        message = json.loads(message)
        if not validate_weather(message):
            socket.send_string("Invalid Weather")
            continue
        weather = combine_weather(message)
        print(f"Combined Weather: {weather}")
        socket.send_string(json.dumps(weather))
        generate_icons(weather)


def validate_weather(weather):
    if not isinstance(weather, dict):
        return False
    if weather["sun"] > 3 or weather["sun"] < 0:
        return False
    if weather["rain"] > 4 or weather["rain"] < 0:
        return False
    if weather["snow"] > 3 or weather["snow"] < 0:
        return False
    if weather["clouds"] > 3 or weather["clouds"] < 0:
        return False
    if weather["wind"] > 3 or weather["wind"] < 0:
        return False
    if weather["rain"] > 1 and weather["clouds"] == 0:
        return False
    return True


def combine_weather(weather):
    new_weather = {
        "main_weather": None,
        "secondary_weather": None,
        "time": "day"
    }
    if not weather["sun"]:
        # If no sun, show a moon
        new_weather["time"] = "night"

    # Main Weather
    if weather["clouds"] > 0:
        # Cloud level 1 is a little cloudy, 2 is mostly cloudy, 3 is very cloudy
        new_weather["main_weather"] = f"cloudy{weather['clouds']}"
    elif weather["clouds"] == 0:
        # Clear weather
        new_weather["main_weather"] = "clear"

    # Secondary Weather
    if weather["rain"] == 4:
        # Lightning
        new_weather["secondary_weather"] = "lightning"
    elif weather["rain"] > 0 and weather["snow"] > 0:
        # If it is raining and snowing, show sleet
        new_weather["secondary_weather"] = "sleet"
    elif weather["rain"] > 0 and weather["wind"] > 0:
        # If it is raining and windy, show windy rain / Storm
        new_weather["secondary_weather"] = f"windy_rain{weather['rain']}"
    elif weather["rain"] > 0:
        # Rain
        new_weather["secondary_weather"] = f"rain{weather['rain']}"
    elif weather["snow"] > 0:
        # Snow
        new_weather["secondary_weather"] = f"snow{weather['snow']}"
        # Wind
    elif weather["wind"] > 0:
        new_weather["secondary_weather"] = f"wind{weather['wind']}"
    return new_weather


def generate_icons(new_weather):
    time, main_weather, secondary_weather = new_weather["time"], new_weather["main_weather"], new_weather[
        "secondary_weather"]
    fig = sg.SVGFigure("5in", "5in")
    time_fig = sg.fromfile(f"./icons/{time}.svg").getroot()
    time_fig.moveto(120, -50)
    fig.append([time_fig])
    if secondary_weather:
        secondary_fig = sg.fromfile(f"./icons/{secondary_weather}.svg").getroot()
        secondary_fig.moveto(0, 200)
        fig.append([secondary_fig])
    if main_weather != "clear":
        main_fig = sg.fromfile(f"./icons/{main_weather}.svg").getroot()
        fig.append([main_fig])
    fig.save(f"./weather_{main_weather}_{secondary_weather}_{time}.svg")


if __name__ == "__main__":
    main()
