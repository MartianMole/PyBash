import os
import changeDir


__doc__ = '''
=============ls=============
Command showing list of directories and files
==> Usage:
cd [keys]
==> Keys:
==> Examples: 
=============ls=============
'''


class Ls:
    def __init__(self, keys, path):
        self.keys = keys

    def showList(self):
        keys = self.keys
        if not keys:
            return os.listdir(path)
