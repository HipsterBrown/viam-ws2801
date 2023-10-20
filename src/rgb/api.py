"""
This file outlines the general structure for the API around a custom, modularized components.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the service,
and the gRPC client that will be able to make calls to this service.

In this example, the ``Rgb`` abstract class defines what functionality is required for all Rgb componentss.
It extends ``ComponentBase``, as all components types must.
It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``RgbRPCService`` implements the gRPC service for the Rgb components. This will allow other robots and clients to make
requests of the Rgb components. It extends both from ``RgbServiceBase`` and ``RPCServiceBase``.
The former is the gRPC service as defined by the proto, and the latter is the class that all gRPC services must inherit from.

Finally, the ``RgbClient`` is the gRPC client for a Rgb components. It inherits from RgbService since it implements
 all the same functions. The implementations are simply gRPC calls to some remote Rgb components.

To see how this custom modular components is registered, see the __init__.py file.
To see the custom implementation of this components, see the ws2801.py file.
"""

import abc
from typing import Final

from grpclib.client import Channel
from grpclib.server import Stream

from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import Subtype, RESOURCE_TYPE_COMPONENT
from viam.components.component_base import ComponentBase

from .proto.rgb_grpc import RgbServiceBase, RgbServiceStub

# update the below with actual methods for your API!
from .proto.rgb_pb2 import AnimateRequest, AnimateResponse, ClearRequest, ClearResponse, StopRequest, StopResponse


class Rgb(ComponentBase):
    """Example service to use with the example module"""

    SUBTYPE: Final = Subtype("hipsterbrown", RESOURCE_TYPE_COMPONENT, "rgb")

    @abc.abstractmethod
    async def animate(self) -> str:
        ...

    @abc.abstractmethod
    async def clear(self) -> str:
        ...

    @abc.abstractmethod
    async def stop(self) -> str:
        ...

class RgbRPCService(RgbServiceBase, ResourceRPCServiceBase):
    """gRPC service for the Rgb Component"""

    RESOURCE_TYPE = Rgb

    async def Animate(self, stream: Stream[AnimateRequest, AnimateResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.animate()
        await stream.send_message(AnimateResponse(text=resp))

    async def Clear(self, stream: Stream[ClearRequest, ClearResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.animate()
        await stream.send_message(ClearResponse(text=resp))

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.animate()
        await stream.send_message(StopResponse(text=resp))

class RgbClient(Rgb):
    """gRPC client for the Rgb Component"""

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = RgbServiceStub(channel)
        super().__init__(name)

    async def animate(self) -> str:
        request = AnimateRequest(name=self.name)
        response: AnimateResponse = await self.client.Animate(request)
        return response.text

    async def clear(self) -> str:
        request = ClearRequest(name=self.name)
        response: ClearResponse = await self.client.Clear(request)
        return response.text

    async def stop(self) -> str:
        request = StopRequest(name=self.name)
        response: StopResponse = await self.client.Stop(request)
        return response.text
