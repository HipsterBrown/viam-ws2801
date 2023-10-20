"""
This file outlines the general structure for the API around a custom, modularized components.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the service,
and the gRPC client that will be able to make calls to this service.

In this example, the ``Rgb`` abstract class defines what functionality is required for all Rgb componentss.
It extends ``ServiceBase``, as all components types must.
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
from typing import Final, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_base import ServiceBase

from ..proto.rgb_grpc import RgbServiceBase, RgbServiceStub

# update the below with actual methods for your API!
from ..proto.rgb_pb2 import EchoRequest, EchoResponse


class Rgb(ServiceBase):
    """Example service to use with the example module"""

    SUBTYPE: Final = Subtype("hipsterbrown", RESOURCE_TYPE_SERVICE, "rgb")

    # update with actual API methods
    @abc.abstractmethod
    async def echo(self, text: str) -> str:
        ...

class RgbRPCService(RgbServiceBase, ResourceRPCServiceBase):
    """Example gRPC service for the Speech service"""

    RESOURCE_TYPE = RgbService

    # update with actual API methods
    async def Echo(self, stream: Stream[EchoRequest, EchoResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.say(request.text)
        await stream.send_message(EchoResponse(text=resp))

class RgbClient(RgbService):
    """Example gRPC client for the Speech Service"""

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = RgbServiceStub(channel)
        super().__init__(name)

    # update with actual API methods
    async def echo(self, text: str) -> str:
        request = EchoRequest(name=self.name, text=text)
        response: EchoResponse = await self.client.Echo(request)
        return response.text