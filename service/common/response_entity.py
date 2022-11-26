class Response():
    def __init__(
        self,
        resource_type: str="node",
        bid: str=None,
        label=None,
        parent=None
    ) -> None:
        self.resource_type = resource_type
        self.id = bid
        self.label = label if label else bid
        self.parent = parent

class PeeringResponse():
    def __init__(
        self,
        resource_type: str="connect",
        bid: str=None,
        source: str=None,
        target: str=None
    ) -> None:
        self.resource_type = resource_type
        self.id = bid
        self.source = source
        self.target = target
        