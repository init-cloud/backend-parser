from service.common.response_entity import PeeringResponse, Response
from service.enum.blocks import Block
from service.enum.blocks_tuple import NCPResourceTuple
from service.impl.parser import TFParser


class NCPParser(TFParser):

    def __init__(self, path: str, block: list=[]) -> None:
        super().__init__(path=path, block=block)
        self.block = self.load_file()

    def get_block_value(self) -> list:
        result = []

        for file in self.block:
            for k in file.keys():
                if k == Block.PROVIDER:
                    provider = next(iter(file[k][0]))
                    b_s = self.parse(file[k][0], provider)
                    if b_s:
                        result.append({"data": b_s[0]})
                elif k == Block.RESOURCE:
                    result += self.retrieve_ncp_resource(file[k])
                else:
                    continue

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