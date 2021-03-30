import os

class FileIO:
    '''
    File input output handler
    '''
    def __init__(self):
        pass
    def get_absolute_path(self, paths: list):
        '''

        :param paths: list of string each being next path depth starting with the next dir after current working dir
        :return: operating system invariant absolute path
        '''
        absolute_path = os.path.join(str(os.getcwd()), *paths)
        return absolute_path

    def read_file(self, file_path: str) -> list:
        '''

        :param file_path: absolute path to read
        :return: list of oligonucletides
        '''
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
        return lines