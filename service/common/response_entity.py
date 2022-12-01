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

    def get_id(self) -> str:
        return self.id

    def get_resource_type(self) -> str:
        return self.resource_type

    def get_parent(self) -> str:
        return self.parent

    def get_label(self) -> str:
        return self.label


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

    def get_id(self) -> str:
        return self.id

    def get_resource_type(self) -> str:
        return self.resource_type

    def get_source(self) -> str:
        return self.source

    def get_target(self) -> str:
        return self.target


        