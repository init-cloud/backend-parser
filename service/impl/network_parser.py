from service.base_parser import BaseParser
import hcl2


class NetworkParser(BaseParser):

    def __init__(
        self,
        file
    ) -> None:
        with open(file, 'r') as tf:
            file_dict = hcl2.load(tf)
            super.__init__(file=file_dict)
