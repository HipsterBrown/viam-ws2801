import asyncio
import random
from typing import ClassVar, Mapping
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from .api import Rgb
from adafruit_ws2801 import WS2801
from viam.logging import getLogger

LOGGER = getLogger(__name__)

class ws2801(Rgb, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("hipsterbrown", "led"), "ws2801")
    
    animating: bool
    clock_pin: int
    data_pin: int
    led_count: int
    brightness: float
    controller: WS2801

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        # here we validate config, the following is just an example and should be updated as needed
        clock_pin = config.attributes.fields["clock_pin"].number_value
        data_pin = config.attributes.fields["data_pin"].number_value
        led_count = config.attributes.fields["led_count"].number_value
        default_brightness = config.attributes.fields["default_brightness"].number_value

        if clock_pin == "":
            raise Exception("A clock_pin must be defined")

        if data_pin == "":
            raise Exception("A data_pin must be defined")

        if led_count == "":
            raise Exception("led_count must be defined")

        if isinstance(default_brightness, float) and (default_brightness > 1.0 or default_brightness < 0.0):
            raise Exception("default_brightness must be between 0.0 and 1.0")

        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.animating = False
        self.clock_pin = int(config.attributes.fields["clock_pin"].number_value)
        self.data_pin = int(config.attributes.fields["data_pin"].number_value)
        self.led_count = int(config.attributes.fields["led_count"].number_value)
        self.brightness = config.attributes.fields["default_brightness"].number_value or 1.0
        self.controller = WS2801(self.clock_pin, self.data_pin, self.led_count, brightness=self.brightness, auto_write=False)

        return

    """ Implement the methods the Viam RDK defines for the Rgb API (rdk:components:rgb) """

    async def animate(self) -> str:
        length = len(self.controller)
        while self.animating:
            for index in range(length):
                self.controller[index] = (self._random_color(), self._random_color(), self._random_color())

            self.controller.show()
            await asyncio.sleep(0.15)

        return "Ok"

    async def clear(self) -> str:
        self.controller.fill((0, 0, 0))
        self.controller.show()
        return "Ok"

    async def stop(self) -> str:
        self.animating = False
        return "Ok"

    def _random_color(self) -> int:
        return random.randrange(0, 7) * 32
