from service.common.response_entity import PeeringResponse, Response
from service.enum.blocks import Block
from service.enum.blocks_tuple import AWSResourceTuple
from service.impl.parser import TFParser


class AWSParser(TFParser):

    def __init__(self, path: str, block: list=[]) -> None:
        super().__init__(path=path, raw_block=block)
        self.block = self.load_file()

    def get_block_value(self) -> list:
        result = []

        for file_path, file in self.block:
            for k in file.keys():
                target = file[k]
                if k == Block.RESOURCE:
                    result += self.retrieve_aws_resource(target, file_path)
                elif k == Block.PROVIDER:
                    provider = next(iter(target[0]))
                    b_s = self.parse(target[0], provider, file_path)
                    if b_s:
                        result.append({"data": b_s[0]})
                else:
                    continue

        return result

    def retrieve_aws_resource(self, file_data, file_path="/") -> list:
        result = []
        multi_list = []

        for d in file_data:
            resource = next(iter(d))
            try:
                val = AWSResourceTuple[resource.upper()].value

                if val[1] == "connect":
                    b_s = self.connect_parse(d[val[0]], file_path)
                    if b_s:
                        result.append({"data": b_s[0]})
                elif val[1] == "multiconnect":
                    multi_list.append((d[val[0]], val[0], file_path))
                else:
                    b_s = self.parse(d[val[0]], b_type=val[0], file_path=file_path)
                    if b_s:
                        result.append({"data": b_s[0]})
            except:
                b_s = self.parse(d[resource], b_type=resource, file_path=file_path)
                if b_s:
                    result.append({"data": b_s[0]})

        return result + self.multi_connect_parse(multi_list)

    def parse(self, blocks: dict, b_type: str=None, default_parent: str=None, file_path: str="/") -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            id = file_path + "\n" + b_type + "." + k

            if "subnet_id" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["subnet_id"]), file_path)))
            elif "vpc_id" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["vpc_id"]), file_path)))
            elif "region" in block:
                result.append(
                    Response(bid=id, label=b_type, parent=self.get_value(self.get_var(block["region"]), file_path)))
            else:
                result.append(
                    Response(bid=id, label=b_type, parent=default_parent))


        return result

    def connect_parse(self, blocks: dict, file_path: str) -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            if "vpc_id" in block and "peer_vpc_id" in block:
                src=self.get_value(self.get_var(block["vpc_id"]), file_path)
                tar=self.get_value(self.get_var(block["peer_vpc_id"]), file_path)
                id = src + "-" + tar
                result.append(
                    PeeringResponse(bid=id, source=src, target=tar))

        return result
    
    def multi_connect_parse(self, block_list: list) -> list:
        result = []
            
        for lb_blocks, lb_type, file_path in block_list:
            for k in lb_blocks:    
                block = lb_blocks[k]

                if "load_balancer_no" in block and "target_group_no" in block:
                    
                    src=self.get_value(self.get_var(block["load_balancer_no"]), file_path)
                    tar=self.get_value(self.get_var(block["target_group_no"]), file_path)
                    id = lb_type + "-" + tar
                    result.append({"data": PeeringResponse(bid=id, source=src, target=tar)})

                elif "target_group_no" in block and "target_no_list" in block:

                    for t in self.get_var_list(block["target_no_list"]):
                        src=self.get_value(self.get_var(block["target_group_no"]), file_path)
                        tar=self.get_value(t, file_path)
                        id = file_path + "\n" + lb_type + "-" + tar
                        result.append({"data": PeeringResponse(bid=id, source=src, target=tar)})
                else:
                    continue
        
        return result