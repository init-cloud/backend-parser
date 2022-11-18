from service.base_parser import BaseParser
from service.common.response_entity import Response, PeeringResponse
from service.enum.blocks import Block, NCPResource
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

    def get_block_value(self, files: list) -> list:
        result, lb_list = [], []

        for file in files:
            for k in file.keys():
                if k == Block.RESOURCE:
                    for d in file[k]:
                        if NCPResource.NCLOUD_SUBNET in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_SUBNET],
                                                b_type=NCPResource.NCLOUD_SUBNET)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_SERVER in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_SERVER],
                                                b_type=NCPResource.NCLOUD_SERVER)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_ACCESS_CONTROL_GROUP in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_ACCESS_CONTROL_GROUP],
                                                b_type=NCPResource.NCLOUD_ACCESS_CONTROL_GROUP)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_AUTO_SCALING_GROUP in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_AUTO_SCALING_GROUP],
                                                b_type=NCPResource.NCLOUD_AUTO_SCALING_GROUP)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_NETWORK_ACL in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_NETWORK_ACL],
                                                b_type=NCPResource.NCLOUD_NETWORK_ACL)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_NETWORK_INTERFACE in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_NETWORK_INTERFACE],
                                                b_type=NCPResource.NCLOUD_NETWORK_INTERFACE)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_VPC in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_VPC],
                                                b_type=NCPResource.NCLOUD_VPC)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_LB_TARGET_GROUP in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_LB_TARGET_GROUP],
                                                b_type=NCPResource.NCLOUD_LB_TARGET_GROUP)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_LB in d:
                            b_s = self.parse(d[NCPResource.NCLOUD_LB],
                                                b_type=NCPResource.NCLOUD_LB)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_VPC_PEERING in d:
                            b_s = self.peering_parse(d[NCPResource.NCLOUD_VPC_PEERING],
                                                b_type=NCPResource.NCLOUD_VPC_PEERING)
                            if b_s:
                                result.append({"data": b_s[0]})
                        elif NCPResource.NCLOUD_LB_LISTENER in d:
                            lb_list.append((d[NCPResource.NCLOUD_LB_LISTENER], 
                                        NCPResource.NCLOUD_LB_LISTENER))
                        elif NCPResource.NCLOUD_LB_TARGET_GROUP_ATTACHMENT in d:
                            lb_list.append((d[NCPResource.NCLOUD_LB_TARGET_GROUP_ATTACHMENT], 
                                        NCPResource.NCLOUD_LB_TARGET_GROUP_ATTACHMENT))
                        else:
                            continue
        
        result += self.lb_parse(lb_list)

        return result

    def parse(self, blocks: dict, b_type: str=None) -> list:
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
                    Response(bid=id, label=b_type, parent=None))


        return result

    def peering_parse(self, blocks: dict, b_type: str=None) -> list:
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

    def lb_parse(self, lb_block_list: list) -> list:
        result = []

        for lb_blocks, lb_type in lb_block_list:
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

        #attach = Attach(result, dict())

        return result