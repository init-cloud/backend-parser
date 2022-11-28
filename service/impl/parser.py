from service.base_parser import BaseParser
from service.common.response_entity import Response, PeeringResponse
from service.enum.blocks import Block, NCPResource, AWSResource
from service.enum.blocks_tuple import NCPResourceTuple, AWSResourceTuple
from service.utils.network_attach import Attach
import os, hcl2


class TFParser(BaseParser):

    def __init__(self, path: str, block: list=[]) -> None:
        self.block = block
        self.path = path
        super().__init__()

    def load_file(self) -> list:
        for (root, directories, files) in os.walk(f'uploads/{self.path}/'):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path[-3:] != ".tf":
                    continue

                with open(file_path, 'r') as tf:
                    fs = hcl2.load(tf)

                    self.add(
                        data=fs[Block.DATA] if Block.DATA in fs else [],
                        resource=fs[Block.RESOURCE] if Block.RESOURCE in fs else [],
                        variable=fs[Block.VARIABLE] if Block.VARIABLE in fs else [])

                    self.block.append(fs)

        return self.block

    def get_value(self, var: str) -> str:

        v = var.split(".")

        if not v:
            return None

        if v[0] == 'var':
            return var
            
        result = self.find(v, v[0])
        return result

    def get_var(self, var) -> str:
        if isinstance(var, list) and var:
            if var[0].startswith("$"):
                return var[0][2:-1]
            else:
                if var.count(".") > 2:
                    li = var.split(".")
                    return li[0] + "." + li[1]

                return var[0]
        elif isinstance(var, str):
            if var.startswith("$"):
                return var[2:-1]
            else:
                return var

        return None

    def get_var_list(self, var: list, result: list=[]) -> list:
        for v in var:
            if v.startswith("$"):
                result.append(v[2:-1])
            else:
                result.append(v)

        return result
