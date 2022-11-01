from service.base_parser import BaseParser
from service.common.response_entity import Response
from service.enum.blocks import Block, NCPResource
import os, hcl2


class TFParser(BaseParser):
    def __init__(self, block=[]) -> None:
        self.block = block
        super().__init__()

    def load_file(self, path: str) -> list:
        for (root, directories, files) in os.walk(f'uploads/{path}/'):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path[-3:] != ".tf":
                    continue

                with open(file_path, 'r') as tf:
                    fs = hcl2.load(tf)
                    self.add(
                        data=fs[Block.DATA],
                        resource=fs[Block.RESOURCE],
                        variable=fs[Block.VARIABLE])

                    self.block.append(fs)

        return self.block

    def get_value(self, var: str) -> str:
        v = var.split(".")

        if not v:
            return None
        
        result = self.find(v, v[0])

        return result

    def get_var(self, var) -> str:
        if isinstance(var, list) and var:
            if var[0].startswith("$"):
                return var[0][2:-1]
            else:
                return var[0]
        elif isinstance(var, str):
            if var.startswith("$"):
                return var[2:-1]
            else:
                return var

        return None

    def get_block_value(self, files: list) -> list:
        result = []

        for file in files:
            for k in file.keys():
                if k == Block.RESOURCE:
                    for d in file[k]:
                        if NCPResource.NCLOUD_SUBNET in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_SUBNET],
                                                b_type=NCPResource.NCLOUD_SUBNET)[0]})
                        elif NCPResource.NCLOUD_SERVER in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_SERVER],
                                                b_type=NCPResource.NCLOUD_SERVER)[0]})
                        elif NCPResource.NCLOUD_LB_TARGET_GROUP in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_LB_TARGET_GROUP],
                                                b_type=NCPResource.NCLOUD_LB_TARGET_GROUP)[0]})
                        elif NCPResource.NCLOUD_ACCESS_CONTROL_GROUP in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_ACCESS_CONTROL_GROUP],
                                                b_type=NCPResource.NCLOUD_ACCESS_CONTROL_GROUP)[0]})
                        elif NCPResource.NCLOUD_NETWORK_ACL in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_NETWORK_ACL],
                                                b_type=NCPResource.NCLOUD_NETWORK_ACL)[0]})
                        elif NCPResource.NCLOUD_NETWORK_INTERFACE in d:
                            result.append({ "data" : self.parse(d[NCPResource.NCLOUD_NETWORK_INTERFACE],
                                                b_type=NCPResource.NCLOUD_NETWORK_INTERFACE)[0]})
                        else:
                            continue

        return result

    def parse(self, blocks: dict, b_type=None) -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            if "subnet_no" in block:
                result.append(
                    Response(k, b_type, parent=self.get_value(self.get_var(block["subnet_no"]))))
            elif "vpc_no" in block:
                result.append(
                    Response(k, b_type, parent=self.get_value(self.get_var(block["vpc_no"]))))
            elif "region" in block:
                result.append(
                    Response(k, b_type, parent=self.get_value(self.get_var(block["region"]))))

        return result
