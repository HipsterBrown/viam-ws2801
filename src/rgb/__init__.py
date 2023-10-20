"""
This file registers the model with the Python SDK.
"""

from viam.components.rgb import Rgb
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .ws2801 import ws2801

Registry.register_resource_creator(Rgb.SUBTYPE, ws2801.MODEL, ResourceCreatorRegistration(ws2801.new, ws2801.validate))
