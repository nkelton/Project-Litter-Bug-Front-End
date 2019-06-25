from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from content.bindings import ContentBinding
from script.bindings import ScriptBinding


class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
        'script': ScriptBinding.consumer,
        'content': ContentBinding.consumer
    }


channel_routing = [
    route_class(APIDemultiplexer)
]