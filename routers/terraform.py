from service.impl.parser import TFParser
from service.impl.aws_parser import AWSParser
from service.impl.ncp_parser import NCPParser

def api_parser(path: str, provider: str="ncp"):

    if provider == "aws":
        parser = AWSParser(block=[], path=path)
        return parser.get_block_value()

    elif provider == "ncloud" or provider == "ncp":
        parser = NCPParser(block=[], path=path)
        return parser.get_block_value()

    return []