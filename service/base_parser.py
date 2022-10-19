class BaseParser():

    def __init__(
        self, 
        file
    ) -> None:
        self.file = file
        datas     = []
        local     = []
        module    = []
        output    = []
        provider  = []
        resource  = []
        terraform = []
        variable  = []
