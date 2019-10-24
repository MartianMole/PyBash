from os import path
import makePath
import makeKeysList

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

    def writeContent(self):
        keys = makeKeysList.makeKeysList(self.keys, 'nh')
        text = self.text
        tk = self.tk
        file = '\\'.join(makePath.processingRequest(self.file, self.curPath))
        if keys.split()[0] == 'Error:':
            text.insert(tk.END, '\n' + keys, 'err')
            return
        if not path.isfile(file):
            text.insert(tk.END, '\nError: ' + file + ' is not a file', 'err')
        if path.isfile(file):
            file = open(file, 'r')
            text.insert(tk.END, '\n')
            num = 1
            for line in file:
                text.insert(tk.END, (str(num) + ') ') * ('n' in keys) + line)
                num += 1

