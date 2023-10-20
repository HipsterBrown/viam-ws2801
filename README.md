# WS2801 Module Component

_ws2801_ is a Viam modular component that provides control of ws2801 addressable RGB LEDs, like [these on Adafruit](https://www.adafruit.com/search?q=ws2801&a%5B%5D=i).

Uses the [`adafruit-circuitpython-ws2801`](https://docs.circuitpython.org/projects/ws2801/en/latest/index.html) library.

## Prerequisites

If you're new to using ws2801-based addressable LEDs (not to be confused with ws2812, or neopixels), check out this overview from Adafruit about how they work and power considerations: https://learn.adafruit.com/12mm-led-pixels/overview 

## Viam Module Configuration

**clock_pin** *Required*:
The pin to output the clock signal on. This can be a standard Digital Out GPIO pin or the serial clock (SCK/SLCK) for hardware-driven SPI.

**data_pin** *Required*:
The pin to output the data signal on. This can be a standard Digital Out GPIO pin or the controller output (PICO/MOSI) for hardware-driven SPI.

**led_count** *Required*:
This is the number of LEDs (or pixels) to control.

**default_brightness** (Optional):
Defaults to "1.0"

## SDK Usage

Since this module has a custom API, this repo must be included as a dependency in your client code. It can be listed in your `requirements.txt` as the following:

```
ws2801 @ git+https://github.com/hipsterbrown/viam-ws2801.git@main
```

Then install with `pip`:

```
pip install -r requirements.txt
```

After adding and configuring this module for your machine through the Viam app:

```python
import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from ws2801 import Rgb

async def connect():
    creds = Credentials(
        type='robot-location-secret',
		# Replace "<SECRET>" (including brackets) with your robot's secret
        payload='<SECRET>')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('<Robot Location>', opts)

async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)
    
    # lights
    lights = Rgb.from_robot(robot, "lights")
    print("Starting RGB animation!")
    # create background task for animation, it will go forever
    animation = asyncio.create_task(lights.animate())
    # wait for a few seconds
    await asyncio.sleep(10)
    await lights.stop()
    print("Animation stopped!")

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
```
