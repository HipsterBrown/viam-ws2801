"""
This file registers the model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration, ResourceRegistration

from .api import Rgb, RgbRPCService, RgbClient
from .ws2801 import ws2801

Registry.register_subtype(ResourceRegistration(Rgb, RgbRPCService, lambda name, channel: RgbClient(name, channel)))

Registry.register_resource_creator(Rgb.SUBTYPE, ws2801.MODEL, ResourceCreatorRegistration(ws2801.new, ws2801.validate))
