class Response():
    def __init__(
        self,
        bid: str,
        label=None,
        parent=None
    ) -> None:
        self.id = bid
        self.label = label if label else bid
        self.parent = parent

class PeeringResponse():
    def __init__(
        self,
        bid: str,
        source: str=None,
        target: str=None
    ) -> None:
        self.id = bid
        self.source = source
        self.target = target
        