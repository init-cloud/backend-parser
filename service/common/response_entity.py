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
        label: str=None,
        name: str=None,
        src: str=None,
        tar: str=None
    ) -> None:
        self.id = bid
        self.label = label if label else bid
        self.name = name
        self.src = src
        self.tar = tar
        