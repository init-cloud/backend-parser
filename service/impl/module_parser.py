import os, hcl2

from typing import Tuple
from service.enum.blocks import Block

class ModuleParser():
    def __init__(self, path: str, directory: str="/", block: list=[]) -> None:
        self.directory = directory
        self.path = path
        self.block = block
        
        self.get_module_block()

    # ㅎㅎ
    def get_module_block(self) -> Tuple[dict, dict]:
        self.output = {}
        self.variable = {}
        self.module = {}

        for file_path, file in self.block:
            for k in file.keys():
                target = file[k]

                if k == Block.OUTPUT:
                    ret_path, ret_block = self.retrieve_output(target, file_path)
                    if ret_path in self.output:
                        self.output[ret_path] += ret_block
                    else:
                        self.output[ret_path] = ret_block

                elif k == Block.VARIABLE:
                    ret_path, ret_block = self.retrieve_variable(target, file_path)
                    if ret_path in self.variable:
                        self.variable[ret_path] += ret_block
                    else:
                        self.variable[ret_path] = ret_block

                elif k == Block.MODULE:
                    ret_path, ret_block = self.retrieve_module(target, file_path)
                    if ret_path in self.module:
                        self.module[ret_path] += ret_block
                    else:
                        self.module[ret_path] = ret_block

        for file_path, file in self.block:
            for k in file.keys():
                target = file[k]

                if k == Block.RESOURCE:
                    self.traverseRawBlocks(file, file_path)

                elif k == Block.MODULE:
                    for i in file[k]:
                        for key, val in i.items():  
                            if self._isRelative(val['source']):
                                relative = self._RelativeToAbsolute(file_path, val['source'])
                                i[key]['source'] = relative

        return self.output, self.variable


    # Precondition and Optional Arguments are not considered
    # https://developer.hashicorp.com/terraform/language/values/outputs
    # 01. Local paths
    # 02. Terraform Registry
    def retrieve_output(self, file_data, file_path="/") -> Tuple[str, dict]:
        blocks = {}

        for d in file_data:
            output = next(iter(d))
            blocks[output] = d[output]['value'][2:-1]

        return (file_path, blocks)

    # https://github.com/cand0/InitCloud/tree/main/module/vpc_module
    # 위 케이스에 한하여 적용 할 필요 없음
    def retrieve_variable(self, file_data, file_path="/") -> Tuple[str, dict]:
        blocks = {}
        
        for d in file_data: 
            output = next(iter(d))
            blocks[output] = {'type' : d[output]['type'][2:-1]}

        return (file_path, blocks)

    def retrieve_module(self, file_data, file_path="/") -> Tuple[str, dict]:
        blocks = {}

        for d in file_data:
            output = next(iter(d))
            blocks[output] = d[output]

        return (file_path, blocks)

    def traverseRawBlocks(self, blocks, file_path):
        for key, value in blocks.items():
            if isinstance(value, str):
                # 문자열 탐색에서 속도 고려 안했지만 내 알빠 아님
                if 'module.' in value:
                    value, source, blockName = self._getModuleInfo(value, file_path)
                    blocks[key] = value
                    i = self._getIndex(file_path)

            elif isinstance(value, list):
                for item in value:
                    if not isinstance(item, str):
                        self.traverseRawBlocks(item, file_path)

                    # 문자열 탐색에서 속도 고려 안했지만 내 알빠 아님
                    # 검증 안됌
                    elif 'module.' in item:
                        item, source, blockName = self._getModuleInfo(item, file_path)
                        blocks[key] = value

            elif isinstance(value, dict):
                self.traverseRawBlocks(value, file_path)
        
    
    def _getModuleInfo(self, block: str, file_path):
        blocks = block.split('.')
        blockName = blocks[1]
        source = self.module[file_path][blockName]['source']

        propertyName = blocks[2].split('}')[0]

        if self._isRelative(source):
            source = self._RelativeToAbsolute(file_path, source)

        try : 
            return self.output[source][propertyName], source, blockName
        except Exception as e:
            print(e.message)
            return propertyName, source, blockName
        

    def _isRelative(self, path: str) -> bool:
        path = path.split('${')[0]
        if path.startswith('.'):
            return True

        return False


    def _RelativeToAbsolute(self, file_path: str, source: str) -> str:
        pwd = file_path.split('/')
        path = source.split('/')

        length = len(path)
        for i in range(length):
            if path[0] == '..':
                pwd.pop()

            elif path[0] != '.':
                pwd.append(path[0])

            if len(path) > 1:
                path = path[1:]

        absolutePath = ''
        for i in pwd:
            if i != '':
                absolutePath += '/' + i
        
        return absolutePath
    
    def _getIndex(self, s: str):
        for i in range(len(self.block)):
            if self.block[i][0] == s:
                return i