from service.common.response_entity import Response
from service.enum.blocks import Block, NCPResource
import hcl2


class TFParser():
    def __init__(self, block=dict()) -> None:
        self.block = block

    def load_file(self) -> dict:
        with open('static/main.tf', 'r') as tf:
            self.block = hcl2.load(tf)
            return self.block

    ##
    # temp
    ##
    def get_var(self, var: list) -> str:
        if var:
            if var[0].startswith("$"):
                return var[0][2:-1]
            else:
                return var[0]

    def get_block_value(self, file: dict) -> list:
        res = []
        for k in file.keys():
            if k == Block.RESOURCE:
                for d in file[k]:
                    if NCPResource.NCLOUD_SUBNET in d:
                        res.append({ "data" : self.parse(d[NCPResource.NCLOUD_SUBNET],
                                            b_type=NCPResource.NCLOUD_SUBNET)[0]})
                    elif NCPResource.NCLOUD_SERVER in d:
                        res.append({ "data" : self.parse(d[NCPResource.NCLOUD_SERVER],
                                            b_type=NCPResource.NCLOUD_SERVER)[0]})
                    else:
                        continue

        return res

    def parse(self, blocks, b_type=None) -> list:
        result = []

        for k in blocks.keys():
            block = blocks[k]

            if "subnet_no" in block:
                result.append(
                    Response(k, b_type, self.get_var(block["subnet_no"]))
                )
            elif "vpc_no" in block:
                result.append(
                    Response(k, b_type, self.get_var(block["vpc_no"]))
                )

        return result
