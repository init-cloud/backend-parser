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
        