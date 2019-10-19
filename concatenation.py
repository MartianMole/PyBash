from os import path
import makePath

__doc__ = '''
================cat===============
This command displays the contents of a text file.

==> Usage:
cat [keys] [path]

==> Keys:
-h help
-n number each line

==> Examples: 
cat file.txt
cat -n ..\folder\file

================cat===============
'''


class Concatenation:
    def __init__(self, keys, file, text, tk, curPath):
        self.keys = keys
        self.file = file
        self.text = text
        self.tk = tk
        self.curPath = curPath

    def makeKeysList(self):
        keys = self.keys
        result = set()
        for i in keys:
            if i[0] == '-':
                for j in i[1:]:
                    result.add(j)
            else:
                return 'Error: unknown key '
        return result

    def writeContent(self):
        keys = Concatenation.makeKeysList(self)
        text = self.text
        tk = self.tk
        file = '\\'.join(makePath.processingRequest(self.file, self.curPath))
        if not path.isfile(file):
            text.insert(tk.END, '\nError: ' + file + ' is not a file', 'err')
        if path.isfile(file):
            file = open(file, 'r')
            text.insert(tk.END, '\n')
            num = 1
            for line in file:
                text.insert(tk.END, (str(num) + ') ') * ('n' in keys) + line)
                num += 1

