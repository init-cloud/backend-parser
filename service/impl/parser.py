from service.base_parser import BaseParser
from service.common.response_entity import Response, PeeringResponse
from service.enum.blocks import Block, NCPResource, AWSResource
from service.enum.blocks_tuple import NCPResourceTuple, AWSResourceTuple
from service.utils.network_attach import Attach
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

    def retrieve_ncp_resource(self, file_data) -> list:
        result = []
        multi_list = []

        for d in file_data:
            resource = next(iter(d))
            try:
                val = NCPResourceTuple[resource.upper()].value

                if val[1] == "connect":
                    b_s = self.connect_parse(d[val[0]])
                    if b_s:
                        result.append({"data": b_s[0]})
                elif val[1] == "multiconnect":
                    multi_list.append((d[val[0]], val[0]))
                else:
                    b_s = self.parse(d[val[0]], b_type=val[0])
                    if b_s:
                        result.append({"data": b_s[0]})
            except:
                b_s = self.parse(d[resource], b_type=resource)
                if b_s:
                    result.append({"data": b_s[0]})

        return result + self.multi_connect_parse(multi_list)

    def retrieve_aws(self):
        return

    def get_block_value(self, files: list) -> list:
        result = []

        for file in files:
            for k in file.keys():
                if k == Block.RESOURCE:
                    result += self.retrieve_ncp_resource(file[k])
                elif k == Block.PROVIDER:
                    provider = next(iter(file[k][0]))
                    b_s = self.parse(file[k][0], provider)
                    if b_s:
                        result.append({"data": b_s[0]})
                else:
                    continue

        return result

    def parse(self, blocks: dict, b_type: str=None, default_parent: str=None) -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            id = b_type + "." + k

            if "subnet_no" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["subnet_no"]))))
            elif "subnet_no_list" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["subnet_no_list"][0]))))
            elif "vpc_no" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["vpc_no"]))))
            elif "region" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["region"]))))
            else:
                result.append(
                    Response(bid=id, label=b_type, parent=default_parent))


        return result

    def connect_parse(self, blocks: dict) -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            if "source_vpc_no" in block and "target_vpc_no" in block:
                src=self.get_value(self.get_var(block["source_vpc_no"]))
                tar=self.get_value(self.get_var(block["target_vpc_no"]))
                id = src + "-" + tar
                result.append(
                    PeeringResponse(bid=id, source=src, target=tar))

        return result
    
    def multi_connect_parse(self, block_list: list) -> list:
        result = []
            
        for lb_blocks, lb_type in block_list:
            for k in lb_blocks:    
                block = lb_blocks[k]

                if "load_balancer_no" in block and "target_group_no" in block:
                    
                    src=self.get_value(self.get_var(block["load_balancer_no"]))
                    tar=self.get_value(self.get_var(block["target_group_no"]))
                    id = lb_type + "-" + tar
                    result.append({"data": PeeringResponse(bid=id, source=src, target=tar)})

                elif "target_group_no" in block and "target_no_list" in block:

                    for t in self.get_var_list(block["target_no_list"]):
                        src=self.get_value(self.get_var(block["target_group_no"]))
                        tar=self.get_value(t)
                        id = lb_type + "-" + tar
                        result.append({"data": PeeringResponse(bid=id, source=src, target=tar)})
                else:
                    continue
        
        return result
