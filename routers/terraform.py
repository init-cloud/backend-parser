from service.impl.parser import TFParser

def api_parser(path: str):
    parser = TFParser(block=[])
    f = parser.load_file(path)
    res = parser.get_block_value(f)

    return res