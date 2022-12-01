from service.base_parser import BaseParser
from service.common.response_entity import Response, PeeringResponse
from service.enum.blocks import Block, NCPResource, AWSResource
from service.enum.blocks_tuple import NCPResourceTuple, AWSResourceTuple
from service.utils.network_attach import Attach
import os, hcl2


class TFParser():

    def __init__(self, path: str, directory: str="/", raw_block: list=[]) -> None:
        self.directory = directory
        self.raw_block = raw_block
        self.path = path

    def load_file(self) -> list:
        for (root, directories, files) in os.walk(f'uploads/{self.path}/'):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path[-3:] != ".tf":
                    continue

                with open(file_path, 'r') as tf:
                    fs = hcl2.load(tf)
                    self.raw_block.append((root.split(self.path)[1], fs))

        return self.raw_block

    def get_value(self, var: str, file_path: str="/", is_provider=False) -> str:

        v = var.split(".")

        if not v:
            return None

        if v[0] == 'var':
            return file_path + "\n" + var

        if v[0] == 'data':
            return file_path + "\n" + ".".join(v[0:-1])
            
        result = self.find(v, v[0])

        if is_provider:
            return result

        return file_path + "\n" + result

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

    def find(self, va: list, type: str=None) -> str:

        if type == Block.DATA:
            return va[1] + "." + va[2]
        elif type == Block.VARIABLE or type == "var":
            return va[1]
        elif len(va) > 1:
            result = (va[0] + "." + va[1]).split("[")
            return result[0]
        elif va:
            return va[0]
        
        return va
