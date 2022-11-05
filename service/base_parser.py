from service.enum.blocks import Block

class BaseParser():

    def __init__(
        self,
        data: list = [],
        local: list = [],
        module: list = [],
        output: list = [],
        provider: list = [],
        resource: list = [],
        terraform: list = [],
        variable: list = []
    ) -> None:
        self.data      = data 
        self.local     = local
        self.module    = module
        self.output    = output
        self.provider  = provider
        self.resource  = resource
        self.terraform = terraform
        self.variable  = variable

    def add(
        self,
        data: list=[],
        local: list=[],
        module: list=[],
        output: list=[],
        provider: list=[],
        resource: list=[],
        terraform: list=[],
        variable: list=[]
    ) -> None:
        self.data += data
        self.local += local
        self.module += module
        self.output += output
        self.provider += provider
        self.resource += resource
        self.terraform += terraform
        self.variable += variable

    def find(
        self,
        va: list,
        type: str=None
    ) -> str:
        if type == Block.DATA:
            return va[1] + "." + va[2]
        elif type == Block.VARIABLE or type == "var":
            return va[1]
        else:
            result = (va[0] + "." + va[1]).split("[")
            return result[0]